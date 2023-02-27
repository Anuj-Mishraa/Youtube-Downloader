import streamlit as st
from pytube import YouTube
import os
def main():
    st.title("YouTube Video Downloader")
    sys_path = st.text_input("Enter your path:")
    
    # Get the YouTube video URL from the user
    video_url = st.text_input("Enter the YouTube video URL:")

    # Download the YouTube video when the user clicks the "Download" button
    if st.button("Download"):
        try:
            # Create a YouTube object from the video URL
            yt = YouTube(video_url)

            # Get the highest resolution video stream
            stream = yt.streams.get_highest_resolution()

            # Download the video to the current directory
            stream.download(sys_path)
            st.success("Video downloaded successfully!")
        except:
            st.error("Oops! Something went wrong. Please check the video URL and try again.")

if __name__ == '__main__':
    main()
