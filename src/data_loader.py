import pandas as pd
import os
import sqlite3

def load_data(filepath=None, sql_query=None, db_path=None):
    """
    Loads dataset from CSV, Excel, or SQL database.

    Parameters
    ----------
    filepath : str, optional
        Path to CSV or Excel file (.csv / .xlsx)
    sql_query : str, optional
        SQL query if loading from SQL database
    db_path : str, optional
        Path to SQLite database (.db)

    Returns
    -------
    pandas.DataFrame
        Loaded dataset

    Raises
    ------
    ValueError:
        If invalid or missing path/query is provided
    """

    if filepath:
        if not os.path.exists(filepath):
            raise ValueError(f"File not found: {filepath}")

        if filepath.endswith(".csv"):
            return pd.read_csv(filepath)
        
        elif filepath.endswith(".xlsx") or filepath.endswith(".xls"):
            return pd.read_excel(filepath)
        
        else:
            raise ValueError("Unsupported file type. Use CSV or Excel.")

    if sql_query and db_path:
        if not os.path.exists(db_path):
            raise ValueError(f"Database not found: {db_path}")
        
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(sql_query, conn)
        conn.close()
        return df

    raise ValueError("Provide either a filepath or sql_query + db_path")
