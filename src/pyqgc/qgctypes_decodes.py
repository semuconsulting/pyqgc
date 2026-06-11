"""
qgxtypes_decodes.py

QGC Protocol decodes and enumerations.

Created on 6 Oct 2025

Information sourced from public domain Quectel Interface Specifications © 2026, Quectel

:author: semuadmin (Steve Smith)
"""

TIME_STATUS = {
    0x00: "TIMEINVALID",  # Time invalid
    0x01: "TIMERTC",  # RTC time
    0x02: "TIMESYNC",  # Accurate time which synchronized with satellite.
}
"""Time Status"""

SOL_STATUS = {
    0: "SOL_COMPUTED",  # Solution computed
    1: "INSUFFIENT_OBS",  # Insufficient observations
    2: "NO_CONVERGENCE",  # No convergence
    3: "COV_TRACE",  # Covariance trace exceeds maximum (trace > 1000m)
}
"""NAV-POS Solution Status"""

POS_STATUS = {
    0: "NONE",  # No solution.
    1: "FIXEDPOS",  # Position has been fixed by manual command.
    2: "FIXEDHEIGHT",  # Height has been fixed by manual command.
    8: "DOPPLER_VELOCITY",  # Velocity computed using instantaneous Doppler.
    16: "SINGLE",  # Single point position.
    17: "PSRDIFF",  # Pseudorange differential solution.
    18: "WAAS",  # Solution calculated using corrections from an WAAS.
    32: "L1_FLOAT",  # Floating L1 ambiguity solution.
    33: "IONOFREE_FLOAT",  # Floating ionospheric-free ambiguity solution.
    34: "NARROW_FLOAT",  # Floating narrow-lane ambiguity solution.
    48: "L1_INT",  # Integer L1 ambiguity solution.
    49: "WIDE_INT",  # Integer wide-lane ambiguity solution
    50: "NARROW_INT",  # Integer narrow-lane ambiguity solution
    52: "INS",  # Inertial navigation system only.
    53: "INS_PSRSP",  # INS and single point position.
    54: "INS_PSRDIFF",  # INS and pseudorange differential solution.
    55: "INS_RTKFLOAT",  # INS and RTK float.
    56: "INS_RTKFIXED",  # INS and RTK fixed.
}
"""NAV-POS Position Status"""

POS_QUALITY = {
    0: "NA",
    4: "RTK_FIXED",
    5: "RTK_FLOAT",
}
"""NAV Position Quality"""
