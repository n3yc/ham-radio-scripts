#!/usr/bin/env python3

# IC-7300-set-frequency.py

# **** BEGIN LICENSE BLOCK ****
#
# This file is part of N3YC Ham Radio Scripts
#
# N3YC Ham Radio Scripts is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# The Original Code is Copyright (C) 2020, Donald R Anderson
# All rights reserved.
#
# SPDX: AGPL-3.0-or-later
#
# **** END LICENSE BLOCK ****/

# =====================================================
# This script sets the current frequency of an IC-7300.
#
# INSTALL PYSERIAL ONCE FROM THE TERMINAL: 
# pip3 install pySerial 
# =====================================================

# IMPORT MODULES
import time
import serial

# THE RADIO AND OUR SCRIPT CI_V ADDRESSES
civ_addr_radio = 0x94  # default
civ_addr_us = 0xE0 # default

# CONNECTION SETTINGS
baudrate = 57600
device = "/dev/tty.SLAB_USBtoUART" # MacOS IC-7300 USB SERIAL PORT

# OPEN THE SERIAL PORT
port = serial.Serial()
port.baudrate = baudrate
port.port = device
port.timeout = 1
port.open()


# CLOSE THE SERIAL PORT
port.close()
