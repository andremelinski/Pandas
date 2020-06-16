import calendar
import datetime
import pandas as pd
import numpy
import random

columns=['ID', 'Quantity Ordered', 'Product', 'Price', 'Date']

#Product: [Price, weights]
products={
	'Veg':[20.50,2], 
	'Bacon Hamb':[26.90, 5], 
	'Classic Hamb':[22.90, 8], 
	'Doble slim Hamb':[27.90, 7], 
	'Doble Hamb':[31.90, 5],
	'Heart attack Hamb':[31.90, 2],
	'Monster Hamb':[50.90, 1],
	'Junior Hamb':[17.90, 6],
	'Junior Hamb Plus':[19.90, 7],
	'Tijuana Hamb':[30.90, 3]
}

#Second Step:
#Function for random Date
def random_day(month):
	day_range = calendar.monthrange(2020,month)[1]
	return random.randint(1,day_range)

def random_date(month):
	day= random_day(month)
	date = datetime.datetime(2020, month, day,20,0)
	time_offset = numpy.random.normal(loc=0.0, scale=60)
	final_date = date + datetime.timedelta(minutes=time_offset)
	return final_date.strftime("%d/%m/%Y %H:%M") #date syle


#Third pass: generate random requests

def write_row(order_id, product, order_date):
	product_price = products[product][0]
	quantity = numpy.random.geometric(p=1.0-(1.0/product_price), size=1)[0]
	output = [order_id, product, quantity, product_price, order_date]
	return output


#Frist step: 
#Definning numbers of rows for each month 

order_id=1
for month in range (1,13):
	if 1 >= month<=3:
		orders_amount= int(numpy.random.normal(15000, scale=1000))

	elif month==11:
		orders_amount = int(numpy.random.normal(2000, scale=1700))

	elif month==12:
		orders_amount = int(numpy.random.normal(22000, scale=1700))

	else:
		orders_amount = int(numpy.random.normal(17000, scale=1200))

	product_list = [product for product in products]
	weights = [products[product][1] for product in products]
	df=pd.DataFrame(columns=columns)

	i=0
	while orders_amount>0:

		order_date=random_date(month)
		product_choice=random.choices(product_list,weights)[0]
		
		df.loc[i] = write_row(order_id, product_choice, order_date)
		i+=1
		#If there weren't more than 1 order, it would be this:
	 	#df.loc[i]=[order_id, product, 1, price, date]

	 	#Last pass: add some conditionals to orders

		if product_choice=='Classic Hamb':
			if random.random()<0.15:
	 			df.loc[i]= write_row(order_id, 'Doble Hamb', order_date)
	 			i+=1

			if random.random()<0.05:
	 			df.loc[i]= write_row(order_id, 'Doble slim Hamb', order_date)
	 			i+=1

			if random.random()<0.07:
	 			df.loc[i]= write_row(order_id, 'Veg', order_date)
	 			i+=1

		elif product_choice=='Junior Hamb' or product_choice=='Junior Hamb Plus':
	 		if random.random()<0.018:
	 			df.loc[i]= write_row(order_id, 'Bacon Hamb', order_date)
	 			i+=1

	 		if random.random()<0.07:
	 			df.loc[i]= write_row(order_id, 'Tijuana Hamb', order_date)
	 			i+=1

		if random.random()<0.02:
	 		product_choice=random.choices(product_list, weights=weights)[0]
	 		df.loc[i]= write_row(order_id, 'Doble Hamb', order_date)

		if random.random()<0.002:
			df.loc[i]=columns
			i+=1

		if random.random()<0.001:
			df.loc[i]= [order_id, None, None, None, order_date]
			i+=1

		order_id+=1
		orders_amount -=1

#Frist step: 
#Generate csv file
	month_name = calendar.month_name[month]
	df.to_csv(f'Sales_{month_name}_2020.csv', index=False)
	print(f'{month_name} Complete')











