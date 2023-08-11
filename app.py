from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"payload": "welcome to my project"})

@app.route("/delete", methods=["DELETE"])
def delete():
    return jsonify ({"payload":"delete successfully"})

@app.route("/create", methods=["POST"])
def delete():
    return jsonify ({"payload":"create successfully"})
    
@app.route("/put", methods=["PUT"])
def delete():
    return jsonify ({"payload":"put successfully"})
    
@app.route("/init", methods=["GET"])
def delete():
    return jsonify ({"payload":"hack-1 finished"})
    
if __name__ == '__main__':
    app.run(debug=True)
