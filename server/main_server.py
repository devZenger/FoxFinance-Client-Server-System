from flask import Flask, request
from flask_restx import Resource, Api

from api import server

if __name__ == "__main__":
    server.run(debug=True)