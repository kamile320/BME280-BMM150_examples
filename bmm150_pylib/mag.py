import bmm150
import math
import time


# Template scripts for reading data via bmm150 library.
# Using bmm150 library to read data from BMM150 magnetometer; source: https://pypi.org/project/bmm150/
device = bmm150.BMM150()
k_int  = '\nCancelled [KeyboardInterrupt].'
time_interval = 0.5 # In seconds 


def reading():
    print("\033[H\033[J", end="")

    x, y, z = device.read_mag_data()

    heading_rads    = math.atan2(x, y)
    heading_degrees = math.degrees(heading_rads)
    print(f"X : {x:.2f}µT")
    print(f"Y : {y:.2f}µT")
    print(f"Z : {z:.2f}µT")
    
    print(f"Heading: {heading_degrees:.2f}°")



def live_reading():
    try:
        while True:
            print("\033[H\033[J", end="")

            x, y, z = device.read_mag_data()

            heading_rads    = math.atan2(x, y)
            heading_degrees = math.degrees(heading_rads)
            print(f"X : {x:.2f}µT")
            print(f"Y : {y:.2f}µT")
            print(f"Z : {z:.2f}µT")

            print(f"Heading: {heading_degrees:.2f}°")
            
            time.sleep(time_interval)

    except KeyboardInterrupt:
        print(k_int)
    except Exception as err:
        print(f"Error: {err}")



def track_direction():
    margin = 10     # margin of error in degrees
    try:
        while True:
            x, y, z = device.read_mag_data()
            deg     = math.degrees(math.atan2(x, y))
            dir     = None

            if     0-margin <= deg <= 0+margin:
                dir = "N"
            elif  90-margin <= deg <= 90+margin:
                dir = "E"
            elif -90-margin <= deg <= -90+margin:
                dir = "W"
            elif 180-margin <= deg <= 180+margin or -180-margin <= deg <= -180+margin:
                dir = "S"
            else:
                if      0 <= deg <= 90:
                    dir = "NE"
                elif   90 <= deg <= 180:
                    dir = "SE"
                elif  -90 <= deg <= 0:
                    dir = "NW"
                elif -180 <= deg <= -90:
                    dir = "SW"
                else:
                    dir = "Unknown"

            print(f"\r\033[KDirection: {dir} ({deg:.2f}°)", end="")
            time.sleep(1)

    except KeyboardInterrupt:
        print(k_int)
    except Exception as err:
        print(f"Error: {err}")



while True:
    print("""BMM150 library examples. Make sure you have connected BMM150 magnetometer sensor to bus 1, address 0x13.\n
Select operation:
1. Readings from BMM150 (µT and heading)
2. Live readings from BMM150
3. Looped direction tracking
4. Quit""")
    
    mode = int(input(">>> "))
    if mode == 1:
        reading()
    elif mode == 2:
        live_reading()
    elif mode == 3:
        track_direction()
    elif mode == 4:
        exit()
    else:
        print('Wrong value.')