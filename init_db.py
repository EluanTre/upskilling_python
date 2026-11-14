#!/home/lrcom/data_upskilling/upskilling_python/.venv/bin/python3
# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd

# Conversion des DF création de tables SQL dans une DB virtuelle duckdb
with duckdb.connect("data/file.duckdb") as conn:

    # ----------------------------------------------------------------------
    # EXERCICES LIST
    # ----------------------------------------------------------------------
    dict_data = {
        "theme": ["CROSS JOINS", "CROSS JOINS"],
        "exercise_name": ["beverages_and_food", "sizes_and_trademarks"],
        "tables": [["beverages", "food_items"], ["sizes", "trademarks"]],
        "last_reviewed": ["1980-01-01", "1970-01-01"],
    }
    df_data = pd.DataFrame(dict_data)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS memory_state AS
        SELECT *
        FROM df_data
        -- L'exercice le plus ancien vu affiché en 1er
        ORDER BY last_reviewed;      
        """)

    # ----------------------------------------------------------------------
    # CROSS JOINS EXERCICE N° 1
    # ----------------------------------------------------------------------
    CSV = """
    beverage,price
    orange juice,2.5
    expresso,2
    tea,3
    """
    beverages = pd.read_csv(io.StringIO(CSV))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS beverages AS 
        SELECT * 
        FROM beverages;
        """)

    CSV2 = """
    food_item,food_price
    cookie_juice,2.5
    chocolatine,2
    muffin,3
    """
    food_items = pd.read_csv(io.StringIO(CSV2))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS food_items AS 
        SELECT * 
        FROM food_items;
        """)

    # ----------------------------------------------------------------------
    # CROSS JOINS EXERCICE N° 2
    # ----------------------------------------------------------------------
    SIZE = """
    size
    XS
    M
    L
    XL
    """
    size_df = pd.read_csv(io.StringIO(SIZE))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sizes AS
        SELECT *
        FROM size_df;
        """)

    TRADEMARK = """
    trademark
    Nike
    Asphalte
    Abercrombie
    Lewis
    """
    trademark_df = pd.read_csv(io.StringIO(TRADEMARK))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS trademarks AS
        SELECT *
        FROM trademark_df;
        """)
