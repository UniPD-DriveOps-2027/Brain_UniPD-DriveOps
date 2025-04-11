import board
import adafruit_bno055
import time

# Initialize I2C and BNO055 sensor
i2c = board.I2C()
bno = adafruit_bno055.BNO055_I2C(i2c)
bno.mode = 0x0C  # NDOF_MODE

def print_sensor_values():
    while True:
        print("\033c")  # Clear screen
        
        # Get and print sensor values
        euler = bno.euler
        accel = bno.acceleration
        gyro = bno.gyro
        
        print("Euler Angles:")
        print(f"Heading: {euler[0]:.2f}")
        print(f"Roll:    {euler[1]:.2f}")
        print(f"Pitch:   {euler[2]:.2f}")
        
        print("\nAcceleration (m/s):")
        print(f"X: {accel[0]:.2f}")
        print(f"Y: {accel[1]:.2f}")
        print(f"Z: {accel[2]:.2f}")
        
        print("\nGyroscope (rad/s):")
        print(f"X: {gyro[0]:.2f}")
        print(f"Y: {gyro[1]:.2f}")
        print(f"Z: {gyro[2]:.2f}")
        
        time.sleep(0.1)

print_sensor_values()
