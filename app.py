from flask import Flask, render_template, redirect, url_for, flash, request
from datetime import datetime
from forms import ItemForm
from models import Items
from db import db
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = 'secret key no one know'
db_filename = 'test.db'
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# create database if not yet exists
if not os.path.exists(f'./instance/{db_filename}'):
        # os.remove(f'./instance/{db_filename}')
        with app.app_context():
            db.create_all()

# Routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/items', methods=['GET', 'POST'])
def items():
    items = Items.query.all()
    items_date = Items.query.with_entities(Items.received_date).all()
    days_since = [(datetime.now().date()-date[0]).days for date in items_date]
    add_form = ItemForm(csrf_enabled=False)
    if add_form.validate_on_submit():
        item_data = Items(name=add_form.name.data, received_date=add_form.received_date.data,
                          is_defect=add_form.is_defect.data, description=add_form.description.data)
        db.session.add(item_data)
        try:
            db.session.commit()
            flash("Item added succesfully")
        except:
            flash('Item already exists')
            db.session.rollback()
        return redirect(url_for('items'))
    return render_template("items.html", items_and_counts=zip(items, days_since), add_form=add_form)

@app.route('/delete/<int:item_id>', methods=['GET', 'POST'])
def delete(item_id):
    item = Items.query.get_or_404(item_id)
    db.session.delete(item)
    try:
        db.session.commit()
        flash('Item deleted succesfully')
    except:
        db.session.rollback()
    return redirect(url_for('items'))

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def update(item_id):
    item = Items.query.get_or_404(item_id)
    edit_form = ItemForm(obj=item ,csrf_enabled=False)
    if request.method == 'POST':
        item.name = edit_form.name.data
        item.received_date = edit_form.received_date.data
        item.is_defect = edit_form.is_defect.data
        item.description = edit_form.description.data
        try:
            db.session.commit()
            flash('Item updated succesfully')
            return redirect(url_for('items'))
        except:
            db.session.rollback()
    return render_template('edit_item.html', edit_form=edit_form, item=item)


if __name__ == '__main__':
    app.run(debug=True)