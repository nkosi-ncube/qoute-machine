from twilio.rest import Client
import requests
import datetime

# Twilio credentials

client = Client(account_sid, auth_token) 
TWILIO_PHONE_NUMBER='+14155238886'
twilio_phone_number = '+14155238886'

# AccuWeather API key


# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to fetch and handle incoming messages
def handle_incoming_messages(messages):
    # Fetch incoming messages
   
    
    for message in messages:
        sender_phone_number = message.from_
        message_body = message.body.lower()  # Convert to lowercase for case-insensitive matching
        
        print(f"From: {sender_phone_number}, Body: {message_body}")
        
        # Check if the message body contains "weather forecast"
        if "weather forecast" in message_body:
            # Extract location from the message (you can customize this part based on your message format)
            search_query = "New York"  # Example location
            
            # Fetch weather forecast
            url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={search_query}"
            response = requests.get(url)
            
            if response.status_code == requests.codes.ok:
                data = response.json()
                key = data[0]['Key']
                
                # API endpoint URL for weather forecast
                url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{key}'
                
                # Parameters
                params = {
                    'apikey': api_key,
                    'language': 'en-us',
                    'details': 'true',
                    'metric': 'true'
                }
                
                # Make the request
                weather_response = requests.get(url, params=params)
                
                if weather_response.status_code == 200:
                    data = weather_response.json()
                    
                    # Initialize message content
                    message_content = ""
                    
                    for forecast in data:
                        date_time = datetime.datetime.strptime(forecast['DateTime'], '%Y-%m-%dT%H:%M:%S%z')
                        formatted_date_time = date_time.strftime('%A %d %B %Y : %I:%M%p')
                        chance_of_rain = forecast['RainProbability']
                        
                        # Construct message content
                        message_content += f"DateTime: {formatted_date_time}\n"
                        message_content += f"Temperature: {forecast['Temperature']['Value']} {forecast['Temperature']['Unit']}\n"
                        message_content += f"Condition: {forecast['IconPhrase']}\n"
                        message_content += f"Chance of rain: {chance_of_rain}%\n"
                        message_content += f"Chances of Thunderstorm: {forecast['ThunderstormProbability']}%\n"
                        message_content += f"Link to view detailed info: {forecast['Link']}\n\n"
                    
                    # Send weather info as a reply
                    client.messages.create(
                        body=message_content,
                        from_=twilio_phone_number,
                        to=sender_phone_number
                    )
                    
                else:
                    print(f"Error {weather_response.status_code}: {weather_response.text}")
            if message.lower() in ['hello','hie','hi']:
                client.messages.create(
                        body="Hie am a bot that gives 12 hour hourly forecast and free quotes based on category.\n For weather type Weather forecast for qoutes type qoute and category e.g qoute love",
                        from_=twilio_phone_number,
                        to=sender_phone_number
                    )

            
            else:
                print(f"Error {response.status_code}: {response.text}")

# Example usage
if __name__ == "__main__":
    handle_incoming_messages()
