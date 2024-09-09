# Obesity Detector Web Application

This project is a web-based tool for detecting obesity using input features such as age, gender, height, weight, and BMI. The application uses a machine learning model trained to predict obesity based on these features and provides predictions in real-time.

## Features
- Collects user inputs (age, gender, height, weight) to calculate BMI.
- Uses a pre-trained machine learning model to predict whether the user is obese or not.
- Provides an easy-to-use interface for non-technical users via **Streamlit**.
- Displays visualizations of the decision tree model.

## Technologies Used
- **Python**: The core programming language for the app.
- **Streamlit**: For building the web interface.
- **Scikit-learn**: For preprocessing (Label Encoding) and model prediction.
- **Pickle**: For loading the pre-trained model.
- **Matplotlib**: For visualizing the decision tree.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/DIXIT0043/Obesity-Detector.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the pre-trained model (`obesity_model.h5`) is available in the correct directory.

4. Run the Streamlit app:

    ```bash
    streamlit run dt_app.py
    ```

## Usage

1. **Age**: Use the slider to select the age (range: 10-112 years).
2. **Gender**: Select between Male or Female.
3. **Height**: Enter height in centimeters.
4. **Weight**: Enter weight in kilograms.
5. **BMI**: Automatically calculated based on the height and weight provided.
6. Click on the **Predict** button to get the prediction result.

The prediction output will display whether the input data indicates obesity or not. The decision tree used for the prediction is also visualized as an image.

## Model

The machine learning model used in this application is pre-trained and stored as a pickle file (`obesity_model.h5`). It uses decision trees to classify the input data as obese or not.

## Example

- **Input**: Age = 25, Gender = Male, Height = 175 cm, Weight = 70 kg
- **Output**: Prediction: Normal
