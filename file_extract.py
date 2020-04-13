file_object = open("cidr.txt")
''' print(file_object)
print(dir(file_object)) '''
'''
file_object.readlines read file contents into a list . Each line in the file is converted into a list item
'''
cidr_list = file_object.readlines()
#print(content)
'''
Iterating over the list named content
'''
for cidr in cidr_list: 
    recording = False
    print (cidr)
    banglr_cidr = []
    if cidr == '#>Bangalore-cidr\n':
        recording = True
        print('Hello')
    if recording == True:
        banglr_cidr.append(cidr)
    if cidr == '#<Bangalore-cidr\n':
        recording = False
    print(banglr_cidr)
    




           









