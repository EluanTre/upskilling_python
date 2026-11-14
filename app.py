# pylint: disable=missing-module-docstring
# pylint: disable=trailing-whitespace

import duckdb
import streamlit as st

with duckdb.connect("data/file.duckdb") as conn:

    with st.sidebar:
        theme = st.selectbox(
            label="What would you like to review?",
            options=("CROSS JOINS", "GROUP BY", "WINDOWS FUNCTION"),
            index=None,
            placeholder="Select a theme...",
        )
        st.write(f"You selected: {theme}")

        exercise = conn.execute(f"""
            SELECT * 
            FROM memory_state
            WHERE theme LIKE '{theme}';
            """).df()
        st.write(exercise)

        # Solution exercise
        try:
            exercise_name = exercise.loc[0, "exercise_name"]
            with open(f"answers/{exercise_name}.sql", "r", encoding="utf-8") as f:
                answer = f.read()
            solution_df = conn.execute(answer).df()
        except (KeyError, FileNotFoundError):
            st.error("Exercice non sélectionné / en cours d'écriture")

    # -----------------------------------------------------------------
    # -------------------- MAIN PAGE ---------------------
    # -----------------------------------------------------------------

    st.header("Enter your code:")
    query = st.text_area(label="votre code SQL ici :", key="user_input")

    if query:
        result = conn.execute(query).df()
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

    tab1, tab2 = st.tabs(["Table", "solution_df"])

    with tab1:
        try:
            for table in exercise.loc[0, "tables"]:
                st.write(f"Table: {table}")
                st.dataframe(conn.execute(f"SELECT * FROM {table}").df())
        except (KeyError, duckdb.CatalogException):
            st.error("Exercice non sélectionné / en cours d'écriture")

    with tab2:
        try:
            st.code(answer)
        except (KeyError, NameError):
            st.error("Exercice non sélectionné / en cours d'écriture")
