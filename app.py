import streamlit as st
import datetime

# Sample movie data
movies = {
    "Inception": ["10:00 AM", "1:00 PM", "5:00 PM"],
    "Interstellar": ["11:00 AM", "3:00 PM", "7:00 PM"],
    "Dune": ["9:00 AM", "12:00 PM", "6:00 PM"]
}

st.title("🎬 Movie Booking Assistant")

# Select movie
movie = st.selectbox("Choose a movie:", list(movies.keys()))

# Select date
date = st.date_input("Select a date", datetime.date.today())

# Select showtime
showtime = st.selectbox("Select a time:", movies[movie])

# Select number of tickets
num_tickets = st.slider("Number of tickets", 1, 10)

# Dummy seat availability check
available_seats = 50  # Mock value
if num_tickets <= available_seats:
    if st.button("Book Now"):
        st.success(f"✅ Booking confirmed for {movie} on {date} at {showtime} for {num_tickets} tickets.")
else:
    st.error("❌ Not enough seats available.")
