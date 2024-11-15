from flask import*
from pymongo import*
from bson.objectid import ObjectId
clinet = MongoClient("mongodb://localhost:27017")
database = clinet["Crude"]
collection = database["UserInfo"]
ID=0
app=Flask("__name__")
@app.route("/",methods=["POST","GET"])
def home():
    
    return render_template("home.html")
@app.route("/register",methods=["POST","GET"])
def register():
    global ID
    ID+=1
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        a=[{
            "_id":ObjectId() ,
            "username":username,
            "password":password
        }]
        if collection.find_one({"username":username}):
            print("Not Availble")

        else:
            collection.insert_many(a)
            
    return render_template("register.html")
@app.route("/login",methods=["POST","GET"])
def login():
    username=request.form.get("username")
    password=request.form.get("password")
    if collection.find_one({"username":username,"password":password}):
        return render_template("main.html")
    elif username and password=="admin":
        return redirect(url_for('admin'))
    else:
        print("nope")
    

    return render_template("login.html")
@app.route("/admin",methods=["POST","GET"])
def admin():
    return render_template("admin.html")
    
    




if __name__=="__main__":
    app.run()