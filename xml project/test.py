import xml.etree.ElementTree as et

tree = et.parse("res_xml.xml")
root = tree.getroot()

data = root.find('services').find('menu')#.findall('menuItem')



for i in data.findall('menuItem'):
	if(i.find('name').text == 'dosa'):
		print('dosa found')
