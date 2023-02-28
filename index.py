import streamlit as st
from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog

def main():
    st.title("YouTube Video Downloader")

    # Get the YouTube video URL from the user
    video_url = st.text_input("Enter the YouTube video URL:")

    # Get the download directory from the user
    download_dir = st.button("Select download directory")
    if download_dir:
        root = tk.Tk()
        root.withdraw()
        download_dir = filedialog.askdirectory()
        st.write(f"Selected directory: {download_dir}")

    # Download the YouTube video when the user clicks the "Download" button
    if st.button("Download"):
        try:
            # Create a YouTube object from the video URL
            yt = YouTube(video_url)

            # Get the highest resolution video stream
            stream = yt.streams.get_highest_resolution()

            # Download the video to the selected directory
            stream.download(download_dir)
            st.success("Video downloaded successfully!")
        except:
            st.error("Oops! Something went wrong. Please check the video URL and try again.")

if __name__ == '__main__':
    main()
