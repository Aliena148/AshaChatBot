from flask import Flask, render_template, request, jsonify
from retriever import data_retriever
import pandas as pd

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('query', '').lower()
    session_data = data.get('session_data', {'last_query': '', 'last_response': []})

    if not query:
        return jsonify({"job_title": "No results found", "category": "", "location": ""})

    results = data_retriever.search(query, session_data)
    session_data['last_query'] = query
    session_data['last_response'] = results

    # Check if results contain a valid job title (not "No results found")
    if results.get('job_title') != "No results found":
        print(f"Server started: {results['job_title']}")

    return jsonify(results)

if __name__== '__main__':
    app.run(debug=True)