mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"sivaavanigadda620@gmail.com \"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = \$PORT\n\
" > ~/.streamlit/config.toml

python -m spacy download en_core_web_sm
