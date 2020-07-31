from flask import Flask, render_template, request
import requests
import json
import smtplib
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='551c5fa6a12d40b78a93259b3a488ed0')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/status")
def status():
    return render_template("status.html")

@app.route("/info1")
def info1():
    return render_template("info1.html")

@app.route("/info2")
def info2():
    return render_template("info2.html")

@app.route("/india")
def india():
    return render_template("india.html")

@app.route("/testingcentres")
def tc():
    return render_template("testingcentres.html")

@app.route("/helpline")
def help():
    return render_template("helpline.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    email = str(request.form.get("mail"))
    message = str(request.form.get("message"))
    sent_mes = str(email + "\n" + message)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("covidinfohub@gmail.com", "covid19sucks")
    server.sendmail("covidinfohub@gmail.com", "covidinfohub@gmail.com", sent_mes)

    return render_template("about.html", email=email, message=message, sent_mes=sent_mes)


@app.route("/news")
def news():
    khabar = newsapi.get_top_headlines(q='corona', language='en', country='in')
    articles = khabar['articles']

    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        


    mylist = zip(news, desc, img)

    return render_template("news.html", khabar=khabar, articles=articles, context=mylist)


if __name__ == "__main__":
    app.run(debug=True)