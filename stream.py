import streamlit as st
import datetime

# Configure the page
st.set_page_config(
    page_title="Cinema Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #ff4b4b;
        text-align: center;
        margin-bottom: 2rem;
    }
    .movie-card {
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin: 1rem 0;
        background-color: #f9f9f9;
    }
    .booking-summary {
        background-color: #e8f4fd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2196F3;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.markdown('<h1 class="main-header">🎬 Cinema Ticket Booking</h1>', unsafe_allow_html=True)

# Available movies data
movies = {
    "M001": {
        "title": "Avengers: Endgame",
        "genre": "Action/Sci-Fi",
        "duration": "3h 1m",
        "rating": "PG-13",
        "price": 12.99,
        "showtimes": ["14:00", "17:30", "21:00"]
    },
    "M002": {
        "title": "The Lion King",
        "genre": "Animation/Adventure",
        "duration": "1h 58m",
        "rating": "PG",
        "price": 10.99,
        "showtimes": ["13:00", "16:00", "19:00"]
    },
    "M003": {
        "title": "Inception",
        "genre": "Sci-Fi/Thriller",
        "duration": "2h 28m",
        "rating": "PG-13",
        "price": 11.99,
        "showtimes": ["15:00", "18:30", "22:00"]
    }
}

# Sidebar for movie selection
st.sidebar.title("🎯 Quick Booking")
st.sidebar.write("Select a movie to see available showtimes:")

# Movie selection in sidebar
selected_movie_id = st.sidebar.selectbox(
    "Choose a Movie:",
    options=list(movies.keys()),
    format_func=lambda x: f"{movies[x]['title']} ({movies[x]['rating']})"
)

if selected_movie_id:
    movie = movies[selected_movie_id]
    st.sidebar.write(f"**Genre:** {movie['genre']}")
    st.sidebar.write(f"**Duration:** {movie['duration']}")
    st.sidebar.write(f"**Price:** ${movie['price']}")

# Main booking form
st.header("📝 Book Your Tickets")

# Step 1: Movie selection
st.subheader("1. Select Movie")
selected_movie = st.selectbox(
    "Choose your movie:",
    options=list(movies.keys()),
    format_func=lambda x: f"{movies[x]['title']} - {movies[x]['genre']} - ${movies[x]['price']}"
)

if selected_movie:
    movie_info = movies[selected_movie]
    
    # Display movie details
    st.markdown(f"""
    <div class="movie-card">
        <h3>{movie_info['title']}</h3>
        <p><strong>Genre:</strong> {movie_info['genre']} | <strong>Duration:</strong> {movie_info['duration']} | <strong>Rating:</strong> {movie_info['rating']}</p>
        <p><strong>Ticket Price:</strong> ${movie_info['price']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Step 2: Showtime selection
    st.subheader("2. Select Showtime")
    selected_showtime = st.selectbox(
        "Available showtimes:",
        options=movie_info['showtimes']
    )

    # Step 3: Date selection
    st.subheader("3. Select Date")
    selected_date = st.date_input(
        "Choose viewing date:",
        min_value=datetime.date.today(),
        max_value=datetime.date.today() + datetime.timedelta(days=30)
    )

    # Step 4: Ticket quantity
    st.subheader("4. Number of Tickets")
    ticket_quantity = st.number_input(
        "How many tickets?",
        min_value=1,
        max_value=10,
        value=1
    )

    # Step 5: Seat type (optional enhancement)
    st.subheader("5. Seat Type")
    seat_type = st.radio(
        "Choose your seat type:",
        ["Standard", "Premium", "VIP"],
        horizontal=True
    )

    # Price adjustment based on seat type
    seat_prices = {"Standard": 0, "Premium": 3.00, "VIP": 6.00}
    seat_surcharge = seat_prices[seat_type]
    total_price = (movie_info['price'] + seat_surcharge) * ticket_quantity

    # Step 6: Customer information
    st.subheader("6. Your Information")
    col1, col2 = st.columns(2)
    
    with col1:
        customer_name = st.text_input("Full Name:")
        customer_email = st.text_input("Email Address:")
    
    with col2:
        customer_phone = st.text_input("Phone Number:")

    # Booking confirmation
    st.subheader("7. Confirm Booking")
    
    if st.button("🎟️ Book Tickets", type="primary"):
        # Basic validation
        if not all([customer_name, customer_email, customer_phone]):
            st.error("❌ Please fill in all your information!")
        else:
            # Display booking summary
            st.markdown(f"""
            <div class="booking-summary">
                <h3>✅ Booking Confirmed!</h3>
                <p><strong>Movie:</strong> {movie_info['title']}</p>
                <p><strong>Date & Time:</strong> {selected_date} at {selected_showtime}</p>
                <p><strong>Tickets:</strong> {ticket_quantity} x {seat_type} seat</p>
                <p><strong>Total Amount:</strong> ${total_price:.2f}</p>
                <p><strong>Customer:</strong> {customer_name}</p>
                <p><strong>Confirmation will be sent to:</strong> {customer_email}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
            st.success("🎉 Your tickets have been booked successfully! Check your email for confirmation.")

# Additional features in expanders
with st.expander("ℹ️ About Our Cinema"):
    st.write("""
    Welcome to our state-of-the-art cinema! We offer:
    - Comfortable seating with various options
    - Digital projection and Dolby sound
    - Snack bar with refreshments
    - Wheelchair accessible facilities
    """)

with st.expander("📋 Booking Policies"):
    st.write("""
    **Cancellation Policy:**
    - Free cancellation up to 2 hours before showtime
    - 50% refund for cancellations within 2 hours of showtime
    
    **General Policies:**
    - Please arrive 15 minutes before showtime
    - Valid ID required for age-restricted movies
    - Outside food and drinks not permitted
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "© 2024 Cinema Ticket Booking App | For demonstration purposes only"
    "</div>",
    unsafe_allow_html=True
)