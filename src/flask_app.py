from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Set your MongoDB URL
app.config['MONGO_URI'] = 'YOUR_URL'
mongo = PyMongo(app)

@app.route('/getData', methods=['GET'])
def get_data():
    try:
        # Replace 'previous' with your actual collection name
        posts = mongo.db.previous.find({})
        data = []
        for post in posts:
            data.append({
                'timestamp': post['timestamp'],
                'link': post['link']
            })
        return jsonify({'data': data})
    except Exception as e:
        print(str(e))
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(port=3000)
