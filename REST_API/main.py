# import resource
# from typing_extensions import Required
from email import message
from django import views
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from requests import delete
# from numpy import require
# from sqlalchemy import true
from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
db.create_all()

class VideoModel(db.Model):
    id = db.Column(db.Integer , primary_key =True)
    name = db.Column(db.String(100), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required = True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)


# names = {"bill" : {"age" : 70, "gender" : "male"},
#         "barbara" :  {"age" : 23, "gender" : "female"}}

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message = "Video id is not valid...")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="video already exists with that ID...")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
  
    def put(self,video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204


# class HelloWorld(Resource):
#     def get(self,name):
#         # return {"name" : name, "test": test} 1
#         return names[name]


    # def post(self):00
    #     return {"data" : "hi"} 00

# api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")1
# api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True) # put false in production, only in development it should be true. logs everything 

