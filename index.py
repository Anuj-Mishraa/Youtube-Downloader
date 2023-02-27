import streamlit as st
from pytube import YouTube
import os

def main():
    st.title("YouTube Video Downloader")

    # Determine the download folder based on the user's operating system
    if os.name == "nt": # Windows OS
        DOWNLOAD_FOLDER = f"{os.path.expanduser('~')}\\Downloads"
    else: # Linux/Mac OS
        DOWNLOAD_FOLDER = f"{os.path.expanduser('~')}/Downloads"

    # Get the YouTube video URL from the user
    video_url = st.text_input("Enter the YouTube video URL:")

    # Download the YouTube video when the user clicks the "Download" button
    if st.button("Download"):
        try:
            # Create a YouTube object from the video URL
            yt = YouTube(video_url)

            # Get the highest resolution video stream
            stream = yt.streams.get_highest_resolution()

            # Download the video to the download folder
            stream.download(output_path=DOWNLOAD_FOLDER)

            # Show success message to user
            st.success("Video downloaded successfully! Check your Downloads folder.")

        except Exception as e:
            # Show error message to user
            st.error(f"Oops! Something went wrong. Error message: {e}")

if __name__ == '__main__':
    main()
