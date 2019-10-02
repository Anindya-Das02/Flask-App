from flask import *
import xml.etree.ElementTree as et
import json

app = Flask(__name__)
app.secret_key = '1234'

order_list = []

tree = et.parse('res_xml.xml')
root = tree.getroot()

@app.route('/')
@app.route('/index')
@app.route('/home')
def indexpage():

	data = root.find('information').find('telephone').text
	return render_template('index.html',phone_no = data)

@app.route('/menu')
def menupage():

	img_src_list = []
	name_list = []
	price_list = []
	rating_list = []
	des_lisk_list = []

	data = root.find('services').find('menu')
	
	for i in data.findall('menuItem'):
		img_src_list.append(i.find('img-src').text) 
		price_list.append(i.find('cost').text)
		name_list.append(i.find('name').text)
		rating_list.append(i.find('rating').text)
		des_lisk_list.append(i.find('description-link').text)

	return render_template('menu.html',img_src_list=img_src_list,name_list=name_list,price_list=price_list,rating_list=rating_list,des_lisk_list=des_lisk_list,zip=zip)


@app.route('/orders',methods=['GET','POST'])
def myorderpage():
	if(request.method == 'POST'):
		food_name = request.form['food_item_name']
		food_price = request.form['food_item_price']
		return render_template('order.html',food_name = food_name,food_price = food_price)
	return "Error occured"

@app.route('/menu/<menuitem>')
def menuitemdetailspage(menuitem):
	data = root.find('services').find('menu')


	for i in data.findall('menuItem'):
		if(i.find('name').text.lower() == menuitem.lower()):
			img_src = i.find('img-src').text
			food_name = i.find('name').text
			cost = i.find('cost').text
			desp = i.find('description').text
			

			return render_template('description.html',img = img_src,food_name = food_name, cost = cost, desp = desp)

	
	return "<h1>item not found!</h1>"

@app.route('/about-us')
def aboutuspage():
	about_us = root.find('information').find('about-us').text
	owner = root.find('information').find('owner').text
	return render_template('about.html',about_us = about_us,owner = owner)


if __name__ == '__main__':
	app.run(debug=True)
