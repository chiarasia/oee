class AvailabilityCalculator:

    def calculate(self, planned_minutes, downtime_minutes):
        if planned_minutes <= 0:
            return 0

        operating = planned_minutes - downtime_minutes

        if operating < 0:
            operating = 0

        return operating / planned_minutes
