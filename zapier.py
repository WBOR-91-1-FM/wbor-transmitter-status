import requests

# Options
#   - Actions: "...turning off the transmitter", "...turning the transmitter back on"
#   - Note: either empty or not

# Sample data provided by Zapier
input_data = {
    "action": "...turning the transmitter back on",
    "note": "",
    "bot_id": "",
}

if input_data["action"] == "...turning off the transmitter":
    action = "turned OFF ❌\n\nListeners will not be able to tune in using their radio."
elif input_data["action"] == "...turning the transmitter back on":
    action = "back ON ✅\n\n91.1 FM is back in action!"

# Defines the message to be sent. If a note is present in the input data, it is included in the message.
message = "Transmitter Status Update: " + action
if "note" in input_data and input_data["note"]:
    message += "\n\nNote provided by technician: \"" + input_data["note"] + "\"\n---------"

url = "https://api.groupme.com/v3/bots/post"
payload = {
    "text": message,
    "bot_id": input_data["bot_id"]
}
response = requests.post(url, json=payload)
print(response)

# Define the output as a dictionary with the key "success" and the value as the status code of the API response.
output = {"success": response.status_code}