# Automatic Authentication by python flask application with selenium

from flask import Flask, render_template,request,redirect,url_for
from selenium import webdriver
app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="GET":
        return redirect(url_for("login"))
    else:
        return render_template("test.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        username = request.form.get("nm")
        password = request.form.get("pass")

        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("https://demo.testfire.net/login.jsp")
        driver.find_element_by_id("uid").send_keys(username)
        driver.find_element_by_id("passw").send_keys(password)
        driver.find_element_by_name("btnSubmit").click()

        return "Successfully Login Mr.Admin"
    else:
        return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)
