class PerformanceCalculator:

    def calculate(
        self,
        ideal_cycle_time,
        total_units,
        operating_minutes
    ):
        if operating_minutes <= 0:
            return 0

        ideal_output = operating_minutes / ideal_cycle_time

        if ideal_output <= 0:
            return 0

        performance = total_units / ideal_output

        return min(performance, 1.0)
