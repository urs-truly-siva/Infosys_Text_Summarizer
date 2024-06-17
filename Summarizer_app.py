import streamlit as st
import re
import spacy
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from streamlit_lottie import st_lottie
import json
import time

def footer():
    # Footer Section

    st.markdown("""------""")
    st.markdown("""
        <p  
        align='center'>Developed by </p>
        """, unsafe_allow_html=True)
    st.markdown("""
        <p  
        align='center'>Avanigadda Sivayya</p>
        """, unsafe_allow_html=True)

   
    st.markdown(""" 
        <p align="center">If you want any assistances or have any  queries. just, feel free to reach out!</p>
        
        <p align="center">
        <a href="https://www.linkedin.com/in/siva-avanigadda/" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/linkedin.png" alt="LinkedIn" style="width:40px;"/>
        </a>
        
        <a href="mailto:sivaavanigadda620@gmail.com" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/gmail.png" alt="GitHub" style="width:40px;"/>
        </a>

        <a href="https://www.instagram.com/urs_truly_.siva/">
            <img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" alt="Instagram" style="width: 40px;">
        </a>

        </p>
    """, unsafe_allow_html=True)

    st.markdown("""  <p align="center"> - Siva620..🤘🏻</p>""", unsafe_allow_html=True)



st.set_page_config(page_title="TextSummarizer 📄✨", page_icon="📚", layout="wide",)

nlp = spacy.load("en_core_web_sm")

nltk.download('punkt')

def preprocess(sentences):
    preprocessed_sentences = []
    for sentence in sentences:
        doc = nlp(sentence)
        extracted_words = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        preprocessed_sentences.append(" ".join(extracted_words))
    return preprocessed_sentences

def summarize_text(text, num_sentences):
    # Preprocess text
    text = re.sub(r'\([^)]*\)', ' ', text)
    text = re.sub(r'\[[^\]]*\]', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'"', '', text)

    # Tokenize into sentences
    original_sentences = nltk.sent_tokenize(text)

    # Preprocess sentences
    preprocessed_sentences = preprocess(original_sentences)

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(preprocessed_sentences)

    # Sum TF-IDF scores for each sentence
    sum_scores = matrix.toarray().sum(axis=1)

    # Rank sentences by score
    ranked_scores = (-sum_scores).argsort()

    # Get top sentence indices
    top_score_indices = sorted(ranked_scores[:num_sentences])

    # Generate final summary
    final_sentences = [original_sentences[i] for i in top_score_indices]
    summary = " ".join(final_sentences)

    return summary

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load Lottie animation
lottie_animation = load_lottie_file("summarer.json")
ani = load_lottie_file('loading.json')


#st.title("🧠 TextBrief: AI Summarization Assistant📄🤖")
st.markdown(
    """
    <div style="display:flex; justify-content:center; align-items:center;">
        <h1>🧠 TextBrief: AI Summarization Tool 📄🤖</h1>
    </div>
    """,
    unsafe_allow_html=True
)

#text_input = st.text_area("Enter the text to summarize:")
#num_sentences = st.slider("Number of sentences in summary:", min_value=1, max_value=10, value=4)
col1, col2 = st.columns([2, 1])

with col1:
    text_input = st.text_area("Enter the text to summarize:", height=350)

with col2:
    st_lottie(lottie_animation, height=400, key="animation")

num_sentences = st.slider("Number of sentences in summary:", min_value=1, max_value=10, value=4)


if st.button("Summarize"):
    if text_input:
        with st.spinner('Summarizing....'):
            time.sleep(5) 
            summary = summarize_text(text_input, num_sentences)
        st.subheader("Summary:")
        #st.write(summary)
        formatted_summary = "\n" + "\n".join(summary.split(". "))
        code_snippet = f'''\n{formatted_summary}\n '''
        st.code(code_snippet, language='python')
        
        st_lottie(ani, height=300, key="ani")
    else:
        st.error("Please enter text to summarize.")

    footer()



