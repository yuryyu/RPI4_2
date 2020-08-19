import csv
import pandas as pd 
from init import *
import sqlite3
from sqlite3 import Error


# Accelerometer, magnetometer, gyroscope.    
def DOF():
    import time
    import board
    import busio
    import adafruit_lsm9ds1
    # I2C connection:
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

    # SPI connection:
    # from digitalio import DigitalInOut, Direction
    # spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    # csag = DigitalInOut(board.D5)
    # csag.direction = Direction.OUTPUT
    # csag.value = True
    # csm = DigitalInOut(board.D6)
    # csm.direction = Direction.OUTPUT
    # csm.value = True
    # sensor = adafruit_lsm9ds1.LSM9DS1_SPI(spi, csag, csm)

    # Main loop will read the acceleration, magnetometer, gyroscope, Temperature
    # values every second and print them out.

    while True:
        # Read acceleration, magnetometer, gyroscope, temperature.
        accel_x, accel_y, accel_z = sensor.acceleration
        mag_x, mag_y, mag_z = sensor.magnetic
        gyro_x, gyro_y, gyro_z = sensor.gyro
        temp = sensor.temperature
        # Print values.
        print(
            "Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
                accel_x, accel_y, accel_z
            )
        )
        print(
            "Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})".format(mag_x, mag_y, mag_z)
        )
        print(
            "Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
                gyro_x, gyro_y, gyro_z
            )
        )
        print("Temperature: {0:0.3f}C".format(temp))
        # Delay for a second.
        time.sleep(1.0/Fs)

def G200():
    pass


#import os
#print(os.getcwd())
# Out: /Users/shane/Documents/blog
# Display all of the files found in your current working directory
#print(os.listdir(os.getcwd())
# read csv
# with open('C:\\Users\\yuzba\\Documents\\GitHub\\RPI4_2\\data\\K544_TLV_20-05-2020_NODE_4191.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         print(row)
#         line_count += 1
#     print(f'Processed {line_count} lines.')


# save csv
# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])    




def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



def acq_data():
    if onboard:
        data = DOF()
    elif db_init:
        data = pd.read_csv("data/data_good.csv")
        data.to_sql(table_name, conn, if_exists='append', index=False)
    else:
        data = pd.read_csv("data/data_good.csv")
    return data 



if __name__ == "__main__":
    create_connection(db_name)
    data = acq_data()
    # Preview the first 5 lines of the loaded data 
    print(data.head())
