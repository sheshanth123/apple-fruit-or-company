import mysql.connector
import datetime
import os

def init_connection():
	mydb = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12290455",
    passwd="5Z8cZ1LqDz",
    database="sql12290455"
    )
	
	return mydb

def get_db_cursor(db_object):
	return db_object.cursor(buffered=True)
	
def insert_into_db(db_object, db_cursor, input_str, label_data):
	file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	f= open("./input_text/"+file_name,"w+")
	f.write(input_str)
	f.close()
	sql = "INSERT INTO input_text (input_text_id, label_data) VALUES (%s, %s)"
	val = (file_name , label_data)
	db_cursor.execute(sql, val)
	db_object.commit()
	
	
