from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load("iris_model.pkl")

# ✅ Add this home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Inference API is running. Use the /predict endpoint to send data."})

# Existing predict route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data["features"]
    prediction = model.predict([features])
    return jsonify({"prediction": prediction.tolist()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)