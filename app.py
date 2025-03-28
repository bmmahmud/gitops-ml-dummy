from flask import Flask
app = Flask(__name__)

@app.route('/')
def predict():
    return "Predicted value: 42 (GitOps Version 1)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

     