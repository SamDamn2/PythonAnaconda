from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.tfrutha import Tfrutha
from app import db

bp = Blueprint('tfrutha', __name__)

@bp.route('/Tfruta')
def index():
    data = Tfrutha.query.all()
    # books_list = [book.to_dict() for book in data]
    # return jsonify(books_list)
    return render_template('tfruthas/index.html', data=data)

@bp.route('/Tfruta/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombret = request.form['nombret']
        
        new_tfrutha = Tfrutha(nombret=nombret)
        db.session.add(new_tfrutha)
        db.session.commit()
        
        return redirect(url_for('tfrutha.index'))

    return render_template('tfruthas/add.html')

@bp.route('/Tfruta/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    tfrutha = Tfrutha.query.get_or_404(id)

    if request.method == 'POST':
        tfrutha.nombret = request.form['nombret']
        db.session.commit()
        return redirect(url_for('tfrutha.index'))

    return render_template('tfruthas/edit.html', tfrutha=tfrutha)
    

@bp.route('/Tfruta/delete/<int:id>')
def delete(id):
    tfrutha = Tfrutha.query.get_or_404(id)
    
    db.session.delete(tfrutha)
    db.session.commit()

    return redirect(url_for('tfrutha.index'))