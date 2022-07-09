import time
import serial

ser = serial.Serial(
  port='/dev/ttyS0', # Change this according to connection methods, e.g. /dev/ttyUSB0
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)
counter = 0
plants = 2
while counter < 1:
    print("Gathering data.....")    
    ser.write('hello'.encode('utf-8'))
    if plants != 0:
        print(plants)
        # put a delay here if not reading all bits
        from_pico = ser.read(14)
        decode_pico = from_pico.decode()
        print(decode_pico)
        plants -=1
    else:
        plants = 2
    counter +=1
ser.write(0)

# # empty list to send to database
# sql_list = [
#     75.2
# ]

# # test the input of large file into database
# database(sql_list)

# print to lcd display
# must convert to string prior to this step
# the current LCD can only take a length of 16/line currently spaced
# find a more efficient way to print each line
# lcd(f"Temp: {test} F    Humidity: {humidity}")