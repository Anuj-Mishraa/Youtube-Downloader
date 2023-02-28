import streamlit as st
from pytube import YouTube
import pytube
import os
from flask import Flask, send_file,request
import requests

app = Flask(__name__)

@app.route('/download')
def main():
    st.title("YouTube Video Downloader")
    video_url = st.text_input("Enter the YouTube video URL:")

    if st.button("Download"):
        # Send a request to the Flask endpoint to download the video
        url = f"http://localhost:5000/download?video_url={video_url}"
        response = requests.get(url)

        if response.status_code == 200:
            st.success("Video downloaded successfully!")
        else:
            st.error("Oops! Something went wrong. Please try again.")

if __name__ == '__main__':
    main()
