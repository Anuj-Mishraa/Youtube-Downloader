import streamlit as st
from pytube import YouTube
import pytube
import os

def main():
    st.title("YouTube Video Downloader")
    DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"
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
            stream.download(DOWNLOAD_FOLDER)
            st.success("Video downloaded successfully!")
        except pytube.exceptions.VideoUnavailable:
            st.error("Oops! Video is unavailable. Please check the video URL and try again.")
        except Exception as e:
            st.error(f"Oops! Something went wrong. Error message: {e}")

if __name__ == '__main__':
    main()
