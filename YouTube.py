import streamlit as st
import pandas as pd
from pytube import YouTube
import requests
from streamlit_lottie import st_lottie
import base64
from io import BytesIO

st.set_page_config(page_title="YouTube Downloader", page_icon=":mag_right:", layout="wide")

# Header

st.title("YouTube Video Downloader")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_xtuje6sh.json")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.")
        st.write("The YouTube Video Downloader project is a python project. This provides users to download videos they need in their devices and watch them offline.")
    with right_column:
        st_lottie(lottie_coding, height=190, key="coding")


def main():
	path = st.text_input('Enter URL of any youtube video')
	option = st.selectbox(
     'Select type of download',
     ('audio', 'highest_resolution', 'lowest_resolution'))
	
	# matches = ['audio', 'highest_resolution', 'lowest_resolution']
	if st.button("download"): 
		video_object =  YouTube(path)
		st.write("Title of Video: " + str(video_object.title))
		st.write("Number of Views: " + str(video_object.views))
		if option=='audio':
			video_object.streams.get_audio_only().download()			
		elif option=='highest_resolution':
			video_object.streams.get_highest_resolution().download()
		elif option=='lowest_resolution':
			video_object.streams.get_lowest_resolution().download()
	if st.button("View"): 
		st.video(path) 
        




if __name__ == '__main__':
	main()
