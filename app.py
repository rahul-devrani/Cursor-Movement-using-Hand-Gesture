import streamlit as st
import subprocess

st.title("Cursor Movement Using Hand Gesture")
st.write("Control your cursor with hand gestures!")

# Buttons to start/stop the gesture detection program
import requests

if st.button("Start Gesture Control"):
    try:
        response = requests.get("http://localhost:5000/start")  # Replace with your local server URL
        if response.status_code == 200:
            st.success("Gesture Control started!")
        else:
            st.error("Failed to start Gesture Control.")
    except Exception as e:
        st.error(f"Error: {e}")


if st.button("Stop Gesture Detection"):
    try:
        # Stop all processes running `main.py` (Linux example, adjust for Windows if needed)
        subprocess.Popen(["pkill", "-f", "main.py"])
        st.success("Gesture detection stopped!")
    except Exception as e:
        st.error(f"Error stopping program: {e}")
