# GemValuate

## Diamond Price Prediction App

## Overview
The **Diamond Price Prediction App** is a Streamlit-based web application that allows users to predict the price of diamonds based on certain features like carat, color, and dimensions. Leveraging machine learning, this app provides accurate and insightful predictions for diamond prices.

## Features
- **User-friendly Interface:** Easy-to-use input fields for carat weight, color, and dimensions.
- **Real-Time Predictions:** Instant diamond price predictions at the click of a button.
- **Machine Learning Integration:** Powered by a trained regression model.

## How It Works
1. **Input Data:** Enter the following details about the diamond:
   - Carat weight (e.g., 2.5)
   - Color grade (D, E, F, G, H, I, J)
   - Y-dimension (length in mm)
2. **Prediction:** Click the **Predict** button to get the predicted price of the diamond.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd diamond-price-prediction-app
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App
Start the Streamlit app with the following command:
```bash
streamlit run app.py
```

## File Structure
- `app.py`: Main application file for the Streamlit app.
- `clr_le.pkl`: Pickle file for the LabelEncoder used to transform color values.
- `model.pkl`: Trained machine learning model for diamond price prediction.
- `requirements.txt`: List of required Python packages.

## Model Details
The app uses a machine learning regression model trained on diamond data to provide accurate predictions. The `LabelEncoder` is used to encode the categorical feature **color**.

## Usage Instructions
1. Launch the app by running the `streamlit` command.
2. Enter the diamond details.
3. Click **Predict** to get the diamond price.

## Example
| Input | Value |
|-------|-------|
| Carat | 2.5   |
| Color | G     |
| Y     | 5.00  |

**Prediction Output:**
```
The predicted price of the diamond is: $4,500
```

## Dependencies
- `streamlit`
- `pandas`
- `scikit-learn`
- `pickle`

## License
This project is licensed under the MIT License.

## Author
Adarsh-fg
Feel free to reach out for feedback or collaboration!

