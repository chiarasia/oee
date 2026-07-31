class QualityCalculator:

    def calculate(self, good_units, total_units):
        if total_units <= 0:
            return 0

        return good_units / total_units
