__author__ = 'k'

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def print_name():
    print ser.name


def switch1_on():
    ser.write('2')
    return switch1_on


def switch2_on():
    ser.write('3')
    return switch2_on


def switch3_on():
    ser.write('4')
    return switch3_on


def switch4_on():
    ser.write('5')
    return switch4_on


def switch1_off():
    ser.write('11')
    return switch1_off


def switch2_off():
    ser.write('12')
    return switch2_off


def switch3_off():
    ser.write('13')
    return switch3_off


def switch4_off():
    ser.write('14')
    return switch4_off


def switch_on():
    ser.write('0')
    return switch_on


def switch_off():
    ser.write('1')
    return switch_off


def close():
    ser.close()
    print "Connection closed"