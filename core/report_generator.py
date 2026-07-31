from pathlib import Path
import json
from datetime import datetime

from config import HISTORY_DATA


class ReportGenerator:

    def save(self, result):
        Path(HISTORY_DATA).parent.mkdir(exist_ok=True)

        history = []

        if Path(HISTORY_DATA).exists():
            try:
                with open(HISTORY_DATA, "r") as file:
                    history = json.load(file)
            except Exception:
                history = []

        history.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            **result
        })

        with open(HISTORY_DATA, "w") as file:
            json.dump(history, file, indent=4)
