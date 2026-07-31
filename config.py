from pathlib import Path

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"

SHIFT_DATA = DATA_DIR / "sample_shift.json"
HISTORY_DATA = DATA_DIR / "history.json"

DECIMAL_PLACES = 2

DEFAULT_SHIFT_HOURS = 8

CHART_WIDTH = 10
CHART_HEIGHT = 5

TITLE = "OEE Calculator Dashboard"
