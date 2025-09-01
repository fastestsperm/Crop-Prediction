<xaiArtifact artifact_id="cc7eb72b-efdf-43fa-8b84-a93171fc237b" artifact_version_id="aaff133b-e2b2-4d07-b87d-f069278dce37" title="README.md" contentType="text/markdown">

# Crop Prediction Web Application

## Overview
This is a Flask-based web application that uses a Random Forest Classifier to predict the most suitable crop based on soil and environmental factors. The model is trained on a dataset (`Crop_recommendation.csv`) containing features such as Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall. Users can input these parameters via a web interface, and the application returns the predicted crop.

## Features
- **User-Friendly Interface**: A clean HTML form to input soil and environmental parameters.
- **Machine Learning Model**: Utilizes a Random Forest Classifier for accurate crop predictions.
- **Real-Time Predictions**: Submits input data via a POST request and displays the predicted crop instantly.
- **Error Handling**: Validates user inputs and provides meaningful error messages for invalid data.

## Project Structure
```
crop_prediction/
├── app.py                  # Flask application script
├── model.py                # Script to train and save the ML model
├── model.pkl               # Trained Random Forest model
├── templates/
│   └── index.html          # HTML template for the web interface
├── static/
│   ├── style.css           # CSS file for styling the web interface
│   └── farm.jpg            # Background image for the web page
└── Crop_recommendation.csv # Dataset used for training the model
```

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A web browser (e.g., Chrome, Firefox)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd crop_prediction
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install flask pandas numpy scikit-learn
   ```

4. **Prepare the Dataset**:
   - Ensure `Crop_recommendation.csv` is in the project root directory.
   - The dataset should have columns: `N`, `P`, `K`, `temperature`, `humidity`, `ph`, `rainfall`, `label`.

5. **Train the Model**:
   - Run `model.py` to train the Random Forest Classifier and generate `model.pkl`:
     ```bash
     python model.py
     ```
   - This script loads the dataset, trains the model, and saves it as `model.pkl`.

6. **Run the Flask Application**:
   ```bash
   python app.py
   ```
   - The app will run on `http://localhost:5000` by default.
   - Open this URL in your browser to access the web interface.

## Usage
1. **Access the Web Interface**:
   - Navigate to `http://localhost:5000` in your browser.
   - You’ll see a form to input the following parameters:
     - Nitrogen (N)
     - Phosphorus (P)
     - Potassium (K)
     - Temperature (°C)
     - Humidity (%)
     - pH
     - Rainfall (mm)

2. **Submit Inputs**:
   - Enter numeric values for each parameter (e.g., `90, 42, 43, 20.8, 82.0, 6.5, 202.9`).
   - Click the **Predict** button to submit the form.

3. **View Prediction**:
   - The predicted crop (e.g., "The Predicted Crop is rice") will appear below the form.

## Example Input
For testing, try these sample values (based on typical crop recommendation datasets):
- Nitrogen: 90
- Phosphorus: 42
- Potassium: 43
- Temperature: 20.8
- Humidity: 82.0
- pH: 6.5
- Rainfall: 202.9

Expected output: A prediction like "The Predicted Crop is rice" (actual output depends on the dataset and model).

## Debugging Tips
- **Model Issues**:
  - Ensure `model.pkl` exists and was generated with the same scikit-learn version (`pip show scikit-learn`).
  - Verify the feature order in `Crop_recommendation.csv` matches the form inputs: `N, P, K, temperature, humidity, ph, rainfall`.
- **Form Issues**:
  - Check the Flask console for debug output (e.g., form inputs and predictions).
  - Ensure all form fields are filled with valid numeric values.
- **Template Issues**:
  - If the prediction doesn’t display, inspect the page source to confirm `<h1 id="predict">` contains the prediction.
  - Check `static/style.css` and `static/farm.jpg` are in place.

## Troubleshooting
- **TemplateNotFound Error**:
  - Ensure `index.html` is in the `templates` folder.
  - Restart the Flask server after moving files.
- **Prediction Not Displaying**:
  - Check the Flask console for errors or debug output.
  - Verify the model’s input expectations (run `python model.py` to print feature columns and test predictions).
- **Environment Issues**:
  - Ensure consistent Python and scikit-learn versions between training (`model.py`) and deployment (`app.py`).

## Future Improvements
- Add input validation for realistic ranges (e.g., pH between 0–14).
- Implement feature scaling if the model requires it (not needed for Random Forest).
- Enhance the UI with responsive design and better styling.
- Add a REST API endpoint for programmatic access to predictions.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with [Flask](https://flask.palletsprojects.com/), [scikit-learn](https://scikit-learn.org/), and [Pandas](https://pandas.pydata.org/).
- Inspired by crop recommendation datasets and machine learning tutorials.

</xaiArtifact>
