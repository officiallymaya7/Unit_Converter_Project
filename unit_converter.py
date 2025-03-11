import streamlit as st

# Custom CSS for styling
theme = """
<style>
    body {
        background-color: #f4f4f4;
    }
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 20px;
        border-radius: 10px;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        cursor: pointer !important;
    }
    .stButton button {
        background-color: #ff6600 !important;
        color: white !important;
        border-radius: 10px;
        padding: 10px;
        transition: all 0.3s ease-in-out;
        border: none;
        outline: none;
    }
    .stButton button:hover {
        background-color: white !important;
        color: black !important;
    }
    .stButton button:active {
        background-color: #ff6600 !important;
        color: white !important;
    }
    .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: white !important;
    }
    .footer-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    /* Sidebar Text */
    section[data-testid="stSidebar"] * {
        color: black !important;
    }
    /* Styling success message */
    div.stAlert {
        background-color: white !important;
        color: green !important;
        border-left: none !important;
    }
    /* Make the deploy button black */
header [data-testid="stToolbar"] button {
    background-color: black !important;
    color: white !important;
    border-radius: 5px;
}

/* Make the 3-dots menu black */
header [data-testid="stToolbar"] button[kind="icon"] svg {
    fill: black !important;
}
</style>
"""

st.markdown(theme, unsafe_allow_html=True)

def length_converter(value, from_unit, to_unit):
    conversions = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084
    }
    return value * conversions[to_unit] / conversions[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversions = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    return value * conversions[to_unit] / conversions[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

st.title("📱Unit Converter🌟")

option = st.sidebar.selectbox("Choose conversion type:", ["Length", "Weight", "Temperature"], key="option")

value = st.number_input("Enter value:", key="value")

if option == "Length":
    from_unit = st.selectbox("From:", ["meters", "kilometers", "miles", "feet"], key="from_length")
    to_unit = st.selectbox("To:", ["meters", "kilometers", "miles", "feet"], key="to_length")
    if st.button("Convert", help="Click to convert", key="convert_length"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"Converted Value: {result} {to_unit}")

elif option == "Weight":
    from_unit = st.selectbox("From:", ["grams", "kilograms", "pounds", "ounces"], key="from_weight")
    to_unit = st.selectbox("To:", ["grams", "kilograms", "pounds", "ounces"], key="to_weight")
    if st.button("Convert", help="Click to convert", key="convert_weight"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"Converted Value: {result} {to_unit}")

elif option == "Temperature":
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit"], key="from_temp")
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit"], key="to_temp")
    if st.button("Convert", help="Click to convert", key="convert_temp"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"Converted Value: {result} {to_unit}")

# Footer
st.markdown("---")
st.markdown('<div class="footer-box">Made with ❤️ by Maya Khurshid Anwar</div>', unsafe_allow_html=True)
