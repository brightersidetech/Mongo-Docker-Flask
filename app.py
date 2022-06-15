from flask import Flask, render_template, request
from pymongo import MongoClient
from pprint import pprint

app = Flask(__name__)

db_client = MongoClient('localhost', 27017)
db=db_client.details
storage = db.storage

data = {}

def db_store_record(result):
    global data
    #check_data('Fname', 'fname')
    db_check_record('Number', result['snumber'])

    data = {
        'Number': result['snumber'],
        'Name' : result['sname'],
        'Grade': result['sgrade'],
    }

    status = storage.insert_one(data)
    print(status.inserted_id)
    print(status)

def db_check_record(key, value):
    #Queryresult = storage.find({key: value})
    Queryresult = storage.find_one({key: value})
    print(Queryresult)


def db_update_record(key_val, record):
    status = storage.update_one(
        {key_val: record['snumber']},
        {
            "$set": {'grds': record}
        }
    )
    print('inside database_update_entry', key_val, record)
    return status

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def process_data():
    result = request.form
    student_number = result['snumber']
    student_name = result['sname']
    student_grade = result['sgrade']

    print(student_number)
    print(student_name)
    print(student_grade)

    # list of all collections in the database
    print(db.list_collection_names())
    db_store_record(result)
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update_data():
    result = request.form
    first_name = result['fname']
    last_name = result['lname']

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)