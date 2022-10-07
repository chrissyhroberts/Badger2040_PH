
# Reduce clock speed to 48MHz
badger2040.system_speed(badger2040.SYSTEM_NORMAL)

import binascii
import badger2040
import badger_os
import machine

import ubinascii
id = machine.unique_id()
serial_bytes = bytes([id[11], id[10] + id[2], id[9], id[8] + id[0], id[7], id[6]])
serial = ubinascii.hexlify(serial_bytes).upper()
serial
