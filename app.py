import pyfirmata2
import time

# 1. Setup the connection
PORT = 'COM3'
board = pyfirmata2.Arduino(PORT)

# 2. Setup the Pins
# 'd' = digital, 9 = pin number, 'p' = pwm (for brightness)
led = board.get_pin('d:9:p')

# 3. Define the Callback Function
def on_pot_change(value):
    """This function runs automatically when the knob moves"""
    if value is not None:
        # Update the LED brightness (0.0 to 1.0)
        led.write(value)
        
# 4. Attach the function to the Analog Pin A0
board.analog[0].register_callback(on_pot_change)
board.analog[0].enable_reporting()

print("Connection Successful! Turn the potentiometer...")

try:
    while True:
        # The script just 'sleeps' while the callback does the work
        board.iterate()
        time.sleep(0.01)
except KeyboardInterrupt:
    led.write(0)
    board.exit()