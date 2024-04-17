import streamlit
from twilio.rest import Client
from another_api import *


account_sid = "ACe0ab16dbb0b431253ade224d7b338c7e"
auth_token = "bd081e57c29690b3bb3162b2a2e540ba"
client = Client(account_sid, auth_token) 
TWILIO_PHONE_NUMBER='+14155238886'
twilio_phone_number = '+14155238886'

def run_chat_bot(msg):
    handle_incoming_messages(msg)
  
    
  

def main():
    streamlit.set_page_config(page_title="Whatsapp Bot")
    streamlit.title("QOUTES MACHINE")
    messages = client.messages.list(to=twilio_phone_number)
   
    run_chat_bot(messages)


main()
