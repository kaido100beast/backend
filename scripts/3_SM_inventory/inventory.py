from smart_meter import SmartMeter
from dataclasses import dataclass


@dataclass
class MeterInventory:
    meters : dict[str, SmartMeter]

    def add_meter(self, meter: SmartMeter) -> None:
        self.meters[meter.meter_id] = meter
        meter.total_meters += 1

    def remove_meter(self, meter_id: str) -> None:
        try:
            print(f"meter {self.meters.pop(meter_id)} deleted!")
        except KeyError:
            print("Key not found!")

    def find_meter(self, meter_id: str) -> SmartMeter:
            return self.meters.get(meter_id)

    def display_all(self) -> None:
        for meter in self.meters.values():
            meter.display()

    def connected_meters(self) -> list[SmartMeter]:
        connected_meters = []
        for meter in self.meters.values():
            if meter.status == "Connected":
                connected_meters.append(meter)
        return connected_meters