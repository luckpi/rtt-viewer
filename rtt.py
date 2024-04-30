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
        self.jlink.close()
        self.jlink.__init__()
        self.jlink.open(sn)

    def close(self):
        self.jlink.close()

    def connect(self, device=None, speed="auto"):
        """
        device (str): eg: "STM32F103RB"
        speed (str): "auto","adaptive" or "1-12000"(kHz)
        """
        if device is None:
            device = self.switch_device()
        try:
            self.jlink.connect(device, speed)
        except Exception as e:
            print(e)

    def set_connect_port(self, port: str):
        """
        port (str): "JTAG" or "SWD"
        """
        # 设置连接模式
        if port not in ["JTAG", "SWD"]:
            raise ValueError("Invalid port. Mode must be either 'JTAG' or 'SWD'.")
        tif_value = (
            pylink.enums.JLinkInterfaces.SWD  # type: ignore
            if port == "SWD"
            else pylink.enums.JLinkInterfaces.JTAG  # type: ignore
        )
        try:
            self.jlink.set_tif(tif_value)
        except Exception as e:
            print(e)

    def get_connect_port(self):
        return "SWD" if self.jlink.tif == pylink.enums.JLinkInterfaces.SWD else "JTAG"  # type: ignore

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
            "connect_mode": self.get_connect_port(),
            "dll_version": self.jlink.version,
        }
        return jlink_info

    def switch_device(self):
        if self.is_connected() == False:
            print("Please connect JLink first")
            return

        index = self.jlink._dll.JLINKARM_DEVICE_SelectDialog(0, 0, 0)  # type: ignore
        try:
            device_param = self.jlink.supported_device(index)
        except Exception as e:
            print(e)
            return
        return device_param.name

    def target_connected(self):
        state = self.is_connected()
        if state == False:
            return False
        else:
            return self.jlink.target_connected()

    def start(self, buff_addr):
        """
        buff_addr (str) : eg: "0x20000000"
        """
        if buff_addr == "":
            print("Please input buffer address")
            return
        try:
            self.jlink.rtt_start(int(buff_addr, 16))
            print("RTT started")
        except Exception as e:
            print(e)

    def stop(self):
        try:
            self.jlink.rtt_stop()
            print("RTT stopped")
        except Exception as e:
            print(e)

    def read(self, buffer_index, size):
        return self.jlink.rtt_read(buffer_index, size)

    def write(self, buffer_index, data: str):
        bytes_data = list(data.encode("ascii"))
        self.jlink.rtt_write(buffer_index, bytes_data)

    def __del__(self): 
        self.close()
