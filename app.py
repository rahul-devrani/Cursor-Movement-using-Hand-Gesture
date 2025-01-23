import streamlit as st
import subprocess

st.title("Cursor Movement Using Hand Gesture")
st.write("Control your cursor with hand gestures!")

# Buttons to start/stop the gesture detection program
if st.button("Start Gesture Detection"):
    try:
        # Launch the main program
        subprocess.Popen(["python", "main.py"])
        st.success("Gesture detection started! Use your webcam to control the cursor.")
    except Exception as e:
        st.error(f"Error starting program: {e}")

if st.button("Stop Gesture Detection"):
    try:
        # Stop all processes running `main.py` (Linux example, adjust for Windows if needed)
        subprocess.Popen(["pkill", "-f", "main.py"])
        st.success("Gesture detection stopped!")
    except Exception as e:
        st.error(f"Error stopping program: {e}")
