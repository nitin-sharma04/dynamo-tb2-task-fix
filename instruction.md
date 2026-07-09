An Apache-style access log is located at `/app/access.log`. Parse it and write a JSON summary report to `/app/report.json`.

The JSON file must contain exactly these keys:

- `total_requests` — integer count of all log lines
- `unique_ips` — integer count of distinct client IP addresses
- `top_path` — string with the URL path that appears most frequently across all requests

Success criteria:

1. `/app/report.json` exists and is valid JSON.
2. `total_requests` equals the exact number of log entries in the file.
3. `unique_ips` equals the exact number of distinct IP addresses in the file.
4. `top_path` equals the URL path with the highest request count.
