from flask import Flask, request
from flask import render_template
from db import db
from urllib.parse import unquote
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/about')
def about():
  return 'This is the about page'

@app.route('/user/<username>')
def show_user_profile(username):
  return f'User {username}'

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)


@app.route('/db')
def dbb():
    return db.hello_world()

@app.route('/tables')
def tables():
    tables_names = db.get_tables_names()
    return render_template('tables.html', tables = tables_names)

@app.route('/table')
def table():
    table_name = unquote(request.args.get('name'))
    columns, table_data = db.get_table(table_name)
    return render_template('table.html', table_name = table_name, columns = columns, table_data = table_data)

@app.route('/table_1')
def table_1():
  return render_template('table_1.html')

@app.route('/table_2')
def table_2():
  return render_template('table_2.html')

@app.route('/report')
def report():
  return render_template('report.html')

@app.route('/pa')
def pa():
  return render_template('pa_service.html')

@app.route('/personal_ac')
def personal_ac():
  id = unquote(request.args.get('id'))
  pa_data, lodger_columns, lodger_data = db.personal_ac_obj(id)
  # a_columns, accarc_data = db.personal_ac_accarc(id)
  return render_template('personal_ac.html', id = id, pa_data=pa_data,
                         lodger_data=lodger_data, lodger_columns=lodger_columns)