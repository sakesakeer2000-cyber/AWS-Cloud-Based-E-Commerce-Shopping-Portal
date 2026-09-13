import os
from flask import Flask,render_template,request,redirect,url_for,flash
from database.dynamodb import get_products
from database.mysql_db import init_db,create_user
app=Flask(__name__); app.secret_key=os.getenv("FLASK_SECRET_KEY","change-this-secret-key")
try: init_db()
except Exception as e: print("MySQL initialization skipped:",e)
@app.route("/")
def home(): return render_template("index.html")
@app.route("/products")
def products(): return render_template("products.html",products=get_products())
@app.route("/about")
def about(): return render_template("about.html")
@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="POST": flash("Thank you! Your message has been received.","success"); return redirect(url_for("contact"))
    return render_template("contact.html")
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        n=request.form.get("name","").strip(); e=request.form.get("email","").strip(); p=request.form.get("password","")
        if not n or not e or not p: flash("Please complete all fields.","error"); return redirect(url_for("register"))
        try: create_user(n,e,p); flash("Account created successfully.","success")
        except Exception as x: flash(f"Registration failed: {x}","error")
        return redirect(url_for("register"))
    return render_template("register.html")
@app.get("/health")
def health(): return {"status":"healthy","application":"AWS Shopping Portal"},200
if __name__=="__main__": app.run(host="0.0.0.0",port=int(os.getenv("PORT","5000")))
