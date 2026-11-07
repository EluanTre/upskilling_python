#!/home/lrcom/data_upskilling/upskilling_python/.venv/bin/python3
import io

import duckdb
import pandas as pd

# Conversion des DF création de tables SQL dans une DB virtuelle duckdb
with duckdb.connect('data/file.duckdb') as con:
    
    # ----------------------------------------------------------------------
    # EXERCICES LIST
    # ----------------------------------------------------------------------
    dict_data = {
        'theme': ['CROSS JOINS', 'WINDOWS FUNCTION'],
        'exercise_name': ['beverages_and_food', 'simple_window'],
        'tables': [['beverages', 'food_items'], 'simple_window'],
        'last_reviewed': ['1970-01-01', '1970-01-01'],
    }
    df_data = pd.DataFrame(dict_data)
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS memory_state AS
        SELECT *
        FROM df_data;      
        """)
    
    # ----------------------------------------------------------------------
    # CROSS JOINS EXERCICES
    # ----------------------------------------------------------------------
    CSV = """
    beverage,price
    orange juice,2.5
    expresso,2
    tea,3
    """
    beverages = pd.read_csv(io.StringIO(CSV))
    con.execute(
        """
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
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS food_items AS 
        SELECT * 
        FROM food_items;
        """)
