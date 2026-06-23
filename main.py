import time
import datetime  # 👈 Yeh line sabse upar hona zaroori hai, isse error khatam hoga
from twilio.rest import Client

# 🔑 Apne credentials aur numbers pehle ki tarah yahan daal do
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = '51XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
client = Client(account_sid, auth_token)

twilio_whatsapp_number = 'whatsapp:+141XXXXXXXX'
target_whatsapp_number = 'whatsapp:+91XXXXXXXXX'
birthday_message = "Happy Birthday Bhai! 🎉 God bless you. \n\n- Sent automatically by your brother, Coding Zone Techno! 😎"

print("Automation Start: Raat ke 12 baje ka wait ho raha hai...")

while True:
    now = datetime.datetime.now() # 👈 datetime.datetime.now() use karo agar pure module import kiya hai
    
    # 🎯 Agar exact raat ke 12 baj gaye hain (Hour 0, Minute 0)
    if now.hour == 0 and now.minute == 0: 
        print("\n[!] Exact 12 baj gaye! Message bheja ja raha hai...")
        try:
            message = client.messages.create(
                from_=twilio_whatsapp_number,
                body=birthday_message,
                to=target_whatsapp_number
            )
            print(f"Bhai message chala gaya! Success! SID: {message.sid}")
            break # Message bhejte hi loop band
        except Exception as e:
            print(f"Error aaya bhai: {e}")
            break
    else:
        # ⏳ Agar 12 nahi baje hain, toh sirf wait karo aur terminal par time dikhao
        print(f"Abhi time ho raha hai: {now.strftime('%H:%M:%S')}. 12 baje ka intezaar...", end="\r")
        time.sleep(1)