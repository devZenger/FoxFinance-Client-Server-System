from flask import Flask
from flask_restx import Namespace, Resource


information_ns = Namespace ("information_ns", description="Information about Fox Finance")


@information_ns.route("/")
class Information(Resource):
    def get(self):
        return {"message":"Test erfolgreich"}, 200