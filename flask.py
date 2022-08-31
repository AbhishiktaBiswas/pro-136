from typing import final
from flask import Flask,jsonify,request
from data import data

app=Flask(__name__)

@app.route("/stars")
def index():
    return jsonify({
        "data":final_stars,
        "message":"sucess"
    }),200

@app.route("/")
def planet():
    name=request.args.get("name")
    final_stars=next(item for item in data if item["name"]==name)
    return jsonify({
        "data":final_stars,
        "message":"sucess"
    }),200

if __name__=="__main__":
    app.run(debug=True)