import streamlit as st
import mysql.connector
import pandas as pd 
import psycopg2

def connectToDatabase():
    try:
        conn = mysql.connector.connect(
            host="kubela.id", 
            port=3306, 
            user="davis2024irwan", 
            password="wh451n9m@ch1n3", 
            database="aw"
        )
        if conn.is_connected():
            return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

def run_query(query):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(data, columns=columns)
    cursor.close()
    conn.close()
    return df




def main():
    st.title("Aplikasi Streamlit untuk Akses Database MySQL")

    if st.button("Connect"):
        conn = connectToDatabase()
        if conn:
            st.success("Connected to database successfully!")
    query = st.text_area('Enter your SQL query here:', )

if __name__ == "__main__":
    main()
