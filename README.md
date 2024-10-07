# Mouse Clicker to Prevent Kaggle/Colab Notebook Idle Shutdown

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

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/BirhanuShimelis/mouse_clicker.git
    ```

2. Navigate to the project folder:
    ```bash
    cd mouse_clicker
    ```

3. Open the script file (`autoclicker.py`) and adjust the `delay` variable if needed. By default, the script will click every 180 seconds (3 minutes):
    ```python
    delay = 180  # Adjust the delay in seconds if needed
    ```

4. Run the script:
    ```bash
    python autoclicker.py
    ```

5. The script will start clicking the mouse every 3 minutes by default. You can stop the script manually by pressing `Ctrl+C` in the terminal.

## Code Overview

- **delay**: Specifies the time between mouse clicks (in seconds).
- **Controller**: From `pynput`, this is used to control the mouse.
- **ClickMouse class**: A threaded class that handles the clicking functionality in the background.
- **run()**: The main loop that continues to click until the program is manually stopped.
  
## Example

```python
# Example of changing the delay to 120 seconds (2 minutes):
delay = 120
```

## Use Cases

This script is particularly useful for:
- **Preventing idle shutdowns** on cloud-based platforms like Kaggle or Colab during long-running machine learning model training.
- **Keeping the environment active** without manually interacting with the browser or notebook interface.

## Important Notes

- **Kaggle/Colab Restrictions:** Some platforms, such as Kaggle or Google Colab, may have restrictions preventing the use of libraries like `pynput` for controlling input devices. Be sure to check platform-specific restrictions. If `pynput` cannot be used, you may need to consider alternatives, such as keeping the notebook active with periodic outputs.

- **Disclaimer:** Use responsibly. This script is intended for personal use to prevent unintentional idle timeouts during long-running tasks. Avoid using it inappropriately.
