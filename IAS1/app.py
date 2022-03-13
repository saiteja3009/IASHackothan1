import sensor_binder

def read_data():
	i = input("Read from sensor: ")
	if i in ["1", "2", "3"]:
		print(sensor_binder.getsensor(i))
	else:
		print("No such sensor")
		

while 1:
	read_data()

