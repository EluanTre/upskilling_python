# pylint: disable=missing-module-docstring
# pylint: disable=trailing-whitespace

import duckdb
import streamlit as st

with duckdb.connect('data/file.duckdb') as con:

    ANSWER_STR = """
    SELECT *
    FROM beverages
    CROSS JOIN food_items;
    """
    # solution_df = duckdb.sql(ANSWER_STR).df()

    with st.sidebar:
        theme = st.selectbox(
            label="What would you like to review?",
            options=("CROSS JOINS", "GROUP BY", "WINDOWS FUNCTION"),
            index=None,
            placeholder="Select a theme...",
        )
        st.write(f"You selected: {theme}")
        
        exercise = con.execute(
            f"""
            SELECT * 
            FROM memory_state
            WHERE theme LIKE '{theme}';
            """).df()
        st.write(exercise)

    st.header("Enter your code:")
    query = st.text_area(label="votre code SQL ici :", key="user_input")

    # if query:
    #     result = duckdb.sql(query).df()
    #     st.dataframe(result)

    #     n_lines_difference = result.shape[0] - solution_df.shape[0]
    #     if n_lines_difference != 0:
    #         st.warning(f"""
    #             Result has a {n_lines_difference} 
    #             lines difference with the solution_df
    #             """)

    #     try:
    #         result = result[solution_df.columns]
    #         st.dataframe(result.compare(solution_df))
    #     except (KeyError, ValueError) as e:
    #         st.error(f"Some columns are missing : {e}")

    # tab2, tab3 = st.tabs(["Table", "solution_df"])

    # with tab2:
    #     st.write("Table: beverages")
    #     st.dataframe(beverages)
    #     st.write("Table: food_items")
    #     st.dataframe(food_items)
    #     st.write("Expected:")
    #     st.dataframe(solution_df)

    # with tab3:
    #     st.code(ANSWER_STR)

