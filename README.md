# Arsenal Ticketing Bot

This bot automates the process of reserving tickets on the Arsenal ticketing platform and sends updates via Telegram. Follow the instructions below to configure the script for your use.

## Setup Instructions

1. **Login Details**:
   - Replace the default email and password in the script with your **Arsenal ticketing account** credentials.
   
2. **Ticketing Page**:
   - Set the URL link to the **ticketing page** for the tickets you want to purchase. Ensure it is the correct page.

3. **Telegram Integration**:
   - Configure the bot to send notifications via Telegram:
     - Set your **Telegram Bot API Token** in the script.
     - Add your **Chat ID** to receive notifications.
   - Visit https://core.telegram.org/bots#how-do-i-create-a-bot for more info

## Important Notes

- **Testing**: Run the script in a test mode to ensure all configurations are correct before using it for live ticket purchases.
- **Updates**: Check for updates to the ticketing process or platform, as changes might require script adjustments.
- **Captcha**: The bot cannot pass capture, if there is a queue for the ticket exchange, the bot will not work
- **Paused Browsing**: If Ticketmaster has paused your browsing, close any open browsers, wait a few minuets and try again.

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/benbridgeman03/ArsenalTicketBot
   ```
2. Install Playwright:
   ```bash
   pip install playwright
   install playwright
   ```
3. Install Fake User-Agent
   ```bash
   pip install fake-useragent
   ```
