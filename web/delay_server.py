from flask import Flask
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def default_response():
    time.sleep(10)  # 10초 지연
    return "Response after 10 seconds delay", 200
@app.route('/delay', methods=['GET'])
def delay_response():
    time.sleep(1)  # 10초 지연
    return "Response after 1 seconds delay", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)