from flask import Flask,request,jsonify, Response
from flask_restful import Resource
import requests
from Auth import token_required
from db import mysql
from datetime import datetime


class events(Resource):
    @token_required
    def get(self,current_user_id):

        data = request.get_json()
       
        if current_user_id is None:
            return {'message' : 'error'},401
        
        cur = mysql.connection.cursor()
        cur.execute("Select * from getallevents where user_id = %d",(current_user_id,))
        result = cur.fetchall()

        if result is None:
            cur.close()
            return {'message' : 'no events found'},401
        
        else:
            column_names = [desc[0] for desc in cur.description]
            cur.close()

            event_dict = {}
            for row in result:
                row_dict = dict(zip(column_names,row))
                event_id = row_dict.pop('event_id')
                event_dict[str(event_id)] = row_dict

            return event_dict, 200
        

class event(Resource):
    @token_required
    def get(self, current_user_id):

        data = request.get_json()

        event_id = data.get('event_id')

        if current_user_id is None:
            return {'message' : 'error'}, 401
        
        cur = mysql.connection.cursor()
        cur.execute("select * from getsingleevents where event_id = %d and user_id = %d", (event_id,current_user_id))
        result = cur.fetchone()


        if result is None:
            cur.close()
            return {'message': 'no event found'}, 401
        
        else:
            column_names = [desc[0] for desc in cur.description]
            cur.close()
            current_event = dict(zip(column_names,result))
            return current_event, 200   

    @token_required
    def post(self,current_user_id):
        data = request.get_json()

        title = data.get('title')
        start_str = data.get('start_time')
        end_str = data.get('end_time')
        start_time = datetime.fromisoformat(start_str)
        end_time = datetime.fromisoformat(end_str)
        event_type = data.get('event_type')

        try:
            cur = mysql.connection.cursor()
            cur.execute("Insert into events(user_id,title,start_time,end_time,event_type) values(%s,%s,%s,%s,%s)", (current_user_id,title,start_time,end_time,event_type))
            mysql.connection.commit()
            cur.close()


            return {'message' : 'new event created'}, 200
        except Exception as e:
            return {'message' : f'error {e}'}


