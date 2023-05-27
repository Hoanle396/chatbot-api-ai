from flask import jsonify, request, send_file
from flask_cors import cross_origin
import datetime


def registryRouter(app, model):
    @app.route("/", methods=["GET"])
    @cross_origin()
    def hello():
        return "Hello world"

    @app.route("/api/chat", methods=["POST"])
    def chat():
        msg = request.json["msg"]
        chat = str(model.chat(msg))
        return {"user": "BOT", "text": chat, "createdAt": datetime.datetime.now()}, 200

