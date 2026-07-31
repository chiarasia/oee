from tabulate import tabulate


class ConsoleDashboard:

    def show(self, result):
        rows = [
            ["Availability", f'{result["availability"]}%'],
            ["Performance", f'{result["performance"]}%'],
            ["Quality", f'{result["quality"]}%'],
            ["OEE", f'{result["oee"]}%']
        ]

        print()
        print("=" * 42)
        print("      OEE CALCULATOR DASHBOARD")
        print("=" * 42)
        print(tabulate(rows, headers=["Metric", "Value"]))
        print("=" * 42)
