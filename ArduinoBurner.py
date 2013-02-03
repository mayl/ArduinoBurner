#!/usr/bin/env python

from sh import avrdude
import argparse

"Get Arguments for avrdude"
parser = argparse.ArgumentParser(description="Bun .hex files to arduino with AVRdude.")
parser.add_argument('file', metavar='F', type=str, help='hex file to burn.')
parser.add_argument('--port', dest='port', metavar='P', type=str, help='serial port arduino is connected to.', default='/dev/ttyUSB0')
parser.add_argument('--baud', dest='baud', metavar='B', type=int, help='baudrate to write serial port.', default=57600)
parser.add_argument('--part', dest='part', metavar='p', type=str, help='AVR part on the arduino.', default='m328p')
args = parser.parse_args()

"Build avrdude command"
filearg = "-Uflash:w:"+args.file
avrdude("-p" , args.part , "-b" , str(args.baud) , "-c", "arduino" , "-P" , args.port , "-v", filearg)
