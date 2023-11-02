import re

line = "192.168.0.111 - rj [13/Nov/2022:12:14:56] 'GET HTTP/1.0' 200"

matched = re.search(r"(?P<IP>\d+\.\d+\.\d+\.\d+)", line)

# to search / get the IP
matched = re.search(r"(?P<IP>\d+.\d+\.\d+\.\d+)", line)
# print(matched.group("IP"))
# matched.group("IP")

# to get time
r = r"\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2})\]"
m = re.search(r, line)
# matched.group("Time")

# for time in r:
#     print(m.group("TIME"))
