import pickle
from datetime import datetime
import os


def show_apingrok():
    with open('ngrok_dict.pkl', 'rb') as f:
        ngrok_dict = pickle.load(f)
    return ngrok_dict


def save_apingrok(data):
    with open('ngrok_dict.pkl', 'rb') as f:
        ngrok_dict = pickle.load(f)
    ngrok_dict[data['apikey']] = False
    with open('ngrok_dict.pkl', 'wb') as f:
        pickle.dump(ngrok_dict, f)


def get_apingrok():
    with open('ngrok_dict.pkl', 'rb') as f:
        ngrok_dict = pickle.load(f)
    apikey = -1
    for k, v in ngrok_dict.items():
        if v == False:
            apikey = k
    if apikey == -1:
        return False
    else:
        ngrok_dict[apikey] = True
    with open('ngrok_dict.pkl', 'wb') as f:
        pickle.dump(ngrok_dict, f)
    return apikey


def release_all_apingrok():
    with open('ngrok_dict.pkl', 'rb') as f:
        ngrok_dict = pickle.load(f)
    for k, v in ngrok_dict.items():
        ngrok_dict[k] = False
    with open('ngrok_dict.pkl', 'wb') as f:
        pickle.dump(ngrok_dict, f)


def release_ngroks(data):
    with open('ngrok_dict.pkl', 'rb') as f:
        ngrok_dict = pickle.load(f)
    ngrok_dict[data['apikey']] = False
    with open('ngrok_dict.pkl', 'wb') as f:
        pickle.dump(ngrok_dict, f)


def delete_all_ngrok():
    with open('ngrok_dict.pkl', 'wb') as f:
        pickle.dump(dict(), f)
    return True


def delete_ngroks(data):
    apikey = data['apikey']
    with open('ngrok_dict.pkl', 'rb') as f:
        ngrok_dict = pickle.load(f)
    if apikey in ngrok_dict.keys():
        del ngrok_dict[apikey]
        with open('ngrok_dict.pkl', 'wb') as f:
            pickle.dump(ngrok_dict, f)
        return True
    return False
