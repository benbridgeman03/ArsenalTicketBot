import asyncio
from playwright.async_api import async_playwright
from fake_useragent import UserAgent
import requests
from random import randint

email = ""
password = ""
ticket_link = ""
telegramID = ""
apiToken = ""
qty = 2 #amount of tickets wanted

def get_chatID():
    apiURL = f'https://api.telegram.org/bot{apiToken}/getUpdates'
    try:
        response = requests.get(apiURL)
        data = response.json()
        if 'result' in data and len(data['result']) > 0:
            chat_id = data['result'][0]['message']['chat']['id']
            return chat_id
        else:
            return "No chat_id found"
    except Exception as e:
        return f"An error occurred: {e}"

def send_message():
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(apiURL, json={'chat_id': telegramID, 'text': "Tickets Secured!"})
        print(response.text)
    except Exception as e:
        print(e)

async def web_login(page):
    await page.click("#onetrust-accept-btn-handler", timeout=600000)
    await page.fill('#email', email)
    await asyncio.sleep(randint(2, 5))
    await page.fill('#password', password)
    await asyncio.sleep(randint(2, 5))
    await page.click('button[type="submit"]')

async def get_tickets(page):
    await page.click("#onetrust-accept-btn-handler", timeout=100000)
    await asyncio.sleep(1)

    try:
        for i in range(qty - 1):
            await page.click('//button[@class="quantity-switcher__btn--add tickets-quantity_add"]')
    except:
        pass

    await asyncio.sleep(2)

    while True:
        done, _ = await asyncio.wait([
            asyncio.create_task(page.wait_for_selector('//button[@class="choose-areas-results__body--results__items--item"]', timeout=20000)),
            asyncio.create_task(page.wait_for_selector('//div[@class="error-noResultsFound"]', timeout=20000)),
        ], return_when=asyncio.FIRST_COMPLETED)

        first_found = list(done)[0]

        try:
            result = await first_found

            if result and await result.get_attribute("class") == "choose-areas-results__body--results__items--item":
                await result.click()
                await asyncio.sleep(4)

                add_qty = await page.query_selector_all('//button[@class="quantity-switcher__btn--add tickets-quantity_add"]')
                for i in range(0, len(add_qty), 2):
                    await add_qty[i].click()
                    await asyncio.sleep(0.5)

                await page.click('//button[@type="submit"]')
                await asyncio.sleep(2)

                await page.click('//a[@class="header__icon header__icon_basket_filled"]')
                send_message()
                break

            else:
                await page.click('//button[@class="quantity-switcher__btn--add tickets-quantity_add"]')
                await page.click('//button[@class="quantity-switcher__btn--remove tickets-quantity_remove"]')
                await page.wait_for_selector('//div[@class="choose-areas-results__body--results is-loading"]', timeout=2000)

        except Exception as e:
            print("Error during seat selection:", e)

    await asyncio.sleep(600)

async def main():
    get_chatID()
    ua = UserAgent().random
    print("Using UA:", ua)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=ua)
        page = await context.new_page()

        await page.goto(ticket_link)
        await asyncio.sleep(4)

        await web_login(page)

        await get_tickets(page)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
