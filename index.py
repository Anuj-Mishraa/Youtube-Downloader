
import streamlit as st
import base64
from PIL import Image
# from streamlit.components.v1 import HtmlComponent
import time
st.set_page_config(layout="wide",page_title="Anuj Mishra",page_icon="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f468-1f3fc-200d-1f393.png")

def set_background(png_file):
    bg_img = '''
    <style>
    .stApp {
    background-image: url("%s");
    background-size: contain;
    }
    </style>
    '''%png_file
    st.markdown(bg_img, unsafe_allow_html=True)
set_background('https://i.ibb.co/yS6JpW1/OIP-2.jpg')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
# st.markdown(hide_menu_style, unsafe_allow_html=True)
p1_con ='''
<head>
    <style>
        * {
            padding: 0;
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
        }

        .card {
            height: 220px;
            max-width: 200px;
            position: relative;
            margin: 30px 10px;
            padding: 20px 15px;
            background: wheat;
            display: flex;
            flex-direction: column;
            box-shadow: 0 5px 202px black;
            transition: 0.3s ease-in-out;
        }

        .card:hover {
            height: 420px;
        }

        .card .imgbox {
            position: relative;
            width: 260px;
            height: 260px;
            top: -60px;
            left: 0px;
        }

        .card .imgbox img {
            max-width: 100%;
            border-radius: 4px;
        }

        .card .content {
            position: relative;
            margin-top: -100px;
            padding: 10px 15px;
            text-align: center;
            color: #111;
            visibility: hidden;
            opacity: 0;
            transition: 0.3s ease-in-out;
        }

        .card:hover .content {
            visibility: visible;
            opacity: 1;
            margin-top: -5px;
            transition-delay: 0.3s;
        }

        /* css part completed*/
    </style>
</head>
<div class="card">
    <div class="imgbox">
        <img src="https://i.ibb.co/gMCnPCp/handwriting-recognition-line-icon-hand-holding-pen-and-writing-image-vector-id901563256-k-6-m-901563.jpg">
    </div>
    <div class="content">

        <!--heading of the card-->
        <h1>AlphaNum</h1>

        <!--content of the card-->
        <p>
        Handwriting Cheracter and digit recognition
        Through Deep Learning Neural Network
        </p>
        <a href="https://github.com/Anuj-gr8/APLHA_NUM" target="_blank" rel="noreferrer">
        <img src="https://img.shields.io/badge/ALFANUM-2C2255?style=for-the-badge&logo=alfanum&logoColor=white" /></a>
    </div>
</div>
'''
p2_con ='''
<head>
    <style>
        * {
            padding: 0;
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
        }

        .card {
            height: 220px;
            max-width: 200px;
            position: relative;
            margin: 30px 10px;
            padding: 20px 15px;
            background: wheat;
            display: flex;
            flex-direction: column;
            box-shadow: 0 5px 202px black;
            transition: 0.3s ease-in-out;
        }

        .card:hover {
            height: 420px;
        }

        .card .imgbox {
            position: relative;
            width: 260px;
            height: 260px;
            top: -60px;
            left: 0px;
        }

        .card .imgbox img {
            max-width: 100%;
            border-radius: 4px;
        }

        .card .content {
            position: relative;
            margin-top: -100px;
            padding: 10px 15px;
            text-align: center;
            color: #111;
            visibility: hidden;
            opacity: 0;
            transition: 0.3s ease-in-out;
        }

        .card:hover .content {
            visibility: visible;
            opacity: 1;
            margin-top: -5px;
            transition-delay: 0.3s;
        }

        /* css part completed*/
    </style>
</head>
<div class="card">
    <div class="imgbox">
        <img src="https://i.ibb.co/MGTx808/R.jpg">
    </div>
    <div class="content">

        <!--heading of the card-->
        <h1>Own Browser</h1>

        <!--content of the card-->
        <p>
        A customize browser Build with Python
        with a downloadable setup &
                Installable <a href="https://github.com/Anuj-gr8/my-browser" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/MY_Browser-0078D4?style=for-the-badge&logo=my%20sBrowser&logoColor=white" /></a>
        </p>
    </div>
</div>
'''
p3_con ='''
<head>
    <style>
        * {
            padding: 0;
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
        }

        .card {
            height: 220px;
            max-width: 200px;
            position: relative;
            margin: 30px 10px;
            padding: 20px 15px;
            background: wheat;
            display: flex;
            flex-direction: column;
            box-shadow: 0 5px 202px black;
            transition: 0.3s ease-in-out;
        }

        .card:hover {
            height: 420px;
        }

        .card .imgbox {
            position: relative;
            width: 260px;
            height: 260px;
            top: -60px;
            left: 0px;
        }

        .card .imgbox img {
            max-width: 100%;
            border-radius: 4px;
        }

        .card .content {
            position: relative;
            margin-top: -100px;
            padding: 10px 15px;
            text-align: center;
            color: #111;
            visibility: hidden;
            opacity: 0;
            transition: 0.3s ease-in-out;
        }

        .card:hover .content {
            visibility: visible;
            opacity: 1;
            margin-top: -5px;
            transition-delay: 0.3s;
        }

        /* css part completed*/
    </style>
</head>
<div class="card">
    <div class="imgbox">
        <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAsJCQcJCQcJCQkJCwkJCQkJCQsJCwsMCwsLDA0QDBEODQ4MEhkSJRodJR0ZHxwpKRYlNzU2GioyPi0pMBk7IRP/2wBDAQcICAsJCxULCxUsHRkdLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCz/wAARCAD1APUDASIAAhEBAxEB/8QAHAABAAIDAQEBAAAAAAAAAAAAAAUGAgQHAwEI/8QAShAAAgIBAgQDBAYFBwgLAAAAAQIAAwQFEQYSITETQVEiYXGBFBUyUpGhB0KSsdEWI1RicpPSJDM2U3OUwdNDVWOForK04eLw8f/EABoBAQADAQEBAAAAAAAAAAAAAAABAgQDBQb/xAAuEQEAAgIABQEGBQUAAAAAAAAAAQIDEQQSEyExQQUiUXGBkRRCUmGhFTJDU/D/2gAMAwEAAhEDEQA/AOtxEQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERA+MyqGZiAoBJJOwAHmSZWda4u0zSt6+ctftutVah7iD2JQkBR6Fj8jIvjHilsIDBwXH0l15ucbEVJvsLSOxY/qD3c3pOa11ZmXa/h13X2sxa1urHmbqWsdjtufeZox4omOe86hiz8VyTy08rPmcd6xezeBVVWhJ28Z7Lm/AFK//DNEcXcQA7mzFI9DjKB+KkH85ppoeqMAWGPX7ntJP4IpH5z0+oM//XYv42/4ZH4rg69uaHnznyz6rBgcfZlTKuZSwTtz4zs4A99N5P5OJfNL1/TtTrV67ayGPLzITyhj+q6t7St7jOO2aNqlfUVJaB/qbAzfssFM8cPMztMyfGoZq7U9m2uwMFsXua7UO24//RLxGHNG8Von5S74+LvWff7w/QESvcNa5RquLUQxDbFQrnd67EALUufPboVPmDLDM0xMTqXqxMWjcEREhJERAREQEREBERAREQEREBERAREQEREBERATS1TLrwsHLybDsldTsxHcKqlm29+wO03GPKrMeygsdvQD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">
    </div>
    <div class="content">

        <!--heading of the card-->
        <h1>Chat-GPT-clone</h1>

        <!--content of the card-->
        <p>
        A customize Bot Build with Python
            using chat gpt API 
        </p>
        <a href="https://github.com/Anuj-gr8/Chat-gpt-mobile-clone" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/ChatBot-3C7755?style=for-the-badge&logo=Chatbot&logoColor=white" /></a>
    </div>
</div>
'''
p4_con ='''
<head>
    <style>
        * {
            padding: 0;
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
        }

        .card {
            height: 220px;
            max-width: 200px;
            position: relative;
            margin: 30px 10px;
            padding: 20px 15px;
            background: wheat;
            display: flex;
            flex-direction: column;
            box-shadow: 0 5px 202px black;
            transition: 0.3s ease-in-out;
        }

        .card:hover {
            height: 420px;
        }

        .card .imgbox {
            position: relative;
            width: 260px;
            height: 260px;
            top: -60px;
            left: 0px;
        }

        .card .imgbox img {
            max-width: 100%;
            border-radius: 4px;
        }

        .card .content {
            position: relative;
            margin-top: -100px;
            padding: 10px 15px;
            text-align: center;
            color: #111;
            visibility: hidden;
            opacity: 0;
            transition: 0.3s ease-in-out;
        }

        .card:hover .content {
            visibility: visible;
            opacity: 1;
            margin-top: -5px;
            transition-delay: 0.3s;
        }

        /* css part completed*/
    </style>
</head>
<div class="card">
    <div class="imgbox">
        <img src="https://th.bing.com/th/id/OIP.3VXhOtSoR2U9chdOt7qSmQHaGt?w=197&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7">
    </div>
    <div class="content">

        <!--heading of the card-->
        <h1>N-L-P</h1>

        <!--content of the card-->
        <p>
        A kivy Application for Natural-
        Language-Processing like translation,
        Text-to-Speech
        </p>
        <a href="https://github.com/Anuj-gr8/Play_lang" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/PlayLang-D83B01?style=for-the-badge&logo=PlayLang&logoColor=white" /></a>
    </div>
</div>
'''




page_bg_img = '''

<p align="center">
  <a href="https://github.com/Anuj-gr8/Anuj-gr8/"><img src="https://readme-typing-svg.herokuapp.com?lines=Computer+Science+Student;AI-ML%20Enthusiast;Cafephile;Always%20learning%20new%20things;Evolving&center=true&width=500&height=50"></a>
</p>
<p align='center'><em><b>Find yourself to discover the real you.</b></em>
<br/>
<em><b>- Key words of the life</b></em>
'''
page_bg_img1 = '''

<br />
</h1>

<p align='center'><em><b>Coming together is a beginning; keeping together is progress; working together is success.</b></em>
<br/>
 <em><b>- Henry Ford</b></em>
<br><br/>
'''
page_footer = '''
<br><br>
### Reach me:
[![Instagram](https://img.shields.io/badge/-Instagram-c13584?style=flat&labelColor=c13584&logo=instagram&logoColor=white&align=center)](https://www.instagram.com/anuj_mishra028/)
[![Twitter Follow](https://img.shields.io/twitter/follow/Anujmishra27003?color=1DA1F2&logo=twitter&style=flat&align=center)](https://twitter.com/Anujmishra27003?t=uUCjGiuVtJgVozF71iMVOQ&s=08)
[![Linkedin](https://img.shields.io/static/v1?label=&message=Linkedin&color=0E7FBF&&&style=flat&logo=linkedin&logoColor=white&align=center)](https://www.linkedin.com/in/anuj-mishra-500320216/)
[![Medium](https://img.shields.io/website?label=Medium&style=flat&url=https%3A%2F%2Fwww.medium.com%2Fprofile%2Fanuj-mishra&align=center)](
https://anuj-mishra.medium.com/)
[![Github](https://img.shields.io/badge/-Github-c13584?style=flat&labelColor=c13584&logo=github&logoColor=white&align=center)](https://github.com/Anuj-gr8/Anuj-gr8)

'''
work_spaces = '''
<p align='center'>
<br/><br/>
  <!-- <img alt="os" src="https://img.shields.io/badge/Apple-Acer_Nitro_5-999999?style=flat&logo=apple&logoColor=white" /> -->
  <img alt="os" src="https://img.shields.io/badge/Windows-11_5-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
  <img alt="soc" src="https://img.shields.io/badge/Intel-Core_i5-0071C5?style=for-the-badge&logo=intel&logoColor=white" />
  <img alt="ram" src="https://img.shields.io/badge/RAM-8GB-%230071C5.svg?&style=for-the-badge&logoColor=white" /><br><br>
  <img alt="graphics" src="https://img.shields.io/badge/NVIDIA-GTX1650-76B900?style=for-the-badge&logo=nvidia&logoColor=white" />
  <img alt="ssd" src="https://img.shields.io/badge/256%20GB%20SSD-grey?style=for-the-badge" />
  <img alt="hdd" src="https://img.shields.io/badge/1%20TB%20HDD-grey?style=for-the-badge" />
</p>
<br/><br/>
'''
soft ='''
<p align='center'>
<br><br>
<img src="https://img.shields.io/badge/Eclipse-2C2255?style=for-the-badge&logo=eclipse&logoColor=white" />
<img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white" /><br><br>
<img src="https://img.shields.io/badge/Microsoft_Office-D83B01?style=for-the-badge&logo=microsoft-office&logoColor=white" />
<img src="https://img.shields.io/badge/PyCharm-D83B65?style=for-the-badge&logo=PyCharm&logoColor=red"/>
</p>
<br/><br/>
'''
projects ='''
<p align='center'>
<br><br>
<h5>Handwriting Cheracter and digit recognition: 👉
<a href="https://github.com/Anuj-gr8/APLHA_NUM" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/ALFANUM-2C2255?style=for-the-badge&logo=alfanum&logoColor=white" /></a></h5><br>
<h5>Building Browser with python: 👉
<a href="https://github.com/Anuj-gr8/my-browser" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/MY_Browser-0078D4?style=for-the-badge&logo=my%20sBrowser&logoColor=white" /></a></h5><br>
<h5>Ecom/EdTech Chatbot : 👉
<a href="https://github.com/Anuj-gr8/Edtech_chatbot" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/ChatBot-3C7755?style=for-the-badge&logo=Chatbot&logoColor=white" /></a></h5><br>
<h5>Play-lang: 'A Tool to doing some language tasks' 👉
<a href="https://github.com/Anuj-gr8/Play_lang" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/PlayLang-D83B01?style=for-the-badge&logo=PlayLang&logoColor=white" /></a></h5><br>
<h5>Py_Site: 'A portfolio website built by python' 👉
<a href="https://github.com/Anuj-gr8/mywebsite" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/mywebsite-D83B65?style=for-the-badge&logo=mywebsite&logoColor=red"/></a></h5><br>
</p>
<br/><br/>
'''
Skills ='''
<p align='center'>
<a href="https://www.python.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="30" alt="vscode" /></a>
<a href="https://docs.microsoft.com/en-us/cpp/?view=msvc-170" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" height="30" alt="C" /></a>
<a href="https://docs.microsoft.com/en-us/cpp/?view=msvc-170" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" height="30" alt="C++" /></a>
<a href="https://www.w3.org/TR/CSS/#css" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/css3-colored.svg" height="30" alt="CSS3" /></a>
<a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/html5-colored.svg" height="30" alt="HTML5" /></a>
<a href="https://www.oracle.com/java/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" height="30" alt="Java" /></a>
<a href="https://www.mysql.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/mysql-colored.svg" height="30" alt="MySQL" /></a>
<a href="https://desktop.github.com/" target="_blank" rel="noreferrer"><img src="https://avatars.githubusercontent.com/u/13171334?s=200&v=4" height="30" alt="githubdesktop" /></a>
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"><img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" height="30" alt="git" /></a>
<a href="https://code.visualstudio.com/" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/1024px-Visual_Studio_Code_1.35_icon.svg.png" height="30" alt="vscode" /></a>

</p>
<br/><br/>
'''
certi = '''
    <iframe src="https://certificates.tiiny.site" width="100%" height="500px">
    </iframe>
'''
extra = '''
<h4 style='text-align: center; color: red;'><a href='#'>Currently I am the Technical team head of the Microsoft Technical Club VIT BHOPAL</a></h4>
'''
Contact = '''
<br><br>
[![WhatsApp](https://img.shields.io/badge/-WhatsApp-D18984?style=flat&labelColor=c13584&logo=WhatsApp&logoColor=white&align=center)](https://wa.link/t06alh)
[![Eamil](https://img.shields.io/badge/E--mail-G--mail-blue?&logo=G-mail&style=flat&align=center)](mailto:anujmishra282003@gmail.com)
[![Call](https://img.shields.io/badge/-Call-E19084?style=flat&labelColor=c13584&logo=Call&logoColor=white&align=center)](tel:+918839219481)

'''
img = '''
<a><img src="https://i.ibb.co/7X94fYV/my-image1.png" alt="my image" width="250" height="250"></a>
'''
st.markdown("<h1 style='text-align: center; color: red;'><a href='https://git.io/typing-svg'><img src='https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=37&duration=2500&pause=1000&color=89E94E&background=5730FF00&width=435&lines=Hey,+I+am+Anuj+🙋‍♂️' alt='Typing SVG' /></a></h1>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["Home", "About", "Contact"])
with tab1:
    with st.spinner('Wait for it...'):
        time.sleep(2)
    # image = Image.open("https://www.bing.com/images/search?q=Google+Upload+Icon&FORM=IRIBIP")
    col1, col2 = st.columns([3, 1])
    with col1.container():
        st.markdown(page_bg_img1, unsafe_allow_html=True)
        st.markdown(page_bg_img, unsafe_allow_html=True)
    st.write("Hi, I'm Anuj Mishra, a passionate self-taught web developer and AI enthusiast from India. My passion for software lies in dreaming up ideas and making them come true with elegant interfaces."+ 
    "\nI take great care in the experience, architecture, and code quality of the things I build. I'm 20 years old and graduated with a degree in Integrated M.Tech. with CSE specialization in AI&ML VIT BHOPAL UNIVERSITY.\nI'm also an open-source enthusiast. I learned a lot from the open-source community and I love how collaboration and knowledge sharing happened through open-source.")

    with col2.container():
        st.markdown(img, unsafe_allow_html=True)
with tab2:
    st.balloons()
    st.write("## About")
    with st.expander("🏆🏆Skils🏆🏆"):
        st.markdown(Skills, unsafe_allow_html=True)
    with st.expander("💻 My workspace"):
        st.markdown(work_spaces, unsafe_allow_html=True)
    with st.expander("⚙️ Softwares I'm Familiar with :"):
        st.markdown(soft, unsafe_allow_html=True)
    with st.expander("📽️ Major Projects:"):
        p1, p2, p3, p4 = st.columns(4)
        with p1:
            st.components.v1.html(p1_con,height=470)
        with p2:
            st.components.v1.html(p2_con,height=470)
        with p3:
            st.components.v1.html(p3_con,height=470)
        with p4:
            st.components.v1.html(p4_con,height=470)
        # st.markdown(projects, unsafe_allow_html=True)
    with st.expander("📇Certifications:"):
        st.markdown(certi, unsafe_allow_html=True)
    with st.expander("Extra curriculurm:"):
        st.markdown(extra, unsafe_allow_html=True)
    
with tab3:
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success("## Contact me")
    progrs = st.progress(0)
    for i in range(100):
        time.sleep(0.005)
        progrs.progress(i+1)
    st.markdown(Contact, unsafe_allow_html=True)
st.write()
st.write()
st.write(" \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write(" \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write(" \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write(" \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
 
st.markdown(page_footer, unsafe_allow_html=True)
