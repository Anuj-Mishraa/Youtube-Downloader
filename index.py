import streamlit as st
from pytube import YouTube
import os

def main():
    st.title("YouTube Video Downloader")

    # Get the YouTube video URL from the user
    video_url = st.text_input("Enter the YouTube video URL:")

    # Download the YouTube video when the user clicks the "Download" button
    if st.button("Download"):
        try:
            # Create a YouTube object from the video URL
            yt = YouTube(video_url)

            # Get the highest resolution video stream
            stream = yt.streams.get_highest_resolution()

            # Ask the user to select the download directory using the system's file explorer
            download_dir = st.text_input("Enter the download directory:")
            if not download_dir:
                download_dir = os.path.expanduser("~") + os.sep + "Downloads"
            else:
                download_dir = os.path.abspath(download_dir)

            if not os.path.exists(download_dir):
                st.error(f"The directory {download_dir} does not exist.")
                return

            # Download the video to the selected directory
            file_path = stream.download(download_dir)
            st.success(f"Video downloaded successfully at {file_path}")
        except:
            st.error("Oops! Something went wrong. Please check the video URL and try again.")

if __name__ == '__main__':
    main()
