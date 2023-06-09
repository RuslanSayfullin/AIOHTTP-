from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/get_user')
def get_user():
    user = {
            "name": "John",
            "age": 25,
            "email": "john@example.com"
            }
    return jsonify(user)

if __name__ == "__main__":
    app.run()
