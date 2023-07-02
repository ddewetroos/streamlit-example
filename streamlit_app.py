#Uploading files

import streamlit as st
from io import StringIO

#upload single file and display it as a dataframe
file = st.file_uploader("Please select a file to upload")
if file is not None:
    #Can be used wherever a "file-like" object is accepted:
    df= pd.read_csv(file)
    st.dataframe(df)
