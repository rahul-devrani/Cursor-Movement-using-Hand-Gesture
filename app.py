import streamlit as st
import os
import subprocess

st.title("Hand Gesture Cursor Control")

if st.button("Start Cursor Control"):
    try:
        subprocess.Popen(["python", "main.py"])
        st.success("Hand Gesture Cursor Control started!")
    except Exception as e:
        st.error(f"Error: {e}")

if st.button("Stop Cursor Control"):
    try:
        subprocess.Popen(["pkill", "-f", "main.py"])
        st.success("Hand Gesture Cursor Control stopped!")
    except Exception as e:
        st.error(f"Error: {e}")
