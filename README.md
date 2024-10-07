# AutoClicker to Prevent Kaggle/Colab Notebook Idle Shutdown

This Python script automates mouse clicks to prevent cloud-based notebooks (e.g., Kaggle or Google Colab) from becoming idle and shutting down due to inactivity. It simulates periodic mouse clicks while your code is running, ensuring that the environment remains active.

## Features
- **Automatic Mouse Clicking:** The script clicks the left mouse button at a specified interval (default: every 3 minutes).
- **Thread-based Automation:** The script runs in the background without interrupting your main tasks.
- **Easy-to-Use:** No manual interaction needed. The clicking starts automatically when the script is run.
- **Customizable:** You can easily adjust the time between clicks by modifying the `delay` variable.

## Requirements

The script requires the `pynput` library, which allows you to control and monitor input devices such as the mouse.

To install `pynput`, run:

```bash
pip install pynput
```
How to Use

git clone https://github.com/your-username/AutoClicker.git

Navigate to the project folder:

bash

cd AutoClicker

Open the script file (autoclicker.py) and adjust the delay variable if needed. By default, the script will click every 180 seconds (3 minutes):

python

delay = 180  # Adjust the delay in seconds if needed

Run the script:

bash

python autoclicker.py

The script will start clicking the mouse every 3 minutes by default. You can stop the script manually by pressing Ctrl+C in the terminal.
