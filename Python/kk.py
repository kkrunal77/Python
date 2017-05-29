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
Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)

#######################################

from itertools import combinations_with_replacement as kk
a, b =  input().split()
print(*[''.join(p) for p in kk(sorted(a),int(b))],sep="\n")
#######################################
Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
#################CODE###################
from itertools import groupby

print(*[(len(list(g)),int(k)) for k, g in groupby(input())], sep=" ")

########################################

Task

You are given a string . 
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string  and the integer value .

Constraints

 
The string contains only UPPERCASE characters.

Output Format

Print the permutations of the string  on separate lines.

Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
#################CODE###################
from itertools import permutations as kk
string, k = input().split()
print(*[''.join(i) for i in kk(sorted(string), int(k))], sep= "\n") 

###########################################

Task

You are given a string . 
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints

 
The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
Submissions: 7188
Max Score: 10
Difficulty: Easy
Rate This Challenge:
    
More
Current Buffer (saved locally, editable)     

################CODE#######################
from itertools import combinations as kk
string, n = input().split()
for i in range(1, int(n)+1):
    for j in kk(sorted(string), i):
        print(''.join(j))
##########################################@
Input Format

A single line containing the string  and integer value  separated by a space.

Constraints

 
The string contains only UPPERCASE characters.

Output Format

Print the combinations with their replacements of string  on separate lines.

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
Submissions: 6499
Max Score: 10
Difficulty: Easy
Rate This Challenge:
    
More
Current Buffer (saved locally, editable)     
 
Python 3
###################CODE###################

from itertools import combinations_with_replacement as kk
a, b =  input().split()
print(*[''.join(p) for p in kk(sorted(a),int(b))],sep="\n")

#########################################################################################
Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.

Constraints



All the letters in the list are lowercase English letters.

Sample Input

4 
a a c d
2
Sample Output

0.8333
Explanation

All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd'), ('c', 'd')


Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter 'a'.

Hence, the answer is 5/6.
#########################################CODE#############################################
from itertools import combinations as kk
a = input()
b = input().split()
c = int(input())
all_comb = list(kk(sorted(b), c))
print(all_comb)
a_comb = list(filter(lambda x: 'a' in x, all_comb))
print(len(a_comb)/len(all_comb))

#########################################################################################
Input Format 
The first line contains  space separated integers K and M. 
The next K lines each contains an integer Ni followed by Ni space separated integers denoting the elements in the list.

Output Format 
Output a single integer denoting the value S(max).

Constraints 
 
 
 

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206
Explanation

Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal to (5^2 + 9^2 + 10^2)%1000 = 206.


##########################################CODE############################################
#+++++++++++++++++MY_CODE+++++++++++++++++++++++++
line , M = input().split()
kk = []
for i in range(int(line)):
    li = list(map(int, input().split()))[1:] 
    kk.append(list(sorted((map(lambda x: x*x , set(li)))))[::-1][0])

print(sum(kk)%int(M))

#+++++++++++++++USING possible_combination+++++++++++++++++++++++++++++++++++++++++++++++++
K, M = [int(x) for x in input().split()]

KK = []
for _i_ in range(K):
    KK.append([int(x) for x in input().split()][1:])
    
from itertools import product
possible_combination = list(product(*KK))

def func(nums):
    return sum(x*x for x in nums) % M

print(max(list(map(func, possible_combination))))

###############################################################################################

























By kk(krunal kalariya)