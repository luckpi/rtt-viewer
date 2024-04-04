import pylink
import re


def extract_serial_numbers(text):
    pattern = r"Serial No\. (\d+)"
    matches = re.findall(pattern, text)
    return matches


class RTT:
    def __init__(self):
        self.jlink = pylink.JLink()

    def get_jlink_list(self):
        jlink_list = self.jlink.connected_emulators()
        jlink_list_sn = list()
        for i in jlink_list:
            jlink_list_sn.append(extract_serial_numbers(str(i))[0])

        return jlink_list_sn

    def open(self, sn=None):
        self.jlink.open(sn)

    def close(self):
        self.jlink.close()

    def connect(self, device=None, speed="auto"):
        if device is None:
            index = self.jlink._dll.JLINKARM_DEVICE_SelectDialog(0, 0, 0)
            device_param = self.jlink.supported_device(index)
            self.jlink.connect(device_param.name, speed)
        else:
            self.jlink.connect(device, speed)

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
        return "SWD" if self.jlink.tif == pylink.enums.JLinkInterfaces.SWD else "JTAG"

    def is_connected(self):
        return self.jlink.connected()

    def info(self):
        if not self.is_connected():
            return None
        jlink_info = {
            "serial_number": self.jlink.serial_number,
            "speed_info": self.jlink.speed_info,
            "hardware_version": self.jlink.hardware_version,
            "firmware_version": self.jlink.firmware_version,
            "connect_mode": self.connect_get_mode(),
            "dll_version": self.jlink.version,
        }
        return jlink_info

    def jlink_switch_device(self):
        if self.is_connected() == False:
            raise Exception("JLink not connected")

        index = self.jlink._dll.JLINKARM_DEVICE_SelectDialog(0, 0, 0)
        device_param = self.jlink.supported_device(index)
        return device_param.name

    def target_connected(self):
        return self.jlink.target_connected()

    def __del__(self):
        self.close()
