# to parse an rss xml document and get its root

import xml.etree.ElementTree as ET

tree = ET.parse("feedburner.com_radar_atm.xml")
root = tree.getroot()

print(root)

# you can walk down the tree by
# iterating over the child nodes

for child in root:
    print(child.tag, child.attrib)
