from flask import Flask
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['url_shortner']
urls_collection = db['urls']

test_client = MongoClient('mongodb://localhost:27017/')
test_db = test_client['url_shortner_test']
test_urls_collection = test_db['test_urls']

app = Flask(__name__)

@app.route('/')
def home():
    return "url shortner api is running"

@app.route('/test-db')
def test_db():
    urls_collection.insert_one({"test":"success"})
    return "inserted test document in production db"

@app.route('/test-db-test')
def test_db_test():
    test_urls_collection.insert_one({"test" : "test success"})
    return "inserted test document is in test db"

    
    

if __name__ == '__main__':
    app.run(debug=True)
    
    