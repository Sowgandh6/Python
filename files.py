fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('subject: '):
        count = count+1
print('there were', count, 'subject lines in', fname)