from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flasl_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)


app.config['MYSQL_USER'] = 'root1'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_tasks'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

CORS(app)


@app.route('/trips', methods=['GET'])
def getAllTrips():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks")
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/trips', methods=['POST'])
def addTrip():
    cur = mysql.connection.cursor()
    title = request.get_json()['title']
    cur.execute("INSERT INTO tasks (title) VALUES ('" + str(title) + "')")
    mysql.connection.commit()
    result = {'title' : title}

    return jsonify({'result' : result})

@app.route('/trip/<id>', methods=['PUT'])
def updateTrip(id):
    cur = mysql.connection.cursor()
    title = request.get_json()['title']
    cur.execute("UPDATE tasks SET title = '" + str(title) + "' WHERE id = " + id)
    mysql.connection.commit()
    result = {'title' : title}

    return jsonify({'result' : result})

@app.route('/trip/<id>', methods=['DELETE'])
def deleteTrip(id):
    cur = mysql.connection.cursor()
    response = cur.execute("DELETE FROM trips where id = " + id)
    mysql.connection.commit()

    if response > 0:
        result = {'message': 'record delete'}
    else:
        result = {'message': 'no record found'}

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
