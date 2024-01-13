from pygovee import Govee

# Replace the following line with your Govee API key
api_key = "c25dd77d-3872-431e-bc40-dca439ca88f7"
client = Govee.GoveeClient(apiKey=api_key)
client.login()



inp = input(
    "Welcome to Govee settings. \n 1. Turn on \n 2. Turn off \n 3. Change color \n 4. Change brightness \n"
)

if inp == "1":
    client.device_on("9E:53:A4:C1:38:D5:2C:14", "H6154")
elif inp == "2":
    client.device_off("9E:53:A4:C1:38:D5:2C:14", "H6154")
elif inp == "3":
    color = input(
        "Enter color: \n 1. Red \n 2. Green \n 3. Blue \n 4. Yellow \n 5. Purple \n 6. Cyan \n 7. White \n 8. Orange \n 9. Pink \n 10. Custom \n"
    )
    if color == "1":
        client.change_device_color("9E:53:A4:C1:38:D5:2C:14", "H6154", 255,0,0)
    elif color == "2":
        client.change_device_color("9E:53:A4:C1:38:D5:2C:14", "H6154", 0,255,0)
    elif color == "3":
        client.change_device_color("9E:53:A4:C1:38:D5:2C:14", "H6154", 0,0,255)
    elif color == "4":
        client.change_device_color("9E:53:A4:C1:38:D5:2C:14", "H6154", 255,255,0)
    elif color == "5":
        client.change_device_color("9E:53:A4:C1:38:D5:2C:14", "H6154", 255,0,255)
    elif color == "6":
        client.change_device_color("9E:53:A4:C1:38:D5:2C:14", "H6154", 0,255,255)
    elif color == "7":
        client.change_device_color("9E:53:A4:C1:38:D5:2C:14", "H6154", 255,255,255)
    elif color == "8":
        client.change_device_color("9E:53:A4:C1:38:D5:2C:14", "H6154", 255,165,0)
    elif color == "9":
        client.change_device_color("9E:53:A4:C1:38:D5:2C:14", "H6154", 255,192,203)
    elif color == "10":
        client.change_device_color(
            "9E:53:A4:C1:38:D5:2C:14", "H6154", input("Enter color: ")
        )
