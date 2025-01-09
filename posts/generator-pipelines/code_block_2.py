import re

def log_lines(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

def filter_errors(lines, error_pattern):
    for line in lines:
        if re.search(error_pattern, line):
            yield line

def extract_timestamps(lines, timestamp_pattern):
    for line in lines:
        match = re.search(timestamp_pattern, line)
        if match:
            yield match.group(1) # Assuming timestamp is the first capture group

def count_errors(timestamps):
  counts = {}
  for timestamp in timestamps:
    counts[timestamp] = counts.get(timestamp, 0) + 1
  return counts # Note: This is not a generator, it returns a dictionary


filepath = "my_log.txt" # Replace with your log file path
error_pattern = r"ERROR: (.*)"
timestamp_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"

error_counts = count_errors(extract_timestamps(filter_errors(log_lines(filepath), error_pattern), timestamp_pattern))
print(error_counts)
