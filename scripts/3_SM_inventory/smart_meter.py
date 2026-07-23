from dataclasses import dataclass
from datetime import datetime
from typing import Self
@dataclass
class SmartMeter:
    # Instance Variable
    meter_id: str
    serial_number: str
    firmware_version: str
    status: str
    last_ping_time : datetime | None = None

    # Class Variable
    manufacturer = "Landis+Gyr"
    total_meters = 0

    # special method that runs after constructor call
    def __post_init__(self):
        if not self.validate_serial(self.serial_number):
            raise ValueError("Invalid serial Number")
        SmartMeter.total_meters += 1

    # when a function needs only the class not the object
    @classmethod
    def total(cls) -> int:
        return cls.total_meters
    # usage
    # SmartMeter.total()

    # when we need a function that logically belongs to the class but doesnt require cls or object
    @staticmethod
    def validate_serial(serial: str) -> bool:
        return len(serial) == 10 and serial.isalnum()

    # default object
    @classmethod
    # def create_default(cls) -> "SmartMeter":     #if directly written it would be called before class is defined, quotes delay this
    def create_default(cls, meter_id: str) -> Self:
        return cls(
            meter_id = meter_id,
            serial_number = "XXXXXXXXXX",
            firmware_version = "1.0.0",
            status = "Disconnected"
        )

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
        serial_number = "Abc1234567",
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
    meter2 = SmartMeter.create_default("MI685")
    meter2.display()
    meter2.ping()
    print(meter.manufacturer)
    print(SmartMeter.total())