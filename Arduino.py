__author__ = 'k'

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)


def print_name():
    print ser.name


def switch_on():
    ser.write('0')
    return switch_on


def switch_off():
    ser.write('1')
    return switch_off


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


def switch5_on():
    ser.write('6')
    return switch5_on


def switch6_on():
    ser.write('7')
    return switch6_on


def switch7_on():
    ser.write('8')
    return switch7_on


def switch8_on():
    ser.write('9')
    return switch8_on


def close():
    ser.close()
    print "Connection closed"