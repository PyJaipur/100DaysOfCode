# A simple android strings value translaString tion script


from googletrans import Translator
import xml.etree.ElementTree as ET

rootForWrittingData = ET.Element("resources")
translator = Translator()

# XML File Reading
base_tree = ET.parse('strings.xml')
nodes = []
root = base_tree.getroot()
for child in root:
    node_name = str(child.attrib['name'])
    tvalue = str(translator.translate([str(child.text)], dest='es')[0].text)
    ET.SubElement(rootForWrittingData, "string", name=node_name).text = tvalue

tree = ET.ElementTree(rootForWrittingData)
tree.write("string-es.xml")