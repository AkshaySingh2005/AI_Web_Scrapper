import streamlit as st
from scrape import scrape_website,split_dom_content,clean_body_content,extract_body_content
from parse import parse_with_ollama

st.title('AI Web Scrapper')
url = st.text_input('Enter a Website URL')

if st.button('Scrape Website'):
    st.write("Scraping Website...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content= clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("view DOM Content"):
        st.text_area("DOM Content",cleaned_content,height=300)


if "dom_content" in st.session_state:
    parse_desc = st.text_area("Describe what you want to parse ?")

    if st.button("Parse Content"):
        if parse_desc:
            st.write("Parsing Content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks,parse_desc)
            st.write(result)