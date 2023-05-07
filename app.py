import streamlit as st
import subprocess


st.set_page_config(page_title="Nerjemahake",
    initial_sidebar_state="expanded")

st.title("Nerjemahake")


def translate(source_text):
    
    with open("data/source.txt", "w") as f:
        f.write(source_text)
    
    
    command = "onmt_translate -model data/model_step_2000.pt -src data/source.txt -output data/pred.txt -verbose"
    subprocess.run(command, shell=True)
    
    
    with open("data/pred.txt", "r") as f:
        pred_text = f.read()
    
    return pred_text


st.sidebar.markdown("# Nerjemahake: Aplikasi Penerjemahan Bahasa Jawa Ngoko - Krama")
st.sidebar.markdown("Aplikasi ini adalah demo penerjemahan dengan metode Neural Machine Translation menggunakan OpenNMT.")
st.sidebar.markdown("Masukkan teks yang ingin diterjemahkan pada kotak teks dan klik 'Terjemahkan'.")
# st.sidebar.markdown("---")
# st.sidebar.markdown("# Help")
# st.sidebar.markdown("Jika ada pertanyaan, silahkan kontak saya di support@gmail.com.")


with st.form("my_form"):
    source_text = st.text_area("Masukkan kalimat dalam bahasa jawa ngoko", placeholder="Contoh: Nggawa jeruk kuwi!", height=40, max_chars=200)
    if st.form_submit_button("Terjemahkan"):
        
        with st.spinner("Sedang proses"):
            
            pred_text = translate(source_text)
        
        st.info(pred_text)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
