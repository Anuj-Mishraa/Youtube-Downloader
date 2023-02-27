import streamlit as st
from pytube import YouTube
import os
def main():
    st.title("YouTube Video Downloader")
    sys_name = st.text_input("Enter your system mobile or pc:")
    if sys_name == "pc":
        DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
    elif sys_name == "mobile":  
        DOWNLOAD_FOLDER = "Storage/emulated/0/Download"
    else:
        st.error("PLease wite only mobile or pc")
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
        except:
            st.error("Oops! Something went wrong. Please check the video URL and try again.")

if __name__ == '__main__':
    main()
