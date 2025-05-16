from flask import request,jsonify,Response,current_app
from flask_restful import Resource
import requests
import re
import MySQLdb
from db import mysql
from Auth import gen_ver_token
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Register(Resource):

    def validate_email(self,email):

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(email_regex,email):
            return True
        
        else:
            return False


    def validate_password(self,password):

        if len(password) < 8:
            return False

        capital = re.search(r'[A-Z]', password)
        symbol = re.search(r'[!@#$%^&*()<>,./?;:{}|\\[\]]', password)
        number = re.search(r'\d',password)


        if capital and symbol and number:
            return True
        
        else:
            return False
        
    def send_ver_email(self,email,token):
        verification_link = f"http://localhost:5000/verify-email?token={token}"

        message = Mail(
            from_email='nwosuleon@gmail.com',
            to_emails=email,
            subject = 'verify Your Email Address',
            html_content= f"""<p>Hello,</p>
                <p>Please click the link below to verify your email address:</p>
                <a href="{verification_link}">{verification_link}</a>
                <p>This link will expire in 30 minutes.</p>
            """
        )

        try:
            sg = SendGridAPIClient(current_app.config['SENDGD_API_KEY'])
            response = sg.send(message)
            print(f"Email sent to {email}, status: {response.status_code}")
        except Exception as e:
            print(f"Error sending verification email: {e}")


    def post(self):
        data = request.get_json()

        email = data.get('email')
        
        password = data.get('password')

        user_name = data.get('username')

        if not email or not password or not user_name:
            return {'message': 'one of the mandatory fields is blank'},401



        if not self.validate_password(password):
            return {'message': 'enter correct password'},401
        
        if not self.validate_email(email):
            return {'message': 'enter correct email address'},401
        
        cur = mysql.connection.cursor()
        cur.execute('select * from getuser where email = %s', (email,))
        result = cur.fetchone()

        if result is None:
            cur.execute("Insert into User(user_name, password_hash, email) values(%s,%s,%s)",(user_name,password,email))
            mysql.connection.commit()
            cur.close()
            token = gen_ver_token(email)
            self.send_ver_email(email,token)
            

        else:
            cur.close()
            return {'message' : 'email has already been registered'}, 409

        return {'message': f"user {user_name} has been registered"}, 200


