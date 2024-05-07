
cellvalue = str(s.cell(row,0).value)
n = cellvalue.strip("\n")
n = filter(notempty,n)
Matrix = [[0 for x in xrange(len(n))] for x in xrange(s.ncols)]
for r in range(len(n)):
    Matrix[0][r] = n[r]
for col in range(1,s.ncols):
    cellvalue = str(s.cell(row,col).value)
    n = cellvalue.split("\n")
    n = filter(notempty,n)
    for r in range(len(n)):
        Matrix[col][r] = n[r]
for r in range(len(n)):
    values = []
    for c in range(s.ncols):
        values.append(str(Matrix[c][r]))
    print(','.join(values))
