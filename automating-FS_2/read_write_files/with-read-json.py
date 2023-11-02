import json
from pprint import pprint

file_path = "service-policy.json"

# read policy file
with open(file_path, "r") as read_file:
    policy = json.load(read_file)

# modified policy file
policy["Statement"]["Resources"] = "S3"

# update modified file
with open(file_path, 'w') as read_file:
    policy = json.dump(policy, read_file)

# don't have to print anything
# print(f"File written | updated {policy}")
