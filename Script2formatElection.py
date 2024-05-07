#Create one column for inPerson, one for byMail
import sys, re

#fname = sys.argv[1]
fname = r"Z:\Dropbox\BerkeleyElectionResults\Results\CALIFORNIAPROPOSITION 36YES.csv"
newfname = r"Z:\Dropbox\BerkeleyElectionResults\Results\Prop36_37.csv"
f = open(fname,'r')
lines = f.readlines()
f.close()

# REMOVE \n and then stick it on the end
header = lines[0]
headers = header.split(',')
newhead = []
newhead.append(headers[0]) # Precinct
newhead.append(headers[2]) # Registration
for i in range(3,len(headers)):
    headers[i] = re.sub('\W','',headers[i])
    newhead.append('m_' + headers[i]) # mail in
    newhead.append('p_' + headers[i]) # in person
    newhead.append('t_' + headers[i]) # total

f2 = open(newfname,'w')
f2.write(','.join(newhead))
f2.write('\n')

for i in range(1,len(lines),2):
    newline = []
    line1 = lines[i].split(',')
    line2 = lines[i+1].split(',')
    # Deal with quirk in precinct numbering where 9 is appended to small precincts
    if int(line1[0]) > 9000000: line1[0] = str(int(line1[0]) - 9000000)
    # Precinct Num
    newline.append(line1[0]) # Precinct
    newline.append(line1[2]) # Registered voters
    for j in range(3,len(line2)):
        newline.append(line1[j])
        newline.append(line2[j])
        newline.append(str(float(line1[j]) + float(line2[j])))
    line = re.sub('\n','',','.join(newline))
    f2.write(line + '\n')
    
f2.close()
    
    