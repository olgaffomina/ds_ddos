import joblib
import pandas as pd

from flask import Flask, jsonify, request

# Load the model
model = joblib.load("net_traffic_model.joblibdump")

# Init the app
app = Flask("default")


# Setup prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # Get the provided JSON
    X = request.get_json()
    # Perform a prediction
    preds = model.predict(pd.DataFrame(X, index=[0]))
    # Output json with prediction
    result = {"predict": int(preds[0])}
    return jsonify(result)


if __name__ == "__main__":
    # Run the app on local host and port 8989
    app.run(debug=True, host="0.0.0.0", port=8989)


