from flask import Flask, request
from flask_restx import Api, Namespace, Resource


server = Flask(__name__)

api = Api(server, version="0.0.1", title = "Welcome to Fox Finance Api")

from .information import information_ns
from .create_customer_accout import create_customer_account_ns
from .authentication import login_user_ns


api.add_namespace(information_ns, path="/info")
api.add_namespace(create_customer_account_ns, path="/create_customer_account")
api.add_namespace(login_user_ns, path="/login_user")