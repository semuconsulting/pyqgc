"""
qgcusage.py

Illustrate basic usage of the pyqgc.QGCMessage and pyqgc.QGCReader classes.

Run from /examples folder

Created on 6 Oct 2025

:author: semuadmin (Steve Smith)
:copyright: semuadmin © 2025
:license: BSD 3-Clause
"""

from serial import Serial

from pyqgc import (
    ERR_LOG,
    GET,
    NMEA_PROTOCOL,
    POLL,
    QGC_PROTOCOL,
    RTCM3_PROTOCOL,
    SET,
    VALCKSUM,
    QGCMessage,
    QGCReader,
)

# create CFG-UART SET (command) message from keyword arguments
# *** remember to set msgmode=SET ***
msg = QGCMessage(
    b"\x02",
    b"\x01",
    msgmode=SET,
    intfid=1,
    intfstatus=1,
    baudrate=921600,
    databit=8,
    parity=0,
    stopbit=1,
)
print(msg)
# send msg.serialize() to receiver

# create INF-VER POLL (query) message from keyword arguments
# *** remember to set msgmode=POLL ***
msg = QGCMessage(
    b"\x06",
    b"\x01",
    msgmode=POLL,
)
print(msg)
# send msg.serialize() to receiver

# create RAW-PPPB2B GET (output) message from keyword arguments
# *** msgmode=GET is the default, so can be omitted here ***
msg1 = QGCMessage(
    b"\x0a",
    b"\xb2",
    parsebitfield=1,
    msgver=1,
    prn=60,
    pppstatus=1,
    msgtype=1,
    msgdata=b"\x10\x35\xfc\x49\x04\x40\x01\x3f\x77\x04\x00\x11\x00\x04\x40\x01\x10\x00\x44\x00\x11\x00\x05\x80\x00\x5f\x6b\x84\x00\x11\x00\x07\x7d\x63\x10\x00\x78\x17\x0f\xfd\xd1\x02\x57\x10\x00\x44\x00\x11\x00\x04\x40\x01\x10\x00\x58\x7f\x00\x01\x81\x36\xb0",
)
print(msg1)
print(msg1.serialize())
print(repr(msg1))

# parse message from bytes
msg2 = QGCReader.parse(msg1.serialize(), validate=VALCKSUM, parsebitfield=1)
print(msg2)
print(str(msg1) == str(msg2))

# parse messages from binary file
with open("pygpsdata_lg580p_qgc.log", "rb") as stream:
    qgr = QGCReader(
        stream,
        msgmode=GET,  # default, normally omitted
        protfilter=NMEA_PROTOCOL | QGC_PROTOCOL | RTCM3_PROTOCOL,
        quitonerror=ERR_LOG,
        validate=VALCKSUM,
        parsebitfield=1,
    )
    msgs = {}
    i = 0
    for raw, parsed in qgr:
        print(parsed)
        i += 1
        msgs[parsed.identity] = msgs.get(parsed.identity, 0) + 1
    print(f"End of file, {i} messages parsed\n{msgs}")

# parse messages from serial port
# PORT = "/dev/tty.usbmodem59320023651"
# BAUD = 460800
# try:
#     with Serial(PORT, BAUD, timeout=3) as stream:
#         qgr = QGCReader(
#             stream,
#             msgmode=GET,
#             protfilter=NMEA_PROTOCOL | QGC_PROTOCOL | RTCM3_PROTOCOL,
#             validate=VALCKSUM,
#             quitonerror=ERR_LOG,
#         )
#         msgs = {}
#         i = 0
#         for raw, parsed in qgr:
#             print(parsed)
#             i += 1
#             msgs[parsed.identity] = msgs.get(parsed.identity, 0) + 1
# except KeyboardInterrupt:
#     print(f"Terminated by user, {i} messages parsed\n{msgs}")
