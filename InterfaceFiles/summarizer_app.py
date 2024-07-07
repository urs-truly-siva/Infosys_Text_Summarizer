import streamlit as st
import re
import spacy
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from streamlit_lottie import st_lottie
import json
import time
import os
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure correct numpy version
try:
    import numpy as np
    assert np.__version__ == '1.23.5'
except (ImportError, AssertionError):
    install_package('numpy==1.23.5')

def footer():
    st.markdown("""------""")
    st.markdown("""
        <p>🚀 Developed by Avanigadda Sivayya 🚀</p>
        """, unsafe_allow_html=True)
    
    st.markdown(""" 
        <p>🌟 Let's connect and collaborate! 🌟</p>
        
        <p>
        <a href="https://www.linkedin.com/in/siva-avanigadda/" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/linkedin.png" alt="LinkedIn" style="width:20px;"/>
            LinkedIn
        </a>
        <br>
        <a href="mailto:sivaavanigadda620@gmail.com" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/gmail.png" alt="Gmail" style="width:20px;"/>
            Gmail
        </a>
        <br>
        <a href="https://www.instagram.com/urs_truly_.siva/" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" alt="Instagram" style="width:20px;"/>
            Instagram
        </a>
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""<p> - Siva620 ✨🤘🏻</p>""", unsafe_allow_html=True)

st.set_page_config(page_title="TextSummarizer 📄✨", page_icon="📚", layout="wide")

@st.cache_resource
def load_spacy_model():
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        from spacy.cli import download
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")
    return nlp

nlp = load_spacy_model()

nltk.download('punkt')

def preprocess(sentences):
    preprocessed_sentences = []
    for sentence in sentences:
        doc = nlp(sentence)
        extracted_words = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        preprocessed_sentences.append(" ".join(extracted_words))
    return preprocessed_sentences

def summarize_text(text, num_sentences):
    text = re.sub(r'\([^)]*\)', ' ', text)
    text = re.sub(r'\[[^\]]*\]', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'"', '', text)

    original_sentences = nltk.sent_tokenize(text)
    preprocessed_sentences = preprocess(original_sentences)

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(preprocessed_sentences)

    sum_scores = matrix.toarray().sum(axis=1)
    ranked_scores = (-sum_scores).argsort()
    top_score_indices = sorted(ranked_scores[:num_sentences])

    final_sentences = [original_sentences[i] for i in top_score_indices]
    summary = " ".join(final_sentences)

    return summary

def load_lottie_file(filepath: str):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    else:
        return None

lottie_animation = load_lottie_file(os.path.join("InterfaceFiles", "summarer.json"))
ani = load_lottie_file(os.path.join("InterfaceFiles", "loading.json"))

st.markdown(
    """
    <div style="display:flex; justify-content:center; align-items:center;">
        <h1>🧠 TextBrief: AI Summarization Tool 📄🤖</h1>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2, 1])

with col1:
    text_input = st.text_area("Enter the text to summarize:", height=350)

with col2:
    if lottie_animation:
        st_lottie(lottie_animation, height=400, key="animation")
    else:
        st.write("Lottie animation not found.")

num_sentences = st.slider("Number of sentences in summary:", min_value=1, max_value=10, value=4)

if st.button("Summarize"):
    if text_input:
        with st.spinner('Summarizing....'):
            time.sleep(5)
            summary = summarize_text(text_input, num_sentences)
        st.subheader("Summary:")
        formatted_summary = "\n" + "\n".join(summary.split(". "))
        code_snippet = f'''\n{formatted_summary}\n '''
        st.code(code_snippet, language='python')
        footer()
        
        if ani:
            st_lottie(ani, height=300, key="ani")
        else:
            st.write("Lottie animation not found.")
    else:
        st.error("Please enter text to summarize.")

    
