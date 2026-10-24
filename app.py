import duckdb
import pandas as pd
import streamlit as st

st.write("""
# SQL SRS
Spaced Regulation System SQL practice
         """)

option = st.selectbox(
    label="What would you like to review?",
    options=("JOINS", "GROUP BY", "Window Functions"),
    index=None,
    placeholder="Select a theme..."
)
st.write(f"You selected: {option}")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    try:
        sql_query = st.text_area(label="Entrer votre requête SQL")
        result = duckdb.sql(sql_query).df()
        
        st.write("Vous avez saisi la requête suivante :")
        st.code(sql_query)
    
        st.dataframe(result)
        
    except (AttributeError, duckdb.BinderException, duckdb.ParserException) as e:
        st.warning(f"Erreur : {e}")

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
