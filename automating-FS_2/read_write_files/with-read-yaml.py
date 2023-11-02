import yaml
from pprint import pprint

with open("verify-apache.yml", "r") as opened_file:
    verify_apache = yaml.safe_load(opened_file)

pprint(verify_apache)
