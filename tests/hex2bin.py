"""
Convert hex string examples in protocol specifications to binary file.
"""

INPUT = "/Users/steve/Library/CloudStorage/Dropbox/Development/workspace_vscode/pyqgc/tests/pygpsdata_lu600_qgc_poll.hex"
OUTPUT = "/Users/steve/Library/CloudStorage/Dropbox/Development/workspace_vscode/pyqgc/tests/pygpsdata_lu600_qgc_poll.log"
with open(OUTPUT, "wb") as output:
    with open(INPUT, "r") as input:
        for line in input:
            if line[0:2] == "//":
                continue
            b = bytearray.fromhex(line.replace(" ", "").split("#", 1)[0])
            output.write(b)
