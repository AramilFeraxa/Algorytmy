from playwright.sync_api import sync_playwright
import requests
import pdfplumber
import re
import os
from datetime import datetime

def main():
    total_participants = 0
    turnusy_info = []

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        page.goto('https://wypoczynek.men.gov.pl')

        page.fill('input[name="form[organizerName]"]', 'QUBUS Group Sp. z o.o.')
        page.fill('input[name="form[startDate]"]', '2025-01-13')
        page.fill('input[name="form[endDate]"]', '2025-03-01')

        page.click('button:has-text("Szukaj")')

        page.wait_for_selector('table')

        while True:
            rows = page.query_selector_all('table tr')
            for row in rows:
                cells = row.query_selector_all('td')
                if len(cells) > 3:
                    start_date = cells[0].inner_text().strip()
                    end_date = cells[1].inner_text().strip()
                    city = cells[4].inner_text().strip() 

                    pdf_link_element = row.query_selector('a:has-text("Podgląd")')
                    if pdf_link_element:
                        pdf_url = pdf_link_element.get_attribute('href')
                        if pdf_url:
                            if pdf_url.startswith('/'):
                                pdf_url = 'https://wypoczynek.men.gov.pl' + pdf_url
                            
                            turnusy_info.append({
                                "start_date": start_date,
                                "end_date": end_date,
                                "city": city,
                                "pdf_url": pdf_url
                            })

            next_button = page.query_selector('span.next > a')
            if next_button:
                print("Klikam na 'Następna strona'")
                next_button.click()
                page.wait_for_timeout(2000)
            else:
                break

        turnusy_info.sort(key=lambda x: datetime.strptime(x["start_date"], "%Y-%m-%d"))

        for turnus in turnusy_info:
            pdf_url = turnus["pdf_url"]
            pdf_file_path = f'wypoczynek_{turnusy_info.index(turnus)}.pdf'

            pdf_response = requests.get(pdf_url)

            with open(pdf_file_path, 'wb') as f:
                f.write(pdf_response.content)

            with pdfplumber.open(pdf_file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        matches = re.findall(r'5a\. Łączna liczba uczestników\s*(\d+)', text)
                        if matches:
                            participants = int(matches[0])
                            total_participants += participants
                            print(f"Turnus w miejscowości {turnus['city']} od {turnus['start_date']} do {turnus['end_date']} ma {participants} uczestników.")

            os.remove(pdf_file_path)

        print(f"Suma łącznej liczby uczestników: {total_participants}")

        browser.close()

if __name__ == '__main__':
    main()
