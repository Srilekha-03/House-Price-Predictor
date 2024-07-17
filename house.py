import streamlit as st
import pickle
import os

# Path to your model file
model_path = r"C:\Users\srile\Downloads\C__Users_srile_Downloads_HousePred_G.pkl"

# Debugging: Check if the file exists at the specified path
if not os.path.exists(model_path):
    st.write(f"File not found: {model_path}")
else:
    st.write(f"File found: {model_path}")

# Load the model
try:
    with open(model_path, "rb") as pickle_in:
        model = pickle.load(pickle_in)
    st.write("Model loaded successfully")
except Exception as e:
    st.write(f"Error loading model: {e}")

def predict_house_price(UNDER_CONSTRUCTION, RERA, BHK_NO, BHK_OR_RK, SQUARE_FT, READY_TO_MOVE, RESALE, LONGITUDE, LATITUDE):
    try:
        # Convert input to float for the model
        prediction = model.predict([[float(UNDER_CONSTRUCTION), float(RERA), float(BHK_NO), float(BHK_OR_RK), float(SQUARE_FT), float(READY_TO_MOVE), float(RESALE), float(LONGITUDE), float(LATITUDE)]])
        return prediction[0]
    except Exception as e:
        st.write(f"Error during prediction: {e}")
        return None

def main():
    st.title("House Price Prediction Model")
    html_temp = """
    <div style="background-color:tomato;padding:12px">
    <h2 style="color:white;text-align:center;">House Price Predictor</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Input fields for user input
    UNDER_CONSTRUCTION = st.radio("Is the house under construction?", ("No", "Yes"))
    UNDER_CONSTRUCTION = 1 if UNDER_CONSTRUCTION == "Yes" else 0
    
    RERA = st.radio("Is the house RERA registered?", ("No", "Yes"))
    RERA = 1 if RERA == "Yes" else 0
    
    BHK_NO = st.number_input("Number of BHKs", min_value=0, format='%d')
    
    BHK_OR_RK = st.radio("Is it a BHK or an RK?", ("BHK", "RK"))
    BHK_OR_RK = 1 if BHK_OR_RK == "RK" else 0
    
    SQUARE_FT = st.number_input("Area in square feet", min_value=0.0, format='%f')
    
    READY_TO_MOVE = st.radio("Is the house ready to move?", ("No", "Yes"))
    READY_TO_MOVE = 1 if READY_TO_MOVE == "Yes" else 0
    
    RESALE = st.radio("Is the house for resale?", ("No", "Yes"))
    RESALE = 1 if RESALE == "Yes" else 0
    
    LONGITUDE = st.number_input("Longitude", format='%f')
    LATITUDE = st.number_input("Latitude", format='%f')

    result = ""
    if st.button("Predict"):
        result = predict_house_price(UNDER_CONSTRUCTION, RERA, BHK_NO, BHK_OR_RK, SQUARE_FT, READY_TO_MOVE, RESALE, LONGITUDE, LATITUDE)
        if result is not None:
            st.success(f'The predicted house price is {result:.2f} Lacs')

if __name__ == '__main__':
    main()




