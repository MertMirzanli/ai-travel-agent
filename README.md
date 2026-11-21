# AI Travel Planning Agent (Recreated Source Code)

A Streamlit + Gemini + LangChain project for personalized travel itineraries and budget estimation.

**Important:** This source code was reconstructed after the original folder was deleted. It is not a byte-for-byte recovery of the original implementation. The Gemini model defaults to `gemini-3.5-flash-lite`; change it in `.env` to a model available to your API account.

## Setup (Windows PowerShell)

1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

5. Copy `.env.example` to `.env` and replace the placeholder with **your own** Gemini API key (Google AI Studio). Do not publish `.env`.
6. Run:

   ```powershell
   streamlit run app.py
   ```

7. Open the local address shown in the terminal (usually http://localhost:8501).

## Project structure

- `app.py`: Streamlit intro screen, form, results, Markdown download, booking links.
- `agent.py`: Gemini/LangChain agent and tool-calling loop.
- `tools.py`: `calculate_travel_budget` tool.
- `links.py`: builds real, pre-filled Google Flights / Booking.com search URLs.
- `requirements.txt`: Python dependencies.
- `.env.example`: API configuration template (no real secrets).

## Booking links

After a plan is generated, the app shows two buttons that open real, live
search results pre-filled with your dates and cities:

- **Google Flights** — real flight search results for your route/dates.
- **Booking.com** — real hotel search results for your destination/dates.

The app does not book or charge anything itself; you review the real options
and complete the purchase yourself, with your own payment details, on those
sites.

## Notes

- Generated itinerary/day-plan text and the budget breakdown are estimates,
  not live bookings or verified rates — only the Google Flights/Booking.com
  links (above) show real, live prices.
- The origin city and travel dates you enter are used as context so the
  model's own flight-cost estimate is realistic for that route and season.
- Gemini API access may be subject to usage limits or model availability.
- The agent prints budget tool calls and results to the terminal for demonstration.
