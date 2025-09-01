


import numpy as np
from flask import Flask, request, render_template
import pickle

flask_app = Flask(__name__)

try:
    model = pickle.load(open("model.pkl", "rb"))
    print("Model loaded successfully:", type(model))
    test_features = np.array([[90, 42, 43, 20.8, 82.0, 6.5, 202.9]])
    print("Test prediction:", model.predict(test_features))
except Exception as e:
    print("Error loading model:", e)
    model = None

@flask_app.route("/")
def Home():
    return render_template("index.html", prediction_text="")  # Pass empty prediction_text

@flask_app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return render_template("index.html", prediction_text="Error: Model not loaded.")
    try:
        float_features = [float(x) for x in request.form.values()]
        print("Form inputs:", float_features)  # Debug
        features = [np.array(float_features)]
        prediction = model.predict(features)
        print("Prediction:", prediction)  # Debug
        return render_template("index.html", prediction_text="The Predicted Crop is {}".format(prediction[0]))
    except ValueError:
        return render_template("index.html", prediction_text="Error: Please enter valid numeric values.")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    flask_app.run(debug=True)