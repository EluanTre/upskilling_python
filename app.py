# pylint: disable=missing-module-docstring
# pylint: disable=trailing-whitespace

import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice,2.5
expresso,2
tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie_juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT *
FROM beverages
CROSS JOIN food_items;
"""
solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    option = st.selectbox(
        label="What would you like to review?",
        options=("JOINS", "GROUP BY", "Window Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write(f"You selected: {option}")

st.header("Enter your code:")
query = st.text_area(label="votre code SQL ici :", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.warning(f"""
            Result has a {n_lines_difference} 
            lines difference with the solution_df
            """)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except (KeyError, ValueError) as e:
        st.error(f"Some columns are missing : {e}")

tab2, tab3 = st.tabs(["Table", "solution_df"])

with tab2:
    st.write("Table: beverages")
    st.dataframe(beverages)
    st.write("Table: food_items")
    st.dataframe(food_items)
    st.write("Expected:")
    st.dataframe(solution_df)

with tab3:
    st.code(ANSWER_STR)
