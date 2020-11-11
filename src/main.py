from flask import Flask, jsonify, request
app= Flask(__name__)
import psycopg2

connection = psycopg2.connect(
    database="instagramclone",
    user="ig",
    password="instagram",
    host="localhost",
    port=5432
    )
    
cursor = connection.cursor()

@app.route("/<profileid>/pictures", methods=["GET"])
def profile_pictures(profileid):
    #Return all pictures
    sql = f"SELECT * From pictures where username='{profileid}'"
    cursor.execute(sql)
    pictures = cursor.fetchall()
    return jsonify(pictures)
    
@app.route("/<profileid>/<pictureid>", methods=["GET"])
def picture_index(profileid,pictureid):
    #Return all pictures
    sql = f"SELECT * From pictures where pictureID={pictureid}"
    cursor.execute(sql)
    pictures = cursor.fetchall()
    return jsonify(pictures)





























# def add(a,b):
#     return (a+b)
    

