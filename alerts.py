import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_telegram_alert(product_name, current_stock):
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    message = f"⚠️ ALERTE STOCK : {product_name} est presque en rupture ({current_stock} unités restantes) ! 🛒 À commander d'urgence."
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"✅ Alert sent for {product_name}")
        else:
            print("❌ Failed to send alert")
    except Exception as e:
        print(f"⚠️ Error: {e}")
