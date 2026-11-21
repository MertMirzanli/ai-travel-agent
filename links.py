import datetime
from urllib.parse import quote, urlencode


def google_flights_link(origin: str, destination: str,
                         depart_date: datetime.date, return_date: datetime.date) -> str:
    query = (
        f"Flights to {destination} from {origin} "
        f"on {depart_date.isoformat()} through {return_date.isoformat()}"
    )
    return "https://www.google.com/travel/flights?q=" + quote(query)


def booking_hotels_link(destination: str, check_in: datetime.date, check_out: datetime.date) -> str:
    city = destination.split(",")[0].strip()
    params = {
        "ss": city,
        "checkin": check_in.isoformat(),
        "checkout": check_out.isoformat(),
        "group_adults": "1",
        "no_rooms": "1",
    }
    return "https://www.booking.com/searchresults.html?" + urlencode(params)
