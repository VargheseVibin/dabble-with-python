import xml.etree.ElementTree as ET
import re

tree = ET.parse('movies.xml')
root = tree.getroot()
print(f"root.tag:{root.tag}")
print(f"root.attrib:{root.attrib}")

for child in root:
    print(f"child.tag:{child.tag}")
    print(f"child.attrib:f{child.attrib}")

# All elements in the root tree
print([elem.tag for elem in root.iter()])

# Convert XML to string
# print(ET.tostring(root))

# Get attributes into dict of all "named" elements
for movie in root.iter('movie'):
    print(f"Movie's Attributes:{movie.attrib}")

# Get text of all "named" elements
for description in root.iter('description'):
    # print(f"Description Attributes:{description.attrib}")
    print(f"Description Text:{description.text}")

# XPath based query to navigate tree and query for a value element
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(f"1992 Movie Attributes:{movie.attrib}")

# XPath based query to navigate tree and query for attribute of element
# Just Prints multiple values
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(f"Multiple Format Attributes:{movie.attrib}")
# XPath based query to navigate tree and query for attribute of element
# Prints the parent element of current el
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(f"Multiple Format Attributes:{movie.attrib}")

print('*******************************')

# Edit/Update XML
# Fix the '2' in Back 2 the Future
b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(f"b2tf.attrib:{b2tf.attrib}")
b2tf.attrib["title"] = "Back to the Future"
print(f"b2tf.attrib:{b2tf.attrib}")
# Write to a new XML
tree.write("movies_01.xml")
tree = ET.parse('movies_01.xml')

root = tree.getroot()
for movie in root.iter('movie'):
    print(movie.attrib)

# Edit/Update XML by updating attributes - multiple in this case.
# Display all format attribs and text
print("Attributes Before XML Update")
for format in root.findall("./genre/decade/movie/format"):
    print(f"format.attrib:{format.attrib},\tformat.text:{format.text}")

for format in root.findall("./genre/decade/movie/format"):
    match = re.search(',', format.text)
    if match:
        format.set('multiple','Yes')
    else:
        format.set('multiple','No')
# Write out the tree to the file again
tree.write("movies_02.xml")
tree = ET.parse('movies_02.xml')
# Display all format attribs and text after update
print("Attributes After XML Update")
for format in root.findall("./genre/decade/movie/format"):
    print(f"format.attrib:{format.attrib},\tformat.text:{format.text}")


print('******************************')
tree = ET.parse('movies.xml')
root = tree.getroot()

root = tree.getroot()
# XML Move Elements
# List Decades and Movie Years in them Before Fixing
print("List Decades and Movie Years in them Before Fixing")
for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text)
    print("\n")


# 2000 year movies are s***d up
for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(f"2000_movie.attrib:{movie.attrib}")

# Add new decade to genre - Action
action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, 'decade')
new_dec.attrib["years"] = '2000s'

# Action element with new decade added
print(f"New_Action:{ET.tostring(action)}")

xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)

# List Decades and Movie Years in them After Fixing
print("List Decades and Movie Years in them After Fixing")
for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text)
    print("\n")

#print(ET.tostring(action, encoding='utf8').decode('utf8'))
tree.write("movies_03.xml")
tree = ET.parse('movies_03.xml')
