from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.fruta import Fruta
from app.models.tfrutha import Tfrutha
from app import db

bp = Blueprint('fruta', __name__)

@bp.route('/')
def index():
    data = Fruta.query.all()
    tdata = Tfrutha.query.all()
    # books_list = [book.to_dict() for book in data]
    # return jsonify(books_list)
    return render_template('frutas/index.html', data=data, tdata=tdata)
    #return data

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        color = request.form['color']
        tamaño = request.form['tamaño']
        tfrutha = request.form['tfrutha']
        
        new_fruta = Fruta(nombre=nombre, color=color, tamaño=tamaño, tfrutha=tfrutha)
        db.session.add(new_fruta)
        db.session.commit()
        
        return redirect(url_for('fruta.index'))
    data = Tfrutha.query.all()
    return render_template('frutas/add.html', data=data)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    fruta = Fruta.query.get_or_404(id)

    if request.method == 'POST':
        #return "entra al if"
        fruta.nombre = request.form['nombre']
        fruta.color = request.form['color']
        fruta.tamaño = request.form['tamaño']
        fruta.tfrutha = request.form['tfrutha']
        
        db.session.commit()
        
        return redirect(url_for('fruta.index'))

    return render_template('frutas/edit.html', fruta=fruta)

@bp.route('/delete/<int:id>')
def delete(id):
    fruta = Fruta.query.get_or_404(id)
    
    db.session.delete(fruta)
    db.session.commit()

    return redirect(url_for('fruta.index'))