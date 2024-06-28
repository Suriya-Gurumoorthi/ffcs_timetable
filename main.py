import streamlit as st
import pandas as pd
import re

st.title("Course Information by Room Number")

# File uploader for the dataset
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    # Load the dataset
    df = pd.read_excel(uploaded_file)
    
    # Extract unique building names from room numbers
    df['ROOM CODE'] = df['ROOM NUMBER'].apply(lambda x: re.match(r'^[A-Z]+', x).group() if re.match(r'^[A-Z]+', x) else '')
    unique_room_codes = df['ROOM CODE'].unique()
    unique_room_codes = ["Select Building name"] + list(unique_room_codes)
    
    # Dropdown to select building name
    room_code = st.selectbox("Select Building Name", unique_room_codes)
    
    if room_code and room_code != "Select Building name":
        # Filter room numbers based on selected building name
        filtered_room_numbers = df[df['ROOM CODE'] == room_code]['ROOM NUMBER'].unique()
        filtered_room_numbers = ["Select Room Number"] + list(filtered_room_numbers)
        
        # Dropdown to select room number
        room_number = st.selectbox("Select Room Number", filtered_room_numbers)
        
        if room_number and room_number != "Select Room Number":
            # Display courses for the selected room number
            filtered_df = df[df["ROOM NUMBER"] == room_number]
            st.write(f"### Courses in Room {room_number}")
            sorted_df = filtered_df[['SLOT', 'COURSE CODE', 'COURSE TITLE', 'EMPLOYEE NAME']].sort_values(by='SLOT')
            
            # Convert DataFrame to HTML table without index
            st.write(sorted_df.to_html(index=False), unsafe_allow_html=True)

    # Adding some styling for better UI
    st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    select {
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.write("Please upload an Excel file to proceed.")
