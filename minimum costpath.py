#minimum path
import sys
def minicost(table,m,n):
    if m<0 or n<0:
        return sys.maxsize
    if m==0 and n==0:
        return table[m][n]
    return table[m][n]+min(minicost(table,m-1,n-1),minicost(table,m,n-1),minicost(table,m-1,n))
table=[ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
print(minicost(table,2,2))
