import datetime

import streamlit as st

from agent import generate_travel_plan
from links import booking_hotels_link, google_flights_link

st.set_page_config(page_title="AI Travel Planning Agent", page_icon="✈️", layout="wide")

if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.title("✈️ AI Travel Planning Agent")
    st.write("Your personal AI-powered travel assistant.")
    st.write("Create a customized itinerary with an estimated travel budget.")
    if st.button("Start Planning", type="primary"):
        st.session_state.started = True
        st.rerun()
else:
    st.title("🌍 Plan Your Next Trip")
    if st.button("← Back to Welcome"):
        st.session_state.started = False
        st.rerun()

    with st.form("travel_form"):
        origin = st.text_input("Flying from", placeholder="Istanbul, Turkey")
        destination = st.text_input("Destination", placeholder="Tokyo, Japan")
        start_date = st.date_input(
            "Departure date",
            value=datetime.date.today() + datetime.timedelta(days=30),
            min_value=datetime.date.today(),
        )
        days = st.number_input("Trip duration (days)", min_value=1, max_value=30, value=5)
        budget = st.number_input("Total budget", min_value=1.0, value=600.0, step=50.0)
        currency = st.selectbox("Currency", ["EUR", "USD", "TRY", "GBP"])
        interests = st.multiselect(
            "Your interests",
            ["Food", "Culture", "Shopping", "Nature", "History", "Adventure", "Nightlife", "Art"],
            default=["Food", "Culture", "Shopping"],
        )
        travel_style = st.selectbox("Travel style", ["Budget", "Balanced", "Luxury"])
        submitted = st.form_submit_button("Generate Travel Plan", type="primary")

    if submitted:
        if not destination.strip():
            st.error("Please enter a destination.")
        elif not origin.strip():
            st.error("Please enter your departure city (used for a realistic flight estimate).")
        else:
            with st.spinner("Your AI agent is creating a travel plan..."):
                try:
                    st.session_state.plan = generate_travel_plan(
                        destination.strip(), int(days), float(budget), interests,
                        travel_style, currency, origin.strip(), start_date
                    )
                    st.session_state.destination = destination.strip()
                    st.session_state.origin = origin.strip()
                    st.session_state.start_date = start_date
                    st.session_state.return_date = start_date + datetime.timedelta(days=int(days))
                except Exception as exc:
                    st.error(f"Could not generate the plan: {exc}")
                    st.info("Check your API key, model access, and Gemini usage quota.")

    if st.session_state.get("plan"):
        st.divider()
        st.subheader(f"Your Travel Plan: {st.session_state.get('destination', 'Trip')}")
        st.markdown(st.session_state.plan)
        st.download_button(
            "Download Plan (.md)",
            data=st.session_state.plan,
            file_name="travel_plan.md",
            mime="text/markdown",
        )

        st.divider()
        st.subheader("Book your trip")
        st.caption(
            "These open real, pre-filled search results on Google Flights and Booking.com. "
            "This app does not book or charge anything itself — you review the real options "
            "and complete the purchase yourself, with your own payment details, on their site."
        )
        flights_url = google_flights_link(
            st.session_state.origin, st.session_state.destination,
            st.session_state.start_date, st.session_state.return_date,
        )
        hotels_url = booking_hotels_link(
            st.session_state.destination,
            st.session_state.start_date, st.session_state.return_date,
        )
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("✈️ Search flights on Google Flights", flights_url, use_container_width=True)
        with col2:
            st.link_button("🏨 Search hotels on Booking.com", hotels_url, use_container_width=True)
