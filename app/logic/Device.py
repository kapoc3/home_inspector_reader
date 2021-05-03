import socket
import struct


class DeviceLogic:
    @classmethod
    def get_default_gateway_linux(cls):
        """Read the default gateway directly from /proc."""
        with open("/proc/net/route") as fh:
            for line in fh:
                fields = line.strip().split()
                if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                    # If not default route or not RTF_GATEWAY, skip it
                    continue

                return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
