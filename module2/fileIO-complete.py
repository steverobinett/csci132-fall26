
#part 1
with open('roster.txt', 'w') as f:
   f.write('Alice\n')
   f.write('Bob\n')
   f.write('Carmen\n')
   
# write a list of names to a file using writelines
names = ['Diego\n', 'Mary\n', 'Hans\n']
with open('roster.txt', 'w') as f:
   f.writelines(names)
   
with open('roster.txt', 'a') as f:
   f.write('Grace\n')
   f.write('Frank\n')
   
#Part 2 Reading from a file

#2.1 read into one string
with open('roster.txt', 'r') as f:
   data = f.read()
   print(data)
   
#2.2 read into a list of strings
with open('roster.txt', 'r') as f:
   data = f.readlines()
   print(data)
   print(data[0])
   
#2.3 read line by line
with open('roster.txt', 'r') as f:
   for line in f:
       print(line)
#2.4 read line by line and strip the newline character
with open('roster.txt', 'r') as f:
   for line in f:
       print(line.strip()) 
       
# handle missing file
try:  
   with open('missing.txt', 'r') as f:
       data = f.read()
       print(data)
except FileNotFoundError:
   print('File not found')
   
#exercise 1. write then read a list of names to a file
names = ['Alice\n', 'Bob\n', 'Carmen\n']  
with open('roster.txt', 'w') as f:
   f.writelines(names)
   
with open('roster.txt', 'r') as f:
   data = f.readlines()
   print(data)
   
#exercise 2 - build a list of favorite movies from user input
movies = []
for i in range(3):
   movie = input('Enter a favorite movie: ')
   movies.append(movie + '\n')   
with open('movies.txt', 'w') as f:
   f.writelines(movies) 