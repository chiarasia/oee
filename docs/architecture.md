# Architecture

```
            app.py
               │
               ▼
       OEECalculator
      ┌──────┼─────────┐
      ▼      ▼         ▼
Availability Performance Quality
      │         │         │
      └─────────┴─────────┘
                │
                ▼
        ReportGenerator
                │
                ▼
      Console Dashboard
                │
                ▼
            Charts
```

## Components

- OEECalculator — combines all OEE metrics.
- AvailabilityCalculator — computes equipment availability.
- PerformanceCalculator — evaluates production speed.
- QualityCalculator — calculates product quality ratio.
- ReportGenerator — saves calculation history.
- ConsoleDashboard — displays metrics in the terminal.
