# Christmas Lights Simulation

This repository contains a simple script to simulate a string of blinking Christmas lights in the terminal. It uses ANSI escape codes to cycle through festive colors for each "light bulb."

## Requirements

- Python 3.x
- A terminal that supports ANSI escape codes

## Installation

1. Clone this repository or download the script file.
2. (Optional) Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   # On macOS / Linux
   source venv/bin/activate
   # On Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   # On Windows (cmd)
   venv\Scripts\activate.bat
   ```

3. Install any necessary dependencies (if applicable). For this script, Python's standard library is sufficient.

## Usage

1. Open a terminal or command prompt in the same directory as the `christmas_lights.py` script.
2. Run:

   ```bash
   python christmas_lights.py
   ```

3. You will see a string of colored "o" characters representing light bulbs, cycling through different ANSI colors.
4. Press Ctrl + C to stop the simulation.

## Customization

- **Number of Lights:** You can pass a new value to the `num_lights` parameter in the `print_christmas_lights` function call to change how many bulbs appear.
- **Blink Delay:** Adjust the `delay` parameter to make the lights switch colors faster or slower.

## Example

Run:

```bash
python christmas_lights.py
```

Sample output (the actual colors will be more vivid in a compatible terminal):

```
Press Ctrl+C to stop the lights.
o o o o o o o o o o o o o o o
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any ideas for improvements or additional features.

## License

This project is provided under the MIT License. See the LICENSE file for more information.
