from dataclasses import dataclass

@dataclass
class SmartMeter:
    meter_id: str
    serial_number: str
    firmware_version: str
    status: str