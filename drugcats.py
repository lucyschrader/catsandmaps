from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, Markup
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
from classes import Cat
import os, json

application = app = Flask('drugcats')
GoogleMaps(app)

carina = Cat(name='Carina', ap=5, money = 500, level = 1)
actions = {'scout': 1, 'deal': 1}

@app.route('/')
def home(): 
    nelson_map = Map(
        identifier = 'view-side',
        lat = -41.2693331,
        lng = 173.2824662,
        markers = [],
        zoom = 16,
        style = 'width: 100%; height: 400px;')
    return render_template('home.html',
        nelson_map = nelson_map,
        carina = carina,
        actions = actions)

@app.route('/select')
def select_cat():
    return render_template('select.html')

@app.route('/actions/<do>')
def use_action(do):
    carina.do()
    return redirect(url_for('home'))

#def take_turn(ap):
#    while ap > 0:

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0')