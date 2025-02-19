from flask import Flask, request, render_template
import numpy as np
import pickle
import os  # For fetching AWS Elastic Beanstalk PORT

# Initialize Flask app
application = Flask(__name__)

# Load the trained model
try:
    model = pickle.load(open("salary.pkl", "rb"))
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {str(e)}")

# Route for displaying the form
@application.route("/", methods=["GET"])
def index():
    """Render the form."""
    return render_template("index.html")

# Route for making predictions (Allow both GET and POST)
@application.route("/predict", methods=["GET", "POST"])
def predict():
    """Handle predictions."""
    prediction = None
    hours = None

    if request.method == "POST":
        try:
            hours = float(request.form["hours"])  # Get user input (study hours)

            # Convert input to NumPy array for prediction
            sample_input = np.array([[hours]])

            # Make prediction
            predicted_score = model.predict(sample_input)[0]
            prediction = round(predicted_score, 2)

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", hours=hours, prediction=prediction)

if __name__ == "__main__":
    application.run(host="0.0.0.0")
