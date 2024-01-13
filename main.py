from pygovee import Govee

# Replace the following line with your Govee API key
api_key = "API_KEY"
client = Govee.GoveeClient(apiKey=api_key)
client.login()

inp = input(
    "Welcome to Govee settings. \n 1. Turn on \n 2. Turn off \n 3. Change color \n 4. Change brightness \n"
)

if inp == "1":
    client.device_on("MAC_ADDRESS", "MODEL")
elif inp == "2":
    client.device_off("MAC_ADDRESS", "MODEL")
elif inp == "3":
    color = input(
        "Enter color: \n 1. Red \n 2. Green \n 3. Blue \n 4. Yellow \n 5. Purple \n 6. Cyan \n 7. White \n 8. Orange \n 9. Pink \n 10. Custom \n"
    )
    if color == "1":
        client.device_set_color("MAC_ADDRESS", "MODEL", "red")
    elif color == "2":
        client.device_set_color("MAC_ADDRESS", "MODEL", "green")
    elif color == "3":
        client.device_set_color("MAC_ADDRESS", "MODEL", "blue")
    elif color == "4":
        client.device_set_color("MAC_ADDRESS", "MODEL", "yellow")
    elif color == "5":
        client.device_set_color("MAC_ADDRESS", "MODEL", "purple")
    elif color == "6":
        client.device_set_color("MAC_ADDRESS", "MODEL", "cyan")
    elif color == "7":
        client.device_set_color("MAC_ADDRESS", "MODEL", "white")
    elif color == "8":
        client.device_set_color("MAC_ADDRESS", "MODEL", "orange")
    elif color == "9":
        client.device_set_color("MAC_ADDRESS", "MODEL", "pink")
    elif color == "10":
        client.device_set_color(
            "MAC_ADDRESS", "MODEL", input("Enter color: ")
        )
