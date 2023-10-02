from flask import Flask, request, jsonify
from flask_cors import CORS
from bl.summerCamp import *

Lee = SummerCampBL()


def SummerCamp(prompt):
    response = Lee.promt_to_conversation(prompt)
    return response

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['Get']) 
def prompt():
    data = request.get_json()
    prompt = data.get('prompt')

    response = SummerCamp(prompt)


    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=False)
