from flask import Flask, request, jsonify
from flask import render_template
from db import db
from db import tables
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
def tabless():
    tables_names = tables.get_tables_names()
    return render_template('tables.html', tables = tables_names)

@app.route('/table')
def table():
    table_name = unquote(request.args.get('name'))
    columns, table_data = tables.get_table(table_name)
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
    (pa_data, lodger_columns, lodger_data, fl_srvs_columns, fl_srvs_data, accarc_columns, accarc_data,
    communics_columns, communics_data, pa_c_columns, pa_c_data,f_c_columns, f_c_data) = db.personal_ac_obj(id)
    # a_columns, accarc_data = db.personal_ac_accarc(id)
    return render_template('personal_ac.html', id = id, pa_data=pa_data,
                          lodger_data=lodger_data, lodger_columns=lodger_columns,
                          fl_srvs_columns = fl_srvs_columns, fl_srvs_data = fl_srvs_data,
                          accarc_columns = accarc_columns, accarc_data = accarc_data,
                          communics_columns = communics_columns, communics_data = communics_data,
                          pa_c_columns = pa_c_columns, pa_c_data = pa_c_data,
                          f_c_columns = f_c_columns, f_c_data = f_c_data)


@app.route('/api/meter-readings/<counter_id>')
def get_meter_readings(counter_id):
    try:
        # Получаем данные из БД
        columns, data = db.сounter_readings(counter_id)

        # Возвращаем данные в формате JSON
        return jsonify({
            'success': True,
            'columns': columns,
            'data': data  # data уже в правильном формате (список кортежей)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e) + "rrrrrrrrrrr"
        }), 500