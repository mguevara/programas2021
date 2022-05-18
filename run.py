# -*- coding: utf-8 -*-
from random import choice, shuffle
from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

cand = {"artes", "boric", "kast", "me-o", "parisi","provoste", "sichel"}
def otros(candidato):
    k = list(cand-{candidato})
    shuffle(k)
    k = map(str.upper, k)
    return k
candidatos = {
    "artes": {
        "nombre": u'Eduardo Artés',
        "nick": u"Artés",
        "dw":"https://datawrapper.dwcdn.net/yoYs8", 
        "tf":"9j2fxfu87ffr",
        "tflink":"https://wordart.com/9j2fxfu87ffr/programa-eduardo%20art%C3%A9s%202021",
        "tfidf":"c451k5l2gfke",
        "tfidflink":"https://wordart.com/c451k5l2gfke/programa-eduardo%20art%C3%A9s%202021%20contraste", 
        },
    "boric": {
        "nombre": u'Gabriel Boric',
        "nick": u"Boric",
        "dw":"https://datawrapper.dwcdn.net/Q9RVs/2/", 
        "tf":"ce5yc9fzp0j1",
        "tflink":"https://wordart.com/ce5yc9fzp0j1/programa-gabriel%20boric%202021",
        "tfidf":"1xdkshcomogd",
        "tfidflink":"https://wordart.com/1xdkshcomogd/programa-gabriel%20boric%202021%20contraste", 
        },
    "kast": {
        "nombre": u'José Antonio Kast',
        "nick": u"Kast",
        "dw":"https://datawrapper.dwcdn.net/zaN5q", 
        "tf":"4lnnk4snlr8l",
        "tflink":"https://wordart.com/4lnnk4snlr8l/programa-jos%C3%A9%20antonio%20kast%202021",
        "tfidf":"9i43z9m7mjd5",
        "tfidflink":"https://wordart.com/9i43z9m7mjd5/programa-jos%C3%A9%20antonio%20kast%202021%20contraste", 
        },
    "me-o": {
        "nombre": u'Marco Enríquez-Ominami',
        "nick": u"ME-O",
        "dw":"https://datawrapper.dwcdn.net/IQrdN", 
        "tf":"5ejwxmwlfoyo",
        "tflink":"https://wordart.com/5ejwxmwlfoyo/programa-marco%20enriquez-ominami%202021",
        "tfidf":"001xal7naec5",
        "tfidflink":"https://wordart.com/001xal7naec5/programa-marco%20enriquez-ominami%202021%20contraste", 
        },
    "parisi": {
        "nombre": u'Franco Parisi',
        "nick": u"Parisi",
        "dw":"https://datawrapper.dwcdn.net/axFk2", 
        "tf":"rgdmv97owu22",
        "tflink":"https://wordart.com/rgdmv97owu22/programa-franco%20parisi%202021",
        "tfidf":"3n4zf57nl796",
        "tfidflink":"https://wordart.com/3n4zf57nl796/programa-franco%20parisi%202021%20contraste", 
        },
    "provoste": {
        "nombre": u'Yasna Provoste Campillay',
        "nick": u"Provoste",
        "dw":"https://datawrapper.dwcdn.net/lTjqd", 
        "tf":"o7ly9y2gk6e9",
        "tflink":"https://wordart.com/o7ly9y2gk6e9/programa-yasna%20provoste%202021",
        "tfidf":"t2br907ye4so",
        "tfidflink":"https://wordart.com/t2br907ye4so/programa-yasna%20provoste%202021%20contraste", 
        },
    "sichel": {
        "nombre": u'Sebastián Sichel',
        "nick": u"Sichel",
        "dw":"https://datawrapper.dwcdn.net/zeYoR/1/", 
        "tf":"t9og7wo1rvv2",
        "tflink":"https://wordart.com/t9og7wo1rvv2/programa-sebasti%C3%A1n%20sichel%202021",
        "tfidf":"plxiazj9dzpt",
        "tfidflink":"https://wordart.com/plxiazj9dzpt/programa-sebasti%C3%A1n%20sichel%202021%20contraste", 
        }
    
    
    }

@app.route("/")
def index():
    c = choice(list(candidatos))
    candidatos[c]["otros"] = otros(c)
    return render_template("index.html", candidato=candidatos[c])

@app.route("/<string:slug>/")
def show_candidate(slug):
    if slug== "about":
        return render_template("about.html", candidatos=map(str.upper,cand))
    else:
        candidatos[slug.lower()]["otros"] = otros(slug.lower())
        return render_template("index.html", candidato=candidatos[slug.lower()])

#def hello_world():
#    return "Hello, World"
