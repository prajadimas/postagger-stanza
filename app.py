import flask
from flask import request, jsonify
from modules.postag import postag

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Part-of-Speech Tagger</h1>
<p>An API for Stanza Part-of-Speech Tagger Indonesian Language.</p>
<p>Check on /api/postag?s={sentence}</p>'''

@app.route('/api/postag', methods=['GET'])
def res_postag():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 's' in request.args:
        s = request.args['s']
    else:
        return "Error: No sentence field provided. Please specify a sentence with s query."

    # Create result list based on postag
    results = postag(s)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

# app.run()
