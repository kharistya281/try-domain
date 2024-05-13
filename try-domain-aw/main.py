import streamlit as st
import mysql.connector

def connectToDatabase(host, port, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host, 
            port=port, 
            user=user, 
            password=password, 
            database=database
        )
        if conn.is_connected():
            return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None
    
def main():
    st.title("Aplikasi Streamlit untuk Akses Database MySQL")

    host = st.text_input("Host", "kubela.id")
    port = st.number_input("Port", min_value=0, max_value=65535, value=3306, step=1)
    user = st.text_input("User", "davis2024irwan")
    password = st.text_input("Password", type="password", value="wh451n9m@ch1n3")
    database = st.text_input("Database", "aw")

    if st.button("Connect"):
        conn = connectToDatabase(host, port, user, password, database)
        if conn:
            st.success("Connected to database successfully!")

if __name__ == "__main__":
    main()