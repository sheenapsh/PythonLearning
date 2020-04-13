# Heading1
Step 1: open cidr.txt
step 2: read line by line
 - if line == "#>Bangalore-cidr" or line == "#>France IPs"
     store all ips into a list until the line == #<Bangalore-cidr
req o/p : {
  "Bangalore": ['172.15.250.0/24', 108.6172.22.80/28,......],
  "France": ['172.59.251.0/29', .....],
  "Sheena": {'Age': 34, 'DOB': '', }
 
}

The first thing you’ll need to do is use Python’s built-in open function to get a file object.
the mode attribute of a file object tells you which mode a file was opened in. And the name attribute tells you the name of the 
file that the file object has opened.

https://realpython.com/read-write-files-python/

cp1252 python file encoding - to be searched
Python List Manipulations - to be searched
https://www.pythonforbeginners.com/basics/python-list-manipulation
https://towardsdatascience.com/python-basics-6-lists-and-list-manipulation-a56be62b1f95



File Seek - https://www.youtube.com/watch?v=SEURXzTgvKI - watch this

##Output Format
```
cidr_dict = {
 "Bangalore-cidr": ['172.15.250.0/24',
   '108.6172.22.80/28',
   '192.148.72.0/23',....],
 "France IPs": [
   ....
 ],
}
```

print(cidr_dict['Bangalore-cidr'])