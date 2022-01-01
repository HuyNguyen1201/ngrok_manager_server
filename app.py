import pickle
from flask import Flask, render_template, jsonify, request
from datetime import datetime
from processor import apingrok_process
import copy
import os

import processor

app = Flask(__name__)
counter_account = 0
ngrok_set = set()


@app.route("/", methods=['GET'])
def index():
    result = apingrok_process.show_apingrok()
    return jsonify(result)


@app.route("/api/get-ngrokapi", methods=['GET'])
def get_account():
    result = apingrok_process.get_apingrok()
    return jsonify(result)


@app.route("/api/add-ngrokapi", methods=['POST'])
def predict():
    global counter_account
    if request.json:
        # predict image
        result = apingrok_process.save_apingrok(
            request.json)
        print('Success!')
        return jsonify({'result': 'success'})
    print('Fail!')
    return jsonify({'result': 'fail'})


@app.route("/api/release-all-ngrokapi", methods=['GET'])
def release_all_ngrok():
    apingrok_process.release_all_apingrok()
    return jsonify({'status': 'sucess'})


@app.route("/api/release-ngrokapis", methods=['POST'])
def release_ngroks():
    if request.json:
        apingrok_process.release_ngroks(request.json)
        return jsonify({'status': 'sucess'})
    return jsonify({'status': 'fail'})


@app.route("/api/delete-all-ngrokapi", methods=['GET'])
def release_all_ngrok():
    apingrok_process.delete_all_ngrok()
    return jsonify({'status': 'sucess'})


@app.route("/api/delete-ngrokapis", methods=['POST'])
def release_ngroks():
    if request.json:
        apingrok_process.delete_ngroks(request.json)
        return jsonify({'status': 'sucess'})
    return jsonify({'status': 'fail'})


@app.route("/shutdown", methods=['GET'])
def shutdown():
    '''Shutdown the server'''
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func is None:
        raise RuntimeError('Not running werkzeug')
    shutdown_func()
    return "Shutting down..."


if __name__ == "__main__":
    # make apikey set
    if os.path.exists('ngrok_dict.pkl') == False:
        with open('ngrok_dict.pkl', 'wb') as f:
            pickle.dump(dict(), f)
    # run flask
    app.run(debug=False)
