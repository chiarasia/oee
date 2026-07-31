from core.availability import AvailabilityCalculator
from core.performance import PerformanceCalculator
from core.quality import QualityCalculator


class OEECalculator:

    def __init__(self):
        self.availability = AvailabilityCalculator()
        self.performance = PerformanceCalculator()
        self.quality = QualityCalculator()

    def calculate(self):
        availability = self.availability.calculate(
            planned_minutes=480,
            downtime_minutes=28
        )

        performance = self.performance.calculate(
            ideal_cycle_time=1.0,
            total_units=410,
            operating_minutes=452
        )

        quality = self.quality.calculate(
            good_units=401,
            total_units=410
        )

        oee = (
            availability *
            performance *
            quality
        )

        return {
            "availability": round(availability * 100, 2),
            "performance": round(performance * 100, 2),
            "quality": round(quality * 100, 2),
            "oee": round(oee * 100, 2)
        }
