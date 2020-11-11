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

#Picture Endpoints

@app.route("/<profileid>/pictures", methods=["GET"])
def profile_pictures(profileid):
    #Return all pictures
    sql = f"SELECT * From pictures where username='{profileid}'"
    cursor.execute(sql)
    pictures = cursor.fetchall()
    return jsonify(pictures)
    
@app.route("/<profileid>/<pictureid>", methods=["GET"])
def picture_index(profileid,pictureid):
    #Return a picture
    sql = f"SELECT * From pictures where pictureID={pictureid}"
    cursor.execute(sql)
    pictures = cursor.fetchall()
    return jsonify(pictures)
    
@app.route("/<profileid>/", methods=["POST"])
def create_picture(profileid):
    #Post a picture
    sql = f"INSERT INTO pictures (title) VALUES (%s);"
    cursor.execute(sql, (request.json["title"],))
    connection.commit()
    
@app.route("/<profileid>/<pictureid>", methods=["DELETE"])
def delete_picture(profileid,pictureid):
    #Delete a picture
    sql = f"SELECT * From pictures where pictureID={pictureid}"
    cursor.execute(sql, (pictureid,))
    pictures = cursor.fetchone()
    
    if pictures:
        sql = f"DELETE FROM pictures where pictureid ={pictureid}"
        cursor.execute(sql, (pictureid,))
        connection.commit()
        
    return jsonify(pictures)

@app.route("/<profileid>/<pictureid>", methods=["PUT", "PATCH"])
def update_picture(profileid,pictureid):
    #Update a picture
    sql = f"UPDATE pictures SET keyword = %s WHERE pictureID={pictureid}"
    cursor.execute(sql, (request.json['keyword'], pictureid))
    pictures = cursor.fetchone()
    
    sql = "SELECT * FROM pictures WHERE pictureID={pictureid}"
    cursor.execute(sql, (pictureid,))
    pictures = cursor.fethone()
    return jsonify(pictures)
    









#Profile endpoints
@app.route("/<profileid>", methods=["GET"])
def profile_index(profileid):
    #Return a profile
    sql = f"SELECT * From profile where username='{profileid}'"
    cursor.execute(sql)
    profile = cursor.fetchall()
    return jsonify(profile)
    
@app.route("/", methods=["POST"])
def create_profile():
    #Create a profile
    sql = f"INSERT INTO profile (username) VALUES (%s);"
    cursor.execute(sql, (request.json["username"],))
    connection.commit()
    
@app.route("/<profileid>/", methods=["DELETE"])
def delete_profile(profileid):
    #Delete a profile
    sql = f"SELECT * From pictures where username={profileid}"
    cursor.execute(sql, (profileid,))
    profile = cursor.fetchone()
    
    if profile:
        sql = f"DELETE FROM profile where username ={profileid}"
        cursor.execute(sql, (profileid,))
        connection.commit()
        
    return jsonify(profile)

@app.route("/<profileid>", methods=["PUT", "PATCH"])
def update_profile(profileid):
    #Update a profile
    sql = f"UPDATE profile SET description = %s WHERE username={profileid}"
    cursor.execute(sql, (request.json['keyword'], profileid))
    profile = cursor.fetchone()
    
    sql = "SELECT * FROM profile WHERE username={profileid}"
    cursor.execute(sql, (profileid,))
    profile = cursor.fethone()
    return jsonify(profile)
    
# Keywords endpoint
@app.route("/<key>", methods=["GET"])
def keyword_pictures(key):
    #Return all pictures
    sql = f"SELECT * FROM pictures WHERE keyword='{key}';"
    cursor.execute(sql)
    pictures = cursor.fetchone()
    return jsonify(pictures)



QUESTIONS FOR BRUCE
*Create/Put resources
*Photos to a databse?
*Get request for keywords
*hows life?
*did you have to send out like 36 emails?


























# def add(a,b):
#     return (a+b)
    

