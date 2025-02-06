import requests
from bs4 import BeautifulSoup

def get_event_data(event_id):
    url = f"https://quatronum.pl/wp-content/themes/quatronum/api/data/events/{event_id}/eventData.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching event {event_id}: {e}")
        return None

def get_free_seats_from_web(event_id):
    url = f"https://quatronum.pl/wydarzenie/?id={event_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        dotted_lists = soup.find_all("div", class_="dotted_list")
        for dotted_list in dotted_lists:
            left_element = dotted_list.find("div", class_="left")
            if left_element and left_element.text.strip() == "Ilość miejsc wolnych:":
                right_element = dotted_list.find("div", class_="right")
                if right_element and right_element.find("b"):
                    free_seats = int(right_element.find("b").text.strip())
                    return free_seats
        print(f"Free seats info not found for event {event_id}")
        return 0
    except requests.exceptions.RequestException as e:
        print(f"Error fetching web data for event {event_id}: {e}")
        return 0
    except ValueError:
        print(f"Error parsing free seats for event {event_id}")
        return 0

def main():
    start_id = 324 # 335 dla lata, 324 dla zimy
    max_attempts = 20 #40 dla lata, 20 dla zimy

    total_seats = 0
    total_used = 0
    total_available = 0
    checked_events = 0
    season = input("Podaj sezon: ")

    for event_id in range(start_id, start_id + max_attempts):
        event_data = get_event_data(event_id)

        if event_data and event_data.get("type") == season and event_data.get("date", "").startswith("2025"):
            free_seats = get_free_seats_from_web(event_id)

            seats_number = event_data.get("seets_number", 0)
            seats_used = event_data.get("seets_used", 0)
            seats_available = event_data.get("seets_availible", 0)

            calculated_seats_used = seats_number - free_seats

            total_seats += seats_number
            total_used += calculated_seats_used
            total_available += free_seats
            checked_events += 1

            print(f"Event {event_id} - Seats: {seats_number}, Used (calculated): {calculated_seats_used}, Available: {free_seats}")

    print("\nSummary:")
    print(f"Total Seats: {total_seats}")
    print(f"Total Used (calculated): {total_used}")
    print(f"Total Available: {total_available}")
    print(f"Checked events: {checked_events}")

main()