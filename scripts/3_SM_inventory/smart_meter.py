from dataclasses import dataclass
from datetime import datetime

@dataclass
class SmartMeter:
    meter_id: str
    serial_number: str
    firmware_version: str
    status: str
    last_ping_time : datetime | None = None

    def ping(self) -> None:
        if self.status == "Connected":
            print(f"Meter {self.meter_id} responded successfully")
            self.last_ping_time = datetime.now()
        else:
            print("Ping command unsuccessfull")
    def connect(self) -> None:
        if self.status == "Connected":
            print(f"Meter {self.meter_id} already connected")
        else:
            self.status = "Connected"
            print(f"Meter {self.meter_id} connected")
    def disconnect(self) -> None:
        if self.status == "Disconnected":
            print(f"Meter {self.meter_id} already disconnected")
        else:
            self.status = "Disconnected"
            print(f"Meter {self.meter_id} disconnected")
    def firmware_upgrade(self, new_fw_version : str) -> None:
        self.firmware_version = new_fw_version
        print(f"firmware upgraded to version: {new_fw_version}")
    def display(self) -> None:
        last_ping = self.last_ping_time or "Never"
        display_template = f"""
    =================

    Meter ID  : {self.meter_id}

    Serial    : {self.serial_number}

    Firmware  : {self.firmware_version}

    Status    : {self.status}

    Last Ping : {last_ping}
    =================
    """
        print(display_template)

if __name__ == "__main__":
    meter = SmartMeter(
        meter_id = "MI123",
        serial_number = "Abc123456",
        firmware_version = "1.0.0",
        status = "Connected"
    )

    meter.display()
    meter.disconnect()
    meter.connect()
    meter.firmware_upgrade("2.0.0")
    meter.display()
    meter.ping()
    meter.display()