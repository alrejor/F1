# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
    
    
if st.button("Update Worksheet"):
    conn.update(data=pd.DataFrame({
        'name': ['Peter'],
        'pet': ['fish']
    }))
    st.success("Worksheet Updated 🤓")