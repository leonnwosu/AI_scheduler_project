from flask import request,jsonify,Response
from flask_restful import Resource
import requests
import re
import MySQLdb
from db import mysql
import jwt
import datetime
from Auth import gen_token


class Login(Resource):
    def post(self):
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {'error' : 'enter information '}, 400
        
        cur = mysql.connection.cursor()
        cur.execute("select * From getuser where email = %s And password_hash = %s",(email, password))
        result = cur.fetchone()

        if result is None:
            cur.close()
            return {'message': 'user not found'}, 401
        else:
            column_names = [desc[0] for desc in cur.description]
            cur.close()
            user_data = dict(zip(column_names,result))
            token = gen_token(user_data.get('user_id'))
            return {'username': user_data.get('user_name'),
                    'token' : token}, 200
        
    
        
        
        
        
    

        
        


    







    

