#   1.)
with open('file_assignment.txt','w') as f:
    f.write('Hi I am Sai Sindhu.\n')

#A file with fassignment.txt is created and data is stored in that file 

#   2.)
with open('file_assignment.txt','a') as f:
    f.write('I am currently in capgemini training.\n')

# Data is appended into the file of fassignment.txt


import os
print(os.path.abspath('file_assignment.txt'))

#C:\Users\saisi\OneDrive\Desktop\Python_Capgemini\fassignment.txt


with open('file_assignment.txt','r',encoding='utf-8') as f:
    lines= f.readlines()
    print(lines)

#['Hi I am Sai Sindhu.\n', 'I am currently in capgemini training.\n']

with open('file_assignment.txt','r',encoding='utf-8') as f:
    lines= f.readline()
    print(lines)

#Hi I am Sai Sindhu.