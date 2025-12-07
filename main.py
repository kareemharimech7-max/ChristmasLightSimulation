import time
import sys

# ANSI escape codes for colors
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m"   # Cyan
]

RESET = "\033[0m"

def print_christmas_lights(num_lights=10, delay=0.5):
    """
    Prints a blinking string of Christmas lights using ANSI color codes.
    :param num_lights: Number of light bulbs to display
    :param delay: Delay in seconds between each blink
    """
    # Create a base pattern of "o" to represent light bulbs
    bulbs = ["o"] * num_lights
    
    color_index = 0
    
    try:
        while True:
            # Clear the line and bring cursor to start
            sys.stdout.write("\r")
            
            # Assign a color to each bulb based on the current color index
            colored_bulbs = []
            for light in bulbs:
                current_color = COLORS[color_index % len(COLORS)]
                colored_bulbs.append(current_color + light + RESET)
                color_index += 1
            
            # Join the colored bulbs into a single string
            lights_str = " ".join(colored_bulbs)
            
            # Display them on the console
            sys.stdout.write(lights_str)
            sys.stdout.flush()
            
            # Wait before switching to next color
            time.sleep(delay)
            
            # Increment the color index so next time they change color
            color_index += 1
    except KeyboardInterrupt:
        # Reset console color when quitting
        print(RESET)

if __name__ == "__main__":
    print("Press Ctrl+C to stop the lights.\n")
    print_christmas_lights(num_lights=15, delay=0.3)