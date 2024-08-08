# # streamlit_app.py

# import streamlit as st
# from streamlit_gsheets import GSheetsConnection
# import pandas as pd

# # Create a connection object.
# conn = st.connection("gsheets", type=GSheetsConnection)

# df = conn.read()

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")


# if st.button("Update Worksheet"):
#     conn.update(data=pd.DataFrame({
#         'name': ['Peter'],
#         'pet': ['fish']
#     }))
#     st.success("Worksheet Updated 🤓")

import streamlit as st

# Sample list of F1 drivers (you can update this with the current list of drivers)
f1_drivers = [
    "Max Verstappen",
    "Sergio Pérez",
    "Lewis Hamilton",
    "George Russell",
    "Charles Leclerc",
    "Carlos Sainz",
    "Lando Norris",
    "Oscar Piastri",
    "Fernando Alonso",
    "Lance Stroll",
    "Esteban Ocon",
    "Pierre Gasly",
    "Alexander Albon",
    "Logan Sargeant",
    "Daniel Ricciardo",
    "Yuki Tsunoda",
    "Guanyu Zhou",
    "Valtteri Bottas",
    "Kevin Magnussen",
    "Nico Hülkenberg",
]

# List of user names
user_names = [
    "Fran",
    "Nacho",
    "Jorge Ortiz",
    "Javi",
    "Bengoa",
    "Alpuente",
    "Julio",
    "Rubén",
]

# Streamlit app title
st.title("Porra F1 :racing_car:")

# Dropdown to select user name
user_name = st.selectbox(
    "Nombre:", user_names, placeholder="Selecciona tu nombre", index=None
)

# Dropdowns to select top 3 drivers
st.header("Top 3")

top_1 = st.selectbox("1", f1_drivers, index=None)
top_2 = st.selectbox(
    "2", [driver for driver in f1_drivers if driver != top_1], index=None
)
top_3 = st.selectbox(
    "3", [driver for driver in f1_drivers if driver not in [top_1, top_2]], index=None
)

# Button to submit prediction
if st.button("Enviar"):
    st.write(f"**{user_name}**!")
    st.write("Tu predicción es:")
    st.write(f"1: **{top_1}**")
    st.write(f"2: **{top_2}**")
    st.write(f"3: **{top_3}**")
