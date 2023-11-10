from flask import Flask, jsonify
from flask_pymongo import PyMongo
import ping3
import psutil

app = Flask(__name__)

# Set your MongoDB URL
app.config['MONGO_URI'] = 'YOUR_URL'
mongo = PyMongo(app)

# Endpoint to get the latency of the Flask server
@app.route('/getlatency', methods=['GET'])
def get_latency():
    ping = ping3.Ping()
    latency = ping.ping('google.com')

    if latency is not None:
        return jsonify({'latency': latency})
    else:
        return jsonify({'error': 'Failed to determine latency'})


# Endpoint to get the current size of the Raspberry Pi device
@app.route('/getsizestatus', methods=['GET'])
def get_size_status():
    total_size, used_size, free_size = shutil.disk_usage("/")
    return jsonify({'total_size': total_size, 'used_size': used_size, 'free_size': free_size})

# Endpoint to get the RAM status of the device
@app.route('/getramstatus', methods=['GET'])
def get_ram_status():
    ram_info = psutil.virtual_memory()
    return jsonify({'total_ram': ram_info.total, 'used_ram': ram_info.used, 'free_ram': ram_info.available})


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
