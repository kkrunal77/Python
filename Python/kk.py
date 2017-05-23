if name == 'main': 
	n = int(input()) 
	d = {} 
	for _ in range(n): 
		s = input().split()
    	d[s[0]]=[float(s[1]),float(s[2]),float(s[3])]
	sr=input() f = 0 for i in range(len(s)-1): 
		f += d[sr][i] f = f/(len(s)-1) 
		print("%.2f" % round(f,2))

#my code 

n = int(input())
my_dict = {}
for line in range(n):
    info = input().split(" ")
    score = list(map(float, info[1:]))
    my_dict.update({info[0] : sum(score)/float(len(score))}) 
print("%.2f" % round(my_dict[input()],2))

#########################################
# pattern arrnage
###########################################

#Replace all ______ with rjust, ljust or center. 
Sample Input

5
Sample Output

    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 

#############################################

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
#######################
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
#######################
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        # print(s[::].center("-",))
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    # print(L[::-1])
    print('\n'.join(L[:0:-1]+L))

#############################
#set of 'a' and 'b' 
input()
a=set(map(int,raw_input().split()))
input()
b=set(map(int,raw_input().split()))
c=a.symmetric_difference(b)
for n in sorted(list(c)):
    print n


a,b = [set(raw_input().split()) for _ in range(4)][1::2]
print '\n'.join(sorted(a^b, key=int))

#############################
#finding substring
string, substring = (input().strip(), input().strip())
print(sum([ 1 for _ in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))
# 1)

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count
##############################
#Set .discard(), .remove() & .pop() 
Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
#############CODE###############
n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))

#################################
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
#########CODE################
# Set .union() Operation("|")
a,b = [set(input().split()) for _ in range(4)][1::2]
c=set(a|b) #c=set(a.union(b))
print(sum([1 for i in c])

##################################
Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

5
###############CODE###############
#Set .intersection() Operation("&") 
input()
a = set(input().split())
input()
b= set(input().split())
#c= a&b
c = set(a.intersection(b)) 
print(sum([1 for _ in c]))

##################################
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output
4
#################################
#Set .difference() Operation("-")
input()
a = set(input().split())
input()
b= set(input().split())
c = a.difference(b) 
print(sum([1 for _ in (a-b)]))
#################################
#Set .symmetric_difference() Operation("^")
 Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

8
##############CODE#################

a,b = [set(input().split()) for _ in range(4)][1::2]
# kk = [1,2,3,4,5,6,7,8,9]
# print(kk[sart_pos::end_pos])
c = a.symmetric_difference(b) 
print(sum([1 for _ in c]))

###################################
#input
Sample Input

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output

False
###################################
a=set(map(int, raw_input().split()))
n=input()
f=0
for i in range(n):
    b=set(map(int, raw_input().split()))
    if len(b.difference(a))!=0: 
        f=1
    else:
        if len(b)==len(a):
            f=1
if f==0:
    print "True"
else:
    print "False"

##############code##################
A = set(input().split())

for _ in range(int(input())):
    if not A.issuperset(set(input().split())):
        print(False)
        break
else:
    print(True)

##############join##################
#pyhon Python List Comprehensions: Explained Visually
# http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
from itertools import combinations_with_replacement as kk
a, b =  input().split()
print(*[''.join(p) for p in kk(sorted(a),int(b))],sep="\n")
