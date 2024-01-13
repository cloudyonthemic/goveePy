from pygovee import Govee

# Replace the following line with your Govee API key
api_key = "API_KEY"
client = Govee.GoveeClient(apiKey=api_key)
client.login()
# get devices
devices = client.get_device_list()
# print devices
print(devices)