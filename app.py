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
            "$set": {'Name': record['sname'], 'Grade': record['sgrade']}
        }
    )
    print('inside database_update_entry', key_val, record)
    return status

@app.route('/')
def index():
    return render_template('index.html')

# just for testing
@app.route('/details')
def details():
    all_results = {}
    all_results['741'] = ['test name', '20']
    return render_template('details.html', dict = all_results)

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

    ########################
    new_results = {}
    for document in db.storage.find():
        print(document['Number'])
        new_results[document['Number']] = [document['Name'], document['Grade']]
    print(new_results)
    ########################
    return render_template('details.html', dict = new_results)

@app.route('/update', methods=['POST'])
def update_data():
    result = request.form
    student_number = result['snumber']
    student_name = result['sname']
    student_grade = result['sgrade']

    print(student_number)
    print(student_name)
    print(student_grade)

    db_update_record('Number', result)

    all_results = {}
    for document in db.storage.find():
        print(document['Number'])
        all_results[document['Number']] = [document['Name'], document['Grade']]
    print(all_results)
    ########################
    return render_template('details.html', dict = all_results)

@app.route('/edit/<string:q>')
def edit_data(q):
    print(q)
    Queryresult = storage.find_one({"Number": q})
    print(Queryresult)
    current_results = {}
    current_results[Queryresult['Number']] = [Queryresult['Name'], Queryresult['Grade']]
    return render_template('edit.html', dict = current_results)

if __name__ == '__main__':
    app.run(debug = True)