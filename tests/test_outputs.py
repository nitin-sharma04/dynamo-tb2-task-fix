import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load():
    assert REPORT_PATH.exists(), "report.json not found at /app/report.json"
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_report_exists():
    """Criterion 1: /app/report.json exists and is valid JSON."""
    data = _load()
    assert isinstance(data, dict), "report.json must be a JSON object"


def test_total_requests():
    """Criterion 2: total_requests equals the exact number of log entries (6)."""
    data = _load()
    assert "total_requests" in data, "key 'total_requests' missing from report.json"
    assert data["total_requests"] == 6, (
        f"expected total_requests=6, got {data['total_requests']}"
    )


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs (3)."""
    data = _load()
    assert "unique_ips" in data, "key 'unique_ips' missing from report.json"
    assert data["unique_ips"] == 3, (
        f"expected unique_ips=3, got {data['unique_ips']}"
    )


def test_top_path():
    """Criterion 4: top_path is the most-requested URL path (/index.html)."""
    data = _load()
    assert "top_path" in data, "key 'top_path' missing from report.json"
    assert data["top_path"] == "/index.html", (
        f"expected top_path='/index.html', got {data['top_path']!r}"
    )
