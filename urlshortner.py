# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 22:02:07 2025

@author: Acer
"""

from flask import Flask, request, redirect, jsonify
import string
import random

app = Flask(__name__)

# In-memory storage for shortened URLs
url_mapping = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))
        if code not in url_mapping:
            return code

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    short_code = generate_short_code()
    url_mapping[short_code] = original_url

    short_url = request.host_url + short_code
    return jsonify({"short_url": short_url})

@app.route('/<short_code>')
def redirect_to_url(short_code):
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)
    else:
        return jsonify({"error": "Short URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
