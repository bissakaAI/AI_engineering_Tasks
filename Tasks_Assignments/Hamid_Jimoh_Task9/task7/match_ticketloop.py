import streamlit as st

st.title("🎟️ Football Match Ticket Booking System")

# initialize session state for seats 
if "seat_numbers" not in st.session_state:
    st.session_state.seat_numbers = set(range(1, 51))  # seats 1–50
if "booked" not in st.session_state:
    st.session_state.booked = []

# Display available seats
st.write(f"Available seats: {len(st.session_state.seat_numbers)}")
st.write(sorted(st.session_state.seat_numbers))

# User selects a seat 
selected_seat = st.number_input(
    "Please enter the seat number you want to book (1-50):",
    min_value=1,
    max_value=50,
    step=1,
)

# --- Booking button ---
if st.button("Book Seat"):
    try:
        if not st.session_state.seat_numbers:
            st.error("🚨 All seats are booked. No seat available.")
        elif selected_seat in st.session_state.booked:
            st.error("❌ This seat has already been reserved by someone else.")
        elif selected_seat not in st.session_state.seat_numbers:
            st.error("⚠️ Invalid seat number or already booked.")
        else:
            st.session_state.seat_numbers.remove(selected_seat)
            st.session_state.booked.append(selected_seat)
            st.success(f"✅ Booking confirmed! Seat {selected_seat} has been reserved for you.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")

# --- Show booked seats ---
if st.session_state.booked:
    st.subheader("📌 Booked Seats:")
    st.write(sorted(st.session_state.booked))
