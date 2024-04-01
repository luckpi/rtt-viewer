import re
import ui
import rtt


if __name__ == "__main__":

    rtt = rtt.RTT()
    print(rtt.get_jlink_list())
    rtt.open()
    rtt.connect_mode("SWD")
    print(rtt.info())
    ui._ui()
