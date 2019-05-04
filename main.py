from flask import Flask, render_template, request
from flask import jsonify
import classifytext
import db_operations

app = Flask(__name__, template_folder='template')
db_connection_object = db_operations.init_connection()
db_connection_cursor = db_operations.get_db_cursor(db_connection_object)

@app.route('/')
def index():
	return "test"

@app.route('/classify', methods=['POST', 'GET'])
def classify_text():
	input_str = request.form.get('inputText')
	label_str = classifytext.predict_text(input_str)
	db_operations.insert_into_db(db_connection_object, db_connection_cursor, input_str, label_str)
	return jsonify(responseStr = label_str)

if __name__ == '__main__':
	app.run()