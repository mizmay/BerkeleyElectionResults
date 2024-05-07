
# First row describes the race - this will be title of text file
title = s.row_values(0)
t = ''.join(title)
t = str(re.sub('\s','',t))

# Second row is headers
headers = s.row_values(1)
headers[0] = 'VoteType'
headers.insert(0,'Precinct')
h = ','.join(headers)
h = str(re.sub('\n','',h))

# Create the file and write the headers
fname = t +'.csv'
f = open(fname, 'w')
f.write(h)
f.write('\n')

# Print the rest of the text file
for row in range(2,s.nrows):
    cellvalue = str(s.cell(row,0).value)
    n = cellvalue.split("\n")
    n = filter(notempty,n)
    Matrix = [[0 for x in xrange(len(n))] for x in xrange(s.ncols+1)]
    for r in range(len(n)):
        m = n[r].split(' - ')
        Matrix[0][r] = m[0]
        Matrix[1][r] = m[1]
    for col in range(1,s.ncols):
        cellvalue = str(s.cell(row,col).value)
        n = cellvalue.split("\n")
        n = filter(notempty,n)
        for r in range(len(n)):
            Matrix[col+1][r] = n[r]
    for r in range(len(n)):
        values = []
        for c in range(s.ncols+1):
            values.append(str(Matrix[c][r]))
        f.write(','.join(values))
        f.write('\n')
f.close()