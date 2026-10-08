import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Prasanna Chowdary - Movie Ticket Booking",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(124, 58, 237, 0.16), transparent 25%),
        radial-gradient(circle at 90% 15%, rgba(236, 72, 153, 0.15), transparent 25%),
        linear-gradient(135deg, #f5f3ff 0%, #ffffff 50%, #fdf2f8 100%);
}

.main-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 4px;
    background: linear-gradient(90deg, #6d28d9, #db2777, #2563eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: titleFloat 2.5s ease-in-out infinite alternate;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 17px;
    margin-bottom: 25px;
}

@keyframes titleFloat {
    from { transform: translateY(0); }
    to { transform: translateY(-5px); }
}

.hero {
    background: linear-gradient(135deg, #7c3aed, #db2777);
    color: white;
    padding: 24px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 12px 30px rgba(124, 58, 237, 0.28);
    animation: heroFloat 3s ease-in-out infinite;
    margin-bottom: 25px;
}

.hero h2 {
    margin: 0;
    font-size: 28px;
}

.hero p {
    margin: 8px 0 0;
    opacity: 0.95;
}

@keyframes heroFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}

.movie-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(124, 58, 237, 0.15);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.07);
    margin-bottom: 18px;
}

.booking-card {
    background: white;
    border-radius: 22px;
    padding: 28px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.10);
    border-top: 7px solid #7c3aed;
}

.total-box {
    background: linear-gradient(90deg, #7c3aed, #db2777);
    color: white;
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    font-size: 29px;
    font-weight: 800;
    margin-top: 18px;
    box-shadow: 0 8px 22px rgba(124,58,237,0.25);
}

.ticket-row {
    background: #f5f3ff;
    border-left: 5px solid #7c3aed;
    border-radius: 10px;
    padding: 11px 15px;
    margin: 8px 0;
}

.footer {
    text-align: center;
    color: #777;
    padding: 20px 0 5px;
    font-size: 14px;
}

div.stButton > button {
    border-radius: 12px;
    border: none;
    font-weight: 700;
    transition: 0.25s;
}

div.stButton > button:hover {
    transform: scale(1.03);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f5f3ff, #fdf2f8);
}

@media (max-width: 768px) {
    .main-title { font-size: 31px; }
    .subtitle { font-size: 14px; }
}
</style>
""", unsafe_allow_html=True)

# -------------------- MOVIE DATA --------------------
MOVIES = {
    "🎬 Pushpa 2: The Rule": 180,
    "🦸 Kalki 2898 AD": 200,
    "🔥 Salaar": 170,
    "🌟 Devara": 190,
    "🎭 Hi Nanna": 160,
    "🚀 Hanuman": 150
}

TICKET_TYPES = {
    "Standard": 0,
    "Premium": 50,
    "VIP": 100
}

SHOW_TIMES = [
    "10:00 AM",
    "01:30 PM",
    "04:30 PM",
    "07:30 PM",
    "10:00 PM"
]

# -------------------- HEADER --------------------
st.markdown(
    '<div class="main-title">Prasanna Chowdary - Movie Ticket Booking System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Book your movie tickets quickly, easily, and beautifully 🎟️</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero">
    <h2>🎬 Welcome to Prasanna's Movie Zone! 🍿</h2>
    <p>Choose a movie, select your show, pick your ticket category and number of tickets.</p>
</div>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.header("🎟️ Booking Details")

    customer_name = st.text_input("👤 Customer Name", value="Guest")

    phone = st.text_input(
        "📱 Mobile Number",
        value="",
        max_chars=10,
        placeholder="Enter 10-digit number"
    )

    st.divider()

    booking_fee = st.number_input(
        "💳 Booking Fee (%)",
        min_value=0.0,
        max_value=30.0,
        value=5.0,
        step=0.5
    )

    st.divider()

    st.info("💡 Select your movie and ticket details, then generate the booking summary.")

# -------------------- MOVIE SELECTION --------------------
st.markdown("### 🎥 Choose Your Movie")

movie_columns = st.columns(3)

for index, (movie, price) in enumerate(MOVIES.items()):
    with movie_columns[index % 3]:
        st.markdown(
            f"""
            <div class="movie-card">
                <h3>{movie}</h3>
                <p>🎟️ Starting from <b>₹{price}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

selected_movie = st.selectbox(
    "🎞️ Select Movie",
    list(MOVIES.keys())
)

base_price = MOVIES[selected_movie]

# -------------------- BOOKING DETAILS --------------------
st.markdown("### 🎟️ Select Ticket Details")

col1, col2, col3 = st.columns(3)

with col1:
    ticket_type = st.selectbox(
        "🏷️ Ticket Category",
        list(TICKET_TYPES.keys())
    )

with col2:
    number_of_tickets = st.number_input(
        "🎟️ Number of Tickets",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

with col3:
    show_time = st.selectbox(
        "🕐 Show Time",
        SHOW_TIMES
    )

# Optional seat preference
seat_preference = st.selectbox(
    "💺 Seat Preference",
    ["Any Available Seat", "Front Rows", "Middle Rows", "Back Rows"]
)

# -------------------- CALCULATION --------------------
ticket_price = base_price + TICKET_TYPES[ticket_type]
ticket_subtotal = ticket_price * number_of_tickets
fee_amount = ticket_subtotal * booking_fee / 100
grand_total = ticket_subtotal + fee_amount

st.markdown("### 📊 Booking Calculation")

c1, c2, c3, c4 = st.columns(4)

c1.metric("🎟️ Tickets", number_of_tickets)
c2.metric("💵 Ticket Price", f"₹{ticket_price:,.2f}")
c3.metric("💳 Booking Fee", f"₹{fee_amount:,.2f}")
c4.metric("💰 Total", f"₹{grand_total:,.2f}")

# -------------------- BOOKING SUMMARY --------------------
st.markdown("### 🧾 Booking Summary")

if st.button("🎟️ Generate Booking Summary", use_container_width=True):
    if not customer_name.strip():
        st.error("Please enter the customer name.")
    elif phone and (not phone.isdigit() or len(phone) != 10):
        st.error("Please enter a valid 10-digit mobile number.")
    else:
        booking_id = "PC" + datetime.now().strftime("%Y%m%d%H%M%S")
        now = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        st.markdown(f"""
        <div class="booking-card">
            <h2 style="text-align:center;">🎬 PRASANNA'S MOVIE ZONE</h2>
            <p style="text-align:center;color:#777;">Movie Ticket Booking Confirmation</p>
            <hr>

            <p><b>Booking ID:</b> {booking_id}</p>
            <p><b>Customer:</b> {customer_name}</p>
            <p><b>Mobile:</b> {phone if phone else "Not Provided"}</p>
            <p><b>Date & Time:</b> {now}</p>

            <hr>

            <div class="ticket-row">
                🎬 <b>Movie:</b> {selected_movie}
            </div>

            <div class="ticket-row">
                🕐 <b>Show Time:</b> {show_time}
            </div>

            <div class="ticket-row">
                🏷️ <b>Ticket Category:</b> {ticket_type}
            </div>

            <div class="ticket-row">
                🎟️ <b>Number of Tickets:</b> {number_of_tickets}
            </div>

            <div class="ticket-row">
                💺 <b>Seat Preference:</b> {seat_preference}
            </div>

            <hr>

            <p style="text-align:right;">
                <b>Base Price:</b> ₹{base_price:,.2f}
            </p>

            <p style="text-align:right;">
                <b>{ticket_type} Upgrade:</b> ₹{TICKET_TYPES[ticket_type]:,.2f}
                per ticket
            </p>

            <p style="text-align:right;">
                <b>Ticket Subtotal:</b> ₹{ticket_subtotal:,.2f}
            </p>

            <p style="text-align:right;">
                <b>Booking Fee ({booking_fee:.1f}%):</b> +₹{fee_amount:,.2f}
            </p>

            <div class="total-box">
                TOTAL PRICE: ₹{grand_total:,.2f}
            </div>

            <p style="text-align:center;margin-top:18px;">
                🍿 Enjoy your movie! 🎬
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.success("✅ Booking summary generated successfully!")
        st.balloons()

        booking_text = f"""PRASANNA'S MOVIE ZONE
Movie Ticket Booking Confirmation

Booking ID: {booking_id}
Customer: {customer_name}
Mobile: {phone if phone else "Not Provided"}
Date & Time: {now}

Movie: {selected_movie}
Show Time: {show_time}
Ticket Category: {ticket_type}
Number of Tickets: {number_of_tickets}
Seat Preference: {seat_preference}

Base Price: ₹{base_price:.2f}
Ticket Price Per Ticket: ₹{ticket_price:.2f}
Ticket Subtotal: ₹{ticket_subtotal:.2f}
Booking Fee ({booking_fee:.1f}%): ₹{fee_amount:.2f}

TOTAL PRICE: ₹{grand_total:.2f}

Thank you for booking with Prasanna's Movie Zone!
"""

        st.download_button(
            "📥 Download Booking Summary",
            data=booking_text,
            file_name="prasanna_chowdary_movie_booking.txt",
            mime="text/plain",
            use_container_width=True
        )

st.markdown("""
<div class="footer">
    🚀 Built with Python + Streamlit | Prasanna Chowdary | Movie Ticket Booking Project
</div>
""", unsafe_allow_html=True)
