from core.oee_calculator import OEECalculator
from core.report_generator import ReportGenerator
from dashboard.console import ConsoleDashboard


def main():
    calculator = OEECalculator()

    result = calculator.calculate()

    dashboard = ConsoleDashboard()
    dashboard.show(result)

    report = ReportGenerator()
    report.save(result)


if __name__ == "__main__":
    main()
