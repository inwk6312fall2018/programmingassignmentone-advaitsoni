"""function to create a list of "access-list" for "global_access" and "fw-management_access_in"""
def access_lst(file_name):
	file=open(file_name)
	lst=[]
	for line in file:
		line=line.strip()
		for i in line.split():
			if i=='global_access' or i=='fw-management_access_in':	#if line contains global-access or fw-management it will add that line to lst
				lst.append(line)
	return lst

print(access_lst('running-config.cfg'))
