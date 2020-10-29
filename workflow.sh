#!/bin/bash 
#does w3m exist ? 
which w3m |grep -i w3m 
if [ $? -eq 0 ]
	then 
		echo w3m does not exist, please install it !
		exit
fi 

# also you need ipython3 installed with stmplib 

#first create the new ip address : 
w3m -dump www.ipchicken.com|grep -B1 Add\ to\ Favorites|grep -v Add >ip.txt 

# then call the python script :
python3 emailFirst.py
