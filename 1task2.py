"""Write a Python function to create a new configuration file that 
replaces all (sub-)interface IP addresses that start with '172.' and '192." to "10." 
and also change the security-level to "10" . """

def change_ip(file_name):
	file=open(file_name)
	lst=[]
	lst2=[]	#contains all ip address
	lst3=[]	#contains list of elements in ip add
	lst4=[]	#list of updated ip add  
	for line in file:
		line=line.strip()
		for word in line.split():
			lst.append(word)
	for i in range(len(lst)):
		if lst[i-1]!='no' and lst[i]=='ip' and lst[i+1]=='address':
			lst2.append(lst[i+2])	#add all ip add in lst2
	for i in lst2:
		lst3.append(i.split('.'))	#list of elements in ip
	for i in lst3:		#remove '172' or '192' and update with '10'
		i[0]='10'	#update ip add
		lst4.append('.'.join(i))	#add upated ip add in list
	return lst4

print(change_ip('running-config.cfg'))
