# INFOSYS SPRINGBOARD INTERNSHIP 2024 
## A Report On Text Summarizer Model
### Initial Design for the Project Work:

![Initial Design Image](<Initial Design Image.png>)

# Text Summarizer
### Abstract:
This project, developed as the part of Infosys Springboard internship, focuses on creating a Text Summarizer using Natural Language Processing (NLP) techniques. The summarizer aims to reduce the length of documents while preserving key information and meaning, making it easier for users to quickly understand the content of large texts.

### Objectives:
- Develop an automatic text summarization tool [Both Extractive and Abstractive] using NLP.
- Ensure the summarizer maintains the original meaning and key points of the text.
- Create an intuitive user interface for easy interaction with the summarizer.

### Methodology:

<b> Data Collection: </b>
Initially, we searched for suitable datasets from various sources and decided to use the CNN/Daily Mail dataset. We can also easily access the CNN Daily Mail dataset using the `datasets` library in Python.
The CNN Daily Mail dataset is used in this project for text summarization tasks. It consists of news articles and their corresponding summaries, making it an ideal dataset for training and evaluating text summarization models.

link: [kaggle](https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail/code)

### Text Preprocessing:

To prepare the data for summarization, we applied several preprocessing steps:
- **Lower Casing**: Converted all text to lowercase.
- **Removing Special Characters, Numbers and Punctuations**
- **Tokenization**: Split text into individual tokens (words).
- **stop words removal**: Removing stop words

These preprocessing steps help in understanding and processing the text more effectively. The detailed preprocessing steps are demonstrated in the `preprocessing.ipynb` file.





