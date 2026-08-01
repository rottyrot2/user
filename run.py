from playwright.sync_api import sync_playwright
from seleniumbase import sb_cdp
import time
import json
import os

token = os.environ["DISCORD_TOKEN"]


# Step 1: Start SeleniumBase in CDP Stealth Mode
# (SeleniumBase handles patching the browser binary & hiding automation flags)
sb = sb_cdp.Chrome()
endpoint_url = sb.get_endpoint_url()

with sync_playwright() as p:
    # Step 2: Attach Playwright to SeleniumBase's stealth browser session
    browser = p.chromium.connect_over_cdp(endpoint_url)
    context = browser.contexts[0]

    # Step 3: Inject the token automatically before any page or script loads
    # (This prevents "localStorage is undefined" and handles missing keys seamlessly)
    context.add_init_script(f"""
        window.localStorage.setItem("token", '"{token}"');
    """)

    # Step 4: Work inside Playwright using the stealthy page object
    page = context.pages[0]
    
    # Navigate to your target page (the token is already in Local Storage)
    page.goto("https://discord.com/login")
    
    # Wait or perform actions using standard Playwright syntax
    page.wait_for_selector("body")
    print("Page title:", page.title())
    urls = [
        "https://discord.com/channels/979082408152412191/1503659698677743716",
        "https://discord.com/channels/1020441000067485850/1485981338421956718",
        "https://discord.com/channels/1282399408046215168/1533153680952524911",
        "https://discord.com/channels/1282399408046215168/1533033498569347172",
        "https://discord.com/channels/1157480671929970729/1523392522678698106",
        "https://discord.com/channels/1157480671929970729/1523392581050830888",
        "https://discord.com/channels/1157480671929970729/1523392646620516515",
        "https://discord.com/channels/1402794062851084340/1527797029554618388",
        "https://discord.com/channels/1402794062851084340/1527797582108168192",
        "https://discord.com/channels/1402794062851084340/1527797891622768720",
        "https://discord.com/channels/1366027162318147654/1532813755958952136",
        "https://discord.com/channels/1366027162318147654/1532450417219211405",
        "https://discord.com/channels/1334222992020082799/1481697214962077786",
        "https://discord.com/channels/1334222992020082799/1498353214788210688",
        "https://discord.com/channels/1334222992020082799/1515794409541730335",
        "https://discord.com/channels/1276759877943037994/1492541364871893094",
        "https://discord.com/channels/1392232861649600773/1522772690723803279",
        "https://discord.com/channels/1392232861649600773/1520542031112568882",
        "https://discord.com/channels/1392232861649600773/1520532155652902913",
        "https://discord.com/channels/1392232861649600773/1520542139686322248",
        "https://discord.com/channels/1051281232966713354/1525972465044688996",
        "https://discord.com/channels/1051281232966713354/1522240124295843981",
        "https://discord.com/channels/1051281232966713354/1522239365101650020",
        "https://discord.com/channels/1051281232966713354/1527485866354675732",
        "https://discord.com/channels/1303571097438126100/1521589998728642731",
        "https://discord.com/channels/1303571097438126100/1506952539419971616",
        "https://discord.com/channels/1303571097438126100/1478427353360105673",
        "https://discord.com/channels/1106744790655176707/1440102216709968084",
        "https://discord.com/channels/1106744790655176707/1475673278084546611",
        "https://discord.com/channels/1106744790655176707/1521877345831485640",
    ]
    time.sleep(10)

    while True:
        for u in urls:
            time.sleep(3)
            page.goto(u)
            try:
                page.get_by_role("textbox").fill("18f I am new to discord. Text me if you wanna be friends.")
                page.keyboard.press("Enter")
            except:
                pass
            time.sleep(3)
        time.sleep(500)
    
sb.quit()
    
  
