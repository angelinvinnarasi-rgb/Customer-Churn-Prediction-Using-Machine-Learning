from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

with open("models/gradient_boosting_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]

    return jsonify({"prediction": int(prediction)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")