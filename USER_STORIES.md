# Product Backlog — User Stories

Customer: **TravelWise** (a small travel agency) — wants an AI assistant that
gives its customers an instant personal itinerary and budget estimate.

Format: `As a <role>, I want <goal>, so that <benefit>.`
Priority uses MoSCoW (Must / Should / Could / Won't). Points use a 1-5 scale
(rough relative effort, not hours). Status reflects the real board as of
today (25 Nov 2026).

---

## Epic 1 — Core Trip Planning (Sprint 1–2)

### US-1: Create a trip request
As a **traveler**, I want to enter my destination, trip duration, budget,
interests and travel style, so that the AI can generate a plan personalized
to me.

- **Acceptance criteria**
  - Form has: destination, trip duration (1–30 days), total budget, currency,
    interests (multi-select), travel style (Budget / Balanced / Luxury).
  - Submitting with an empty destination shows a validation error and does
    not call the AI.
  - Submitting a valid form returns a day-by-day itinerary.
- **Priority:** Must · **Points:** 5 · **Sprint:** 1 · **Status:** ✅ Done
- **Linked issues:** #1, #2

### US-2: Get a practical, usable itinerary
As a **traveler**, I want the itinerary to include concrete activities,
food recommendations and practical tips for each day, so that I can follow
it without doing extra research myself.

- **Acceptance criteria**
  - Each day lists specific activities and at least one food recommendation.
  - Plan includes a general "practical tips" section (transport, timing,
    etc.).
- **Priority:** Must · **Points:** 3 · **Sprint:** 1 · **Status:** ✅ Done
- **Linked issues:** #2

### US-3: See a itemized cost breakdown
As a **traveler**, I want to see my trip's cost broken down by category
(accommodation, food, transport, attractions, other), so that I understand
where my money goes instead of seeing one lump estimate.

- **Acceptance criteria**
  - Budget table shows all 5 categories, their subtotal, the total, and the
    remaining budget.
  - The underlying calculation never accepts negative costs or a negative
    total budget (returns an explicit error instead).
- **Priority:** Must · **Points:** 5 · **Sprint:** 2 · **Status:** ✅ Done
- **Linked issues:** #18

### US-4: Know when my budget isn't enough
As a **traveler**, I want to be told clearly when my budget is insufficient
for the trip I asked for, so that I can adjust my expectations instead of
getting a plan I can't actually afford.

- **Acceptance criteria**
  - When remaining budget is negative, the plan explicitly says the budget
    is insufficient and explains why (in the same response, not a separate
    error).
- **Priority:** Should · **Points:** 2 · **Sprint:** 2 · **Status:** ✅ Done
- **Linked issues:** #18, #19

### US-5 (technical): Correctly parse the model's response
As a **developer**, I want the agent's text output parsed correctly no
matter what format the model returns (plain string or a list of content
blocks), so that the UI never shows raw Python data instead of readable
text.

- **Acceptance criteria**
  - A helper converts both string and list-of-blocks model responses into
    plain Markdown text before display.
  - Tested against at least one model that returns each format.
- **Priority:** Must · **Points:** 3 · **Sprint:** 2 · **Status:** ✅ Done
- **Linked issues:** #19

### US-6: Download my plan
As a **traveler**, I want to download my generated plan as a file, so that
I can keep or share it without needing the app open.

- **Acceptance criteria**
  - A "Download Plan (.md)" button saves the itinerary as a Markdown file.
- **Priority:** Could · **Points:** 1 · **Sprint:** 1 · **Status:** ✅ Done
- **Linked issues:** #1

---

## Epic 2 — Reliability (Sprint 3)

### US-7: Keep working when the AI provider has issues
As a **traveler**, I want the app to stay usable even if the underlying AI
model is unavailable, deprecated, or rate-limited, so that I don't just see
a crash with no explanation.

- **Acceptance criteria**
  - API/quota/model errors are caught and shown as a clear, friendly message
    (not a raw stack trace).
  - The AI model used is configurable via an environment variable, so it
    can be swapped without a code change.
- **Priority:** Must · **Points:** 5 · **Sprint:** 3 · **Status:** ✅ Done

### US-8: Get a helpful hint when something goes wrong
As a **traveler**, I want a hint about what to check (API key, model access,
usage quota) when plan generation fails, so that I'm not stuck guessing.

- **Acceptance criteria**
  - On failure, the app shows a one-line hint pointing at the most likely
    causes.
- **Priority:** Should · **Points:** 2 · **Sprint:** 3 · **Status:** ✅ Done

---

## Epic 3 — Real Booking Links (Sprint 4)

### US-9: Find real flights for my trip
As a **traveler**, I want a direct link to real, live flight search results
for my exact route and dates, so that I can check actual prices without
leaving the app or retyping my trip details.

- **Acceptance criteria**
  - A "Search flights on Google Flights" button opens a pre-filled search
    with the traveler's origin, destination and dates.
  - Clicking it returns real, live results (not placeholder data).
- **Priority:** Must · **Points:** 5 · **Sprint:** 4 · **Status:** ✅ Done

### US-10: Find real hotels for my trip
As a **traveler**, I want a direct link to real hotel search results for my
destination and dates, so that I can compare and book accommodation myself.

- **Acceptance criteria**
  - A "Search hotels on Booking.com" button opens a pre-filled search with
    the traveler's destination and check-in/check-out dates.
- **Priority:** Must · **Points:** 3 · **Sprint:** 4 · **Status:** ✅ Done

### US-11: Understand that booking happens on the provider's site
As a **traveler**, I want it to be clear that this app does not book or
charge anything itself, so that I know exactly where I'll enter my payment
details and who is responsible for the booking.

- **Acceptance criteria**
  - The booking section's copy explicitly states the app does not book or
    charge anything; the traveler completes the purchase on the provider's
    own site.
- **Priority:** Should · **Points:** 1 · **Sprint:** 4 · **Status:** ✅ Done

---

## Epic 4 — Delivery & Documentation (Sprint 5)

### US-12: Get the project running on my own machine
As a **new contributor**, I want clear setup instructions and a documented
project structure, so that I can install and run the app without asking
someone else for help.

- **Acceptance criteria**
  - README covers: prerequisites, virtual environment setup, dependency
    install, `.env` configuration, run command, and a project structure
    overview.
- **Priority:** Should · **Points:** 2 · **Sprint:** 5 · **Status:** ✅ Done

---

## Backlog — not yet scheduled (post-Sprint-5)

These are known, deliberately out of scope for Sprints 1–5:

- **US-13:** As a developer, I want the agent's tools exposed over MCP
  instead of being bound directly in-process, so that other MCP-compatible
  clients could reuse them. *(Won't — this sprint cycle)*
- **US-14:** As a traveler, I want the budget breakdown itself to use real,
  live prices (not the model's trained-in estimate), so that the numbers
  are verified, not just plausible. *(Won't — this sprint cycle)*
- **US-15:** As a traveler, I want a more polished, modern interface.
  *(Won't — this sprint cycle)*
- **US-16:** As a traveler, I want to reach the app on a permanent public
  URL rather than a developer's local machine. *(Partially delivered via a
  Streamlit Community Cloud deployment; a fuller production deployment
  remains backlog.)*

---

*Maintained by Mert Mirzanlı (Product Owner / Scrum Master role) on behalf
of the team. Updated as of Sprint 2, 25 Nov 2026.*
