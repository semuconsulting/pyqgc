"""
qgcusage.py

Illustrate basic usage of the pyqgc.QGCMessage and pyqgc.QGCReader classes.

Created on 6 Oct 2025

:author: semuadmin (Steve Smith)
:copyright: semuadmin © 2025
:license: BSD 3-Clause
"""

from pyqgc import ERR_LOG, VALCKSUM, QGCMessage, QGCReader

# create RAW-PPPB2B message from raw msgdata parameters
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

# parse message from binary file
with open("pygpsdata_lg580p_qgc.log", "rb") as stream:
    qgr = QGCReader(stream, quitonerror=ERR_LOG, validate=VALCKSUM, parsebitfield=1)
    for raw, parsed in qgr:
        print(parsed)
