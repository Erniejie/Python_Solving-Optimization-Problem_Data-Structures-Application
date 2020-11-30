# DATA STRUCTURES-Practical application -Solving Optimization Problem with Python-Many Cases
  # t= (No.of tasks,time,pay)
t =[(1,7,15),(2,2,20),(3,5,30),(4,3,10),\
    (5,4,18),(6,5,10),(7,2,23),(8,7,16),\
    (9,3,25)]

# FIRST: Calculate the Pay:  for only the ones completed on time- Within 7 HoursF

def whatIsPay(v): 
    total = 0
    for i in range(0,len(v)):
        if (v[i][1] >= i+1):
            total = total + v[i][2]
    return total
print(whatIsPay(t),t)


#CASE-SORT BY TIME?
from operator import itemgetter
t1 = sorted(t,key=itemgetter(1))
print(whatIsPay(t1),t1)

# CASE-SORT BY PAY?
t2 = sorted(t,key=itemgetter(2),reverse=True)
print(whatIsPay(t2),t2)
# CASE- BRUTE LABOUR FORCE?
   # 9 Optional: so 9 factorial possibilities = 362880
from itertools import permutations
p = list(permutations(t))

def printMax(v):
    high = 0
    for v1 in v:
        thigh = whatIsPay(v1)
        if (thigh > high):
            high = thigh
            v2 = v1
    print(high,v2)
    print()

printMax(p)   # for permutations


# SPECIAL SOLUTION: FIND WHAT WORKS IN EACH HOUR OPTIONS
#available
s = []
for i in range(0,9):
    s1 = []
    for j in range(0,9):
        if (t[j][1] >= i):
            s1.append(t[j])
    s.append(s1)

    print(i + 1, s[i])
    print()

# CREATE SELECTIVE PERMUTATION LIST from only available options

from itertools import product
c = list(product(s[0],s[1]))
c = list(set(c))

# We ve got now 64 of lists c, each of which must cross with,
## each new s.

c = list(product(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))
c = list(set(c))
printMax(c)

# IF WE CAN DETECT DUPLICATES , THEN WE CAN REMOVE THEM OUT

def has_duplicates(arr):
    if len(arr) == len(set(arr)):
        return False
    else:
        return True

d = c[:]  ## Copy of C

for c1 in c:
    if has_duplicates(c1):
        d.remove(c1)

printMax(d)    # normal case
printMax(p)    # for permutations

    

