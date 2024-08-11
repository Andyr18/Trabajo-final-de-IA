from flask import render_template, request
from app import app
from app.models import Drug
from datetime import datetime

inventory = []

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

@app.route('/add_drug', methods=['POST'])
def add_drug():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    expiry_date = datetime.strptime(request.form['expiry_date'], '%Y-%m-%d').date()

    drug = Drug(name, quantity, expiry_date)
    inventory.append(drug)

    return render_template('index.html', inventory=inventory)
