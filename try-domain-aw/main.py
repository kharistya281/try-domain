import streamlit as st
import mysql.connector

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
    
def main():
    st.title("Aplikasi Streamlit untuk Akses Database MySQL")

    if st.button("Connect"):
        conn = connectToDatabase()
        if conn:
            st.success("Connected to database successfully!")

if __name__ == "__main__":
    main()
