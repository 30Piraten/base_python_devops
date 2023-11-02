import xml.etree.ElementTree as ET

tree = ET.parse("feedburner.com_radar_atm.xml")

root = tree.getroot()

name_space = {
    "default": "http://www.w3.org/2005/Atom"
}  # this isn't valid
authors = root.findall(
    "default:channel/default:item/default:author", name_space)

for author in authors:
    print(author.text)


print(authors)
