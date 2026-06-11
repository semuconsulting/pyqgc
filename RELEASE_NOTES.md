# pyqgc Release Notes

### RELEASE 0.3.0

1. Add support for LG580P v1.3 firmware - additional QTM NAV message types:

    - b"\x08\x01": "NAV-POS",  # output
    - b"\x08\x11": "NAV-VEL",  # output
    - b"\x08\x21": "NAV-TIME",  # output
    - b"\x08\x41": "NAV-NAV",  # output
    - b"\x08\x51": "NAV-EVENTTIME",  # output
    - b"\x08\x52": "NAV-EVENTPOS",  # output
    - b"\x08\x31": "NAV-TAR",  # output
    - b"\x09\x01": "NAV2-POS",  # output
    - b"\x09\x11": "NAV2-VEL",  # output

### RELEASE 0.2.2

1. Fix LU600 CFG-MSG POLL definition.

### RELEASE 0.2.0

1. Minor internal enhancements.

### RELEASE 0.1.2

1. Add support for LU600 IMU GET, SET and POLL QGC message definitions (https://quectel.com/content/uploads/2024/02/Quectel_LUA600A_IMU_Protocol_Specification_V1.0.pdf).

### RELEASE 0.1.1

1. Add support for NMEA and RTCM protocols, selectable via `protfilter` argument, similar to pyubx2 (u-blox) and pysbf2 (Septentrio).

### RELEASE 0.1.0

1. Initial alpha release, covering only LG580P RAW GET QGC message definitions (https://www.quectel.com/download/quectel_lg290p03lgx80p03_gnss_protocol_specification_v1-1/).

