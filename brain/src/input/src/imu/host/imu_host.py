import board
import busio
import adafruit_bno055
import time
import mmap
import os

class Mode:
    CONFIG_MODE = 0x00
    ACCONLY_MODE = 0x01
    MAGONLY_MODE = 0x02
    GYRONLY_MODE = 0x03
    ACCMAG_MODE = 0x04
    ACCGYRO_MODE = 0x05
    MAGGYRO_MODE = 0x06
    AMG_MODE = 0x07
    IMUPLUS_MODE = 0x08
    COMPASS_MODE = 0x09
    M4G_MODE = 0x0A
    NDOF_FMC_OFF_MODE = 0x0B
    NDOF_MODE = 0x0C

# Initialize I2C and BNO055 sensor
i2c = board.I2C()
bno = adafruit_bno055.BNO055_I2C(i2c)
bno.mode = Mode.NDOF_MODE

# Define the shared memory file (use /dev/shm for inter-process shared memory)
shm_file = "/dev/shm/imu_shared_memory"

# Create or open a shared memory segment (1024 bytes)
if not os.path.exists(shm_file):
    with open(shm_file, "wb") as f:
        f.write(b'\x00' * 1024)  # Initialize the file with zeros

shm = mmap.mmap(os.open(shm_file, os.O_RDWR), 1024)

def write_to_shared_memory():
    while True:
        euler = bno.euler
        accel = bno.acceleration
        gyro = bno.gyro

        if euler and accel and gyro:
            message = f"{euler[0]},{euler[1]},{euler[2]},{accel[0]},{accel[1]},{accel[2]},{gyro[0]},{gyro[1]},{gyro[2]}"
            msg_bytes = message.encode('utf-8')

        
            shm.seek(0)
            shm.write(b'\x00' * (1024))  # Clear old data
            shm.seek(0)
            shm.write(msg_bytes[:1024])  # Write new data

         

            #print(f"Written to shared memory: {message}")

        time.sleep(0.1)

# Call the function to start writing to shared memory
write_to_shared_memory()
