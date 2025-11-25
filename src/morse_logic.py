DOT_THRESHOLD = 200   # ms
DASH_THRESHOLD = 700  # ms

def classify_press(duration_ms):
    if duration_ms <= 0:
        return None
    if duration_ms <= DOT_THRESHOLD:
        return "."
    if DOT_THRESHOLD < duration_ms <= DASH_THRESHOLD:
        return "-"
    return None
