import re

# match for IP
regex = r"(?P<IP>\d+.\d+\.\d+\.\d+)"

# match for User - string
regex += r" - (?P<User>\w+)"

# match for Time
regex += r"\[(?P<Time>08/Nov/\d{4}:\d{2}:\d{2}:\d{2} [- +]\d{4})\]"

# match for Request
regex += r" (?P<Request>'GET .+')"

# using the findinter() to iterate through
# the access log and print out the result of
# the matching line:
log = "access_log.txt"
matched = re.finditer(regex, log)

for m in matched:
    print(m.group("User"))
