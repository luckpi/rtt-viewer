import pylink
import re


def extract_serial_numbers(text):
    pattern = r'Serial No\. (\d+)'
    matches = re.findall(pattern, text)
    return matches

class RTT:
    def __init__(self):
        self.jlink = pylink.JLink()

    def get_jlink_list(self):
        self.close()
        jlink_list = self.jlink.connected_emulators()
        jlink_list_sn = list()
        for i in jlink_list:
            jlink_list_sn.append(extract_serial_numbers(str(i))[0])

        return jlink_list_sn


    def open(self):
        self.jlink.open()

    def close(self):
        self.jlink.close()

    def connect(self, device):
        self.jlink.supported_device()

    def connect_mode(self, mode: str):
        # 设置连接模式
        if mode not in ["JTAG", "SWD"]:
            raise ValueError("Invalid mode. Mode must be either 'JTAG' or 'SWD'.")
        tif_value = (
            pylink.enums.JLinkInterfaces.SWD
            if mode == "SWD"
            else pylink.enums.JLinkInterfaces.JTAG
        )
        self.jlink.set_tif(tif_value)

    def connect_get_mode(self):
        # 获取当前连接模式
        return (
            "SWD"
            if self.jlink.tif == pylink.enums.JLinkInterfaces.SWD
            else "JTAG"
        )

    def is_connected(self):
        return self.jlink.connected()

    def device_list(self):
        return self.jlink.get_device_index

    def info(self):
        if not self.is_connected():
            return None
        jlink_info = {
            "serial_number": self.jlink.serial_number,
            "speed_info": self.jlink.speed_info,
            "hardware_version": self.jlink.hardware_version,
            "firmware_version": self.jlink.firmware_version,
            "connect_mode": self.connect_get_mode(),
        }
        return jlink_info

    def __del__(self):
        self.close()
