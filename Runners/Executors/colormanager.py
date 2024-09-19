from console import Swdconsole_logs

con_logs = Swdconsole_logs()


class colors:
    idle = 0x1abc9c
    error = 0x992d22
    warning = 0xf1c40f

class Swdcolor_picker():
    def __init__(self):
        con_logs.call("Colormanager")

    def get_color(self, color: str):
        if color == "idle":
            ec = colors.idle
        elif color == "error":
            ec = colors.error
        elif color == "warning":
            ec = colors.warning

        return ec