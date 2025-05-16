"""TO-DO:
        remove the token generator form the login resouse and add the function here
        add the token decorator function here for the events resouse
        import this file into events and login/registration
"""



import jwt
import datetime
from flask import current_app, request
from functools import wraps


def gen_token(user_id):
        token = jwt.encode({
            'user_id' : user_id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours = 1)
        },current_app.config['token'], algorithm= 'HS256')

        return token

def gen_ver_token(email):
        token = jwt.encode({
                'email' : email,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=15) 
        }, current_app.config['token'], algorithm='HS256')

        return token

 


def token_required(f):
        @wraps(f)
        def decorated(*args,**kwargs):
                if 'Authorization' in request.headers:
                        auth_header = request.headers['Authorization']
                        if auth_header.startswith("Bearer"):
                                token = auth_header.split(" ")[1]

                if not token:
                        return {'message' : 'Token is missing'},401
                
                try:
                        data = jwt.decode(token,current_app.config['token'],algorithm=['HS256'])
                        current_user_id = data['user_id']
                except jwt.ExpiredSignatureError:
                        return {'message' : 'token has expired'}, 401
                
                except jwt.InvalidTokenError:
                        return {'message' : 'Invalid token'}, 401
                
                return f(current_user_id,*args,**kwargs)
        





                
