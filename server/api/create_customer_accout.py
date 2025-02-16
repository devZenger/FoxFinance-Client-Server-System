from flask import Flask, request
from flask_restx import Namespace, Resource


create_customer_account_ns = Namespace ("create_customer_account_ns", description="Create customer account")


@create_customer_account_ns.route("/")
class CreateCustomerAccount(Resource):
    def post(self):
        try:
            data = request.get_json()
            
            return {"message":"Test erfolgreich"}, 200
        except Exception as e:
            return {"error:" f"{e} error orccurred"}, 500