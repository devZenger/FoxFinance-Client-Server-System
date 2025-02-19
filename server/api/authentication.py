from flask import Flask, request
from flask_restx import Namespace, Resource


login_user_ns = Namespace ("login_user_ns", description="User login")


@login_user_ns.route("/")
class LoginUser(Resource):
    def post(self):
        try:
            data = request.get_json()
            
            return {"message":"Test erfolgreich"}, 200
        except Exception as e:
            return {"error:" f"{e} error orccurred"}, 500