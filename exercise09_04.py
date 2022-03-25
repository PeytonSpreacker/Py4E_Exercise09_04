#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File does not exist:', fname)
    quit()
#create dictionary
counts = dict()
#go through lines
for line in fh:
    if len(line) < 1:
        continue
    if line.startswith('From '):
        linesplit = line.split()
        #isolate email
        email = linesplit[1:2]
#fill in dictionary
    for e in email :
        counts[e] = counts.get(e,0) + 1
#print(counts)
#find the largest value of emails in the dictionary we created and print that email and number of commits completed. Note, this simplified solution would NOT work if there is a tie. It returns the first max encountered and would not register an equal value key that follows it.
maxkey = max(counts, key=counts.get)
maxvalue = max(counts.values())
print(maxkey, maxvalue)