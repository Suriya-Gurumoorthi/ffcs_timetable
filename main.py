import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_excel("dataset.xlsx")
st.title("Course Information by Room Number")

# Extract unique room codes
df['ROOM CODE'] = df['ROOM NUMBER'].apply(lambda x: x[:3])
unique_room_codes = df['ROOM CODE'].unique()
unique_room_codes = ["Select Building name"] + list(unique_room_codes)
# Dropdown to select room code
room_code = st.selectbox("Select Room Code", unique_room_codes)

if room_code and room_code != "Select Building name":
    # Filter room numbers based on selected room code
    filtered_room_numbers = df[df['ROOM CODE'] == room_code]['ROOM NUMBER'].unique()
    filtered_room_numbers = ["Select Room Number"] + list(filtered_room_numbers)
    
    # Dropdown to select room number
    room_number = st.selectbox("Select Room Number", filtered_room_numbers)
    
    if room_number and room_number != "Select Room Number":
        # Display courses for the selected room number
        filtered_df = df[df["ROOM NUMBER"] == room_number]
        st.write(f"### Courses in Room {room_number}")
        sorted_df = filtered_df[['SLOT','COURSE CODE', 'COURSE TITLE','EMPLOYEE NAME','CREDITS']].sort_values(by='SLOT')
        st.table(sorted_df)
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