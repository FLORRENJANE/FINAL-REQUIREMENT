%%writefile streamlit_app.py
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("streamlit_app.py", "ITEQMT Machine Learning Application Portfolio", "💻"),
        Section("Machine Learning UI App", "🧙‍♂️"),
        Page("croprecom.py", "Crop Recommendation ML Model", "1️⃣", in_section=True),
        Page("analyzer.py", "Basic Sentiment Analyzer", "2️⃣", in_section=True),
        Page("classify.py", "Image Classification 1 (Sky Condition)", "3️⃣", in_section=True),
  
        Section("Sample Source Code", "💾"),
        Page("croprecom_src.py", "Crop Recommendation SRC", "1️⃣", in_section=True),
        Page("analyzer_src.py", "Basic Sentiment Analyzer SRC", "2️⃣", in_section=True),
        Page("classify_src.py", "Image Classification SRC", "3️⃣", in_section=True),
    ]
)

hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 ML Learning by [FLORRENJANE](https://github.com/FLORRENJANE)")

st.image("./back.jpg")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("About""Myself"""):
    st.markdown("""

    #

        **About Myself**
        **Name:** Florren Jane C. Orique
        **Age:** 22 
        **School:** Carlos Hilado Memorial State University
        **Course, Year&Section:** BSIS 3B
        **Skills Learned:** Html&css, js, java, php, sql, c++, and python
    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 Read More

##### 👨‍👦‍👦 Description of Apps

* Prediction App is about the crop recommendation machine learning based on the required input in croprecom.py file
* Sentiment Analyzer is about the emotion identifier of information input of how you feel or what have will you do, etc. in analyzer.py file
* Image Classification is about the determination wether the uploaded picture is an apple, orange, lemon, or mandarin.

##### 👨‍🔧 What I have Learned

              Through the development of the Prediction app, Sentiment Analyzer, and Image Classification app using Streamlit, 
              I have gained extensive knowledge and practical experience in various key areas. This includes understanding different 
              machine learning algorithms and their training processes, data cleaning and preparation techniques, and the evaluation 
              of model performance. Specifically, I learned how to process and analyze text data for sentiment analysis, handle and 
              classify image data using machine learning models, and create interactive web applications for user-friendly interfaces. 
              Additionally, I enhanced my Python programming skills, particularly in integrating machine learning models into Streamlit 
              apps, and gained valuable insights into project planning, development, and deployment of real-world applications.

### 🔎 Overview""", unsafe_allow_html=True)

st.image("./back.jpg")

st.markdown("""
              My name is Florren Jane C. Orique, a 22-year-old student from Carlos Hilado Memorial State University, 
              currently enrolled in BSIS 3B. I have acquired various skills in programming languages such as HTML & CSS, 
              JavaScript, Java, PHP, SQL, C++, and Python. Through the development of my applications, I have created a 
              Prediction app that uses trained models for forecasting and estimating outcomes, a Sentiment Analyzer that 
              determines the sentiment of text data, and an Image Classification app that categorizes images using machine 
              learning models. These projects have deepened my understanding of algorithmic processes, data preparation, 
              model evaluation, and the deployment of machine learning models in user-friendly interfaces. Additionally, I 
              have improved my skills in building interactive applications with Streamlit, furthering my knowledge in both 
              programming and machine learning domains. 
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
