from flask import Flask, request, jsonify

app = Flask(__name__)

# GET request
@app.route("/get-user/<int:user_id>")
def get_user(user_id):
    user_data ={
        "user_id": user_id,
        "name": "John Doe",
        "email": "johndoe@example.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    #this will return user_data in json format and the 200 is the status code
    return jsonify(user_data), 200

# POST request
@app.route("/create_user", method=["POST"])
def create_user():
    data = request.get_json()

    # this will post a users data in a json format and the 201 is a status code
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
