import streamlit as st
import subprocess

# Global variable to store the process
process = None

# Streamlit layout
st.title("🎮 Hand Gesture Cursor Control 🎮")
st.markdown("### Control your cursor using hand gestures")

# Start Gesture Control
if st.button("Start Gesture Control"):
    try:
        process = subprocess.Popen(["python", "main.py"])
        st.success("Hand Gesture Cursor Control started!")
    except Exception as e:
        st.error(f"Error starting gesture control: {e}")

# Stop Gesture Control
if st.button("Stop Gesture Control"):
    try:
        if process:
            process.terminate()
            process.wait()
            process = None
            st.success("Hand Gesture Cursor Control stopped!")
        else:
            st.warning("No process is running!")
    except Exception as e:
        st.error(f"Error stopping gesture control: {e}")

st.markdown("**Designed by Rahul**")
