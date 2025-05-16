from flask_restful import Api
from flask import Flask,request,current_app
import MySQLdb
from resources.login import Login
from resources.Register import Register
from resources.events import events,event
import jwt

from db import mysql

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Chukwuma@1231'
app.config['MYSQL_DB'] = 'ai_scheduler'
app.config['token'] = '6828043811'
app.config['SENDGD_API_KEY'] = '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'

mysql.init_app(app)


api.add_resource(Login, '/login')         # your frontend can POST or GET to this
api.add_resource(Register, '/register')   # your frontend can POST to this
api.add_resource(event, '/event')
api.add_resource(events, '/events')

@app.route('/verify-email', methods = ['GET'])
def verify_email():
    token = request.args.get('token')


    try:
        data = jwt.decode(token, current_app.config['token'],algorithms='HS256')
        email = data['email']


        cur = mysql.connection.cursor()
        cur.execute('update User Set verified = 1 where email = %s', (email,))
        mysql.connection.commit()
        cur.close()

        return {'message' : 'Email verified. You may now login'},200
    
    except jwt.ExpiredSignatureError: 
        return {'message' : 'Email link has expired'},400
    
    except jwt.InvalidTokenError:
        return {'message': 'Invalid or malformed token'}, 400


@app.route("/")
def hello_world():
    return "<p> hello world! </p>"


if __name__ == "__main__":
    app.run()