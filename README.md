# Govee Control Script 🌈💡

## Overview
This Python script allows you to control Govee LED devices using the pygovee library. There are two main files in this repository:

1. `devices.py`: This script retrieves a list of Govee devices connected to your account, providing their MAC addresses and model numbers. It helps you identify the devices you want to control in the `main.py` script.

## Requirements
- Python 3.x
- pygovee library

## Installation
1. Install the required library using the following command:
   ```bash
   pip install pygovee
   

## Usage

1. Run `devices.py` to get a list of your Govee devices and their details.
2. Note the MAC address and model number of the device you want to control.
3. Open `main.py` in a text editor.
4. Replace the placeholder API key (`"API_KEY"`) with your Govee API key.
5. Replace `"MAC_ADDRESS"` and `"MODEL"` with the actual MAC address and model number of your Govee device.
6. Save the changes.
7. Run `main.py` to control your Govee LED device based on the provided options.

**Note:** Make sure to keep your API key private and not share it publicly.


## Commands
- **1:** Turn on the Govee device.
- **2:** Turn off the Govee device.
- **3:** Change the color of the Govee device.
- **4:** Change the brightness of the Govee device.

### Color Options
- **1:** Red
- **2:** Green
- **3:** Blue
- **4:** Yellow
- **5:** Purple
- **6:** Cyan
- **7:** White
- **8:** Orange
- **9:** Pink
- **10:** Custom (Enter a custom color when prompted)

