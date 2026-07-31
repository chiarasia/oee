class Formatter:

    @staticmethod
    def percent(value):
        return f"{value:.2f}%"

    @staticmethod
    def line(title, value):
        return f"{title:<20}{Formatter.percent(value)}"

    @staticmethod
    def separator():
        return "-" * 40
