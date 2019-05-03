#!/usr/bin/env python3

from flask import Flask, render_template, request, Response
from config import mongo_db
from bson.json_util import dumps


app = Flask(__name__)

@app.route("/post", methods=["POST"])
def insertUser():
	try:
		user = request.get_json()
		mongo_db.user.insert_one(
			{
				"name": user["name"],
				"email": user["email"]
			}
		)
		response = {"message": "Usuário '%s' criado com sucesso!"%(user["name"])}
		return Response(dumps(response), status=201, content_type="application/json")
	except Exception as e:
		return "Erro %s"%(e)


@app.route("/get", methods=["GET"])
def getUser():
    try:
       	users = mongo_db.user.find()
        return Response(dumps(users), status=200, content_type="application/json")
    except Exception as e:
        return "Erro %s"%(e)

if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')
