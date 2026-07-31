import matplotlib.pyplot as plt

from config import CHART_WIDTH, CHART_HEIGHT


class DashboardCharts:

    def draw(self, result):
        labels = [
            "Availability",
            "Performance",
            "Quality",
            "OEE"
        ]

        values = [
            result["availability"],
            result["performance"],
            result["quality"],
            result["oee"]
        ]

        plt.figure(figsize=(CHART_WIDTH, CHART_HEIGHT))
        plt.bar(labels, values)

        plt.ylabel("Percent")
        plt.title("OEE Metrics")
        plt.ylim(0, 100)

        plt.tight_layout()
        plt.show()
