import streamlit as st
import os
import urllib.request
import re
def main():
    st.title("YouTube Video Downloader")
    if os.name == "nt":
        DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
    else:
        DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"
    # Get the YouTube video URL from the user
    video_url = st.text_input("Enter the YouTube video URL:")

    # Download the YouTube video when the user clicks the "Download" button
    if st.button("Download"):
        try:
            # Send a request to YouTube to get the page source
            response = urllib.request.urlopen(video_url)
            html = response.read().decode()

            # Extract the video stream URL from the page source
            stream_url = None
            pattern = r'"url_encoded_fmt_stream_map":"(.*?)"'
            match = re.search(pattern, html)
            if match:
                stream_map = match.group(1)
                stream_map = stream_map.replace("%2C", ",")
                stream_map = urllib.parse.unquote(stream_map)
                pattern = r"url=(.*?)(,|&)"
                matches = re.findall(pattern, stream_map)
                for match in matches:
                    if "mime=video/mp4" in match[0]:
                        stream_url = match[0]
                        break

            # Download the video stream to a file
            if stream_url:
                response = urllib.request.urlopen(stream_url)
                with open(os.path.join(DOWNLOAD_FOLDER, "video.mp4"), "wb") as f:
                    f.write(response.read())
                st.success("Video downloaded successfully!")
            else:
                st.error("Oops! Something went wrong. Please check the video URL and try again.")
        except:
            st.error("Oops! Something went wrong. Please check the video URL and try again.")

if __name__ == '__main__':
    main()
