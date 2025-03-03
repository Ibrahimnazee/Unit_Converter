import streamlit as st
import streamlit.components.v1 as components

def length_converter(value, choice):
    conversions = {
        "Kilometers to Miles": value * 0.621371,
        "Miles to Kilometers": value * 1.60934,
        "Inches to Centimeters": value * 2.54,
        "Centimeters to Inches": value / 2.54,
        "Feet to Meters": value * 0.3048,
        "Meters to Feet": value / 0.3048,
        "Inches to Feet": value / 12,
        "Feet to Inches": value * 12
    }
    return f"{value} {choice.split()[0]} is {conversions[choice]:.2f} {choice.split()[-1]}"

def weight_converter(value, choice):
    conversions = {
        "Kilograms to Pounds": value * 2.20462,
        "Pounds to Kilograms": value * 0.453592
    }
    return f"{value} {choice.split()[0]} is {conversions[choice]:.2f} {choice.split()[-1]}"

def temperature_converter(value, choice):
    conversions = {
        "Celsius to Fahrenheit": (value * 9/5) + 32,
        "Fahrenheit to Celsius": (value - 32) * 5/9
    }
    return f"{value}°{choice[0]} is {conversions[choice]:.2f}°{choice[-1]}"

def time_converter(value, choice):
    conversions = {
        "Minutes to Hours": value / 60,
        "Hours to Minutes": value * 60
    }
    return f"{value} {choice.split()[0]} is {conversions[choice]:.2f} {choice.split()[-1]}"

def speed_converter(value, choice):
    conversions = {
        "Kilometers per hour to Miles per hour": value * 0.621371,
        "Miles per hour to Kilometers per hour": value * 1.60934
    }
    return f"{value} {choice.split()[0]} is {conversions[choice]:.2f} {choice.split()[-2]} {choice.split()[-1]}"

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="⚖️", layout="wide")
    theme = st.sidebar.radio("Select Theme", ["Dark", "Light"])
    
    if theme == "Dark":
        st.markdown("""
            <style>
                .stApp {background-color: #1e1e1e; color: white;}
                .stTitle {color: white; text-align: center; font-size: 2.5rem;}
                .stSidebar {background-color: #a5c9c3; padding: 15px; border-radius: 10px; color: black;}
                .stButton > button {background-color: #f39c12; color: black; border-radius: 8px; font-size: 1.2rem;}
                .stRadio label {color: black !important;}
                .stNumberInput label {color: white;}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .stApp {background-color: #ffffff; color: black;}
                .stTitle {color: black; text-align: center; font-size: 2.5rem;}
                .stSidebar {background-color: #f5f5f5; padding: 15px; border-radius: 10px; color: black;}
                .stButton > button {background-color: #007bff; color: white; border-radius: 8px; font-size: 1.2rem;}
                .stRadio label {color: black !important;}
                .stNumberInput label {color: black;}
            </style>
        """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='stTitle'>🌍 Universal Unit Converter</h1>", unsafe_allow_html=True)
    st.markdown("### Convert Length, Weight, Temperature, Time, and Speed effortlessly!", unsafe_allow_html=True)
    
    st.sidebar.header("🔀 Conversion Options")
    option = st.sidebar.selectbox("Choose Conversion Type", 
                                  ["Length Converter", "Weight Converter", "Temperature Converter", "Time Converter", "Speed Converter"])
    
    conversions = {
        "Length Converter": ["Kilometers to Miles", "Miles to Kilometers", "Inches to Centimeters", "Centimeters to Inches", "Feet to Meters", "Meters to Feet", "Inches to Feet", "Feet to Inches"],
        "Weight Converter": ["Kilograms to Pounds", "Pounds to Kilograms"],
        "Temperature Converter": ["Celsius to Fahrenheit", "Fahrenheit to Celsius"],
        "Time Converter": ["Minutes to Hours", "Hours to Minutes"],
        "Speed Converter": ["Kilometers per hour to Miles per hour", "Miles per hour to Kilometers per hour"]
    }
    
    choice = st.sidebar.radio("Select Conversion", conversions[option])
    
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    with col2:
        if st.button("Convert", use_container_width=True):
            if option == "Length Converter":
                result = length_converter(value, choice)
            elif option == "Weight Converter":
                result = weight_converter(value, choice)
            elif option == "Temperature Converter":
                result = temperature_converter(value, choice)
            elif option == "Time Converter":
                result = time_converter(value, choice)
            elif option == "Speed Converter":
                result = speed_converter(value, choice)
            
            st.success(result)
            st.balloons()
    
    st.markdown("<h3 style='text-align: center; color: white;'>Made by Ibrahim Nazeer</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
