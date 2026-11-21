import streamlit as st

from agent import generate_travel_plan

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
        destination = st.text_input("Destination", placeholder="Tokyo, Japan")
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
        else:
            with st.spinner("Your AI agent is creating a travel plan..."):
                try:
                    st.session_state.plan = generate_travel_plan(
                        destination.strip(), int(days), float(budget), interests,
                        travel_style, currency
                    )
                    st.session_state.destination = destination.strip()
                except Exception as exc:
                    st.error(f"Could not generate the plan: {exc}")

    if st.session_state.get("plan"):
        st.divider()
        st.subheader(f"Your Travel Plan: {st.session_state.get('destination', 'Trip')}")
        st.markdown(st.session_state.plan)
