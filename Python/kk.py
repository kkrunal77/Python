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

#########################################################################kk######################

                          #Numpy

##################################################################################################

Input Format

A single line of input containing space separated numbers.

Output Format

Print the reverse NumPy array with type float.

Sample Input

1 2 3 4 -8 -10
Sample Output

[-10.  -8.   4.   3.   2.   1.]

##########################################CODE##################################################

import numpy as np
print(np.array(input().split(), float)[::-1])
#################################################################################################

Input Format

A single line of input containing  space separated integers.

Output Format

Print the X NumPy array.

Sample Input

1 2 3 4 5 6 7 8 9
Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]

 ##########################################CODE#################################################

import numpy as kk
print(kk.array(input().split(), int).reshape(3,3))
#################################################################################################


nput Format

The first line contains the space separated values of N and M. 
The next  lines contains the space separated elements of M columns.

Output Format

First, print the transpose array and then print the flatten.

Sample Input

2 2
1 2
3 4import numpy l=[] t=[] n,m,p=map(int,input().split()) for i in range(n): l.append([int(i) for i in input().split()]) for i in range(m): t.append([int(i) for i in input().split()]) print (numpy.concatenate((l, t), axis = 0))
Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]

#########################################CODE###################################################

import numpy as np
N, M = input().split()

kk = np.array([input().split() for _ in range(int(N))], int)
print(kk.transpose())
print(kk.flatten())


#################################################################################################
Input Format

The first line contains space separated integers , N and M. 
The next N lines contains the space separated elements of the P columns. 
After that, the next M lines contains the space separated elements of the P columns.

Output Format

Print the concatenated array of size (N+M)XP.

Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4

Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 

##########################################CODE###################################################

import numpy
#N,M,P=map(int, input().split())
#print(np.array([input().strip().split() for _ in range(N+M)], int))
l=[] 
t=[] 
n,m,p=map(int,input().split()) 
for i in range(n):
    l.append([int(i) for i in input().split()]) 
for i in range(m):
    t.append([int(i) for i in input().split()]) 
print (numpy.concatenate((l, t), axis = 0))

#################################################################################################
You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format

A single line containing the space-separated integers.

Constraints


Output Format

First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

Sample Input 0

3 3 3
Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]


##########################################CODE###################################################

import numpy as np
num =tuple(map(int, input().split()))

print(np.zeros(num,int))
print(np.ones(num,int))

#################################################################################################
import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
Task

Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.

Input Format

A single line containing the space separated values of  and . 
 denotes the rows. 
 denotes the columns.

Output Format

Print the desired X array.

Sample Input

3 3
Sample Output

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
##########################################CODE###################################################
import numpy as np
a,b = map(int, input().split())
print(np.eye(int(a),int(b),0))
#################################################################################################
Task

You are given two arrays ( & ) of dimensions X. 
Your task is to perform the following operations:

Add ( + )
Subtract ( - )
Multiply ( * )
Divide ( / )
Mod ( % )
Power ( ** )
Input Format

The first line contains two space separated integers,  and . 
The next  lines contains  space separated integers of array . 
The following  lines contains  space separated integers of array .

Output Format

Print the result of each operation in the given order under Task.

Sample Input

1 4
1 2 3 4
5 6 7 8
Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
Use // for division in Python 3.


##########################################CODE###################################################
import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n') 
#################################################################################################
input array

a= [8.5, 2.4, 3.1, 6.4, 5.5, 6.6, 7.7, 8.8, 9.9]

Output array

[ 8.  2.  3.  6.  5.  6.  7.  8.  9.]
[  9.   3.   4.   7.   6.   7.   8.   9.  10.]
[  8.   2.   3.   6.   6.   7.   8.   9.  10.]


##########################################CODE###################################################

import numpy as np
#a = input().split()
a= [8.5, 2.4, 3.1, 6.4, 5.5, 6.6, 7.7, 8.8, 9.9]
kk = np.array(a, float)
print(np.floor(kk), np.ceil(kk), np.rint(kk), sep="\n")

#################################################################################################
Task

You are given a 2-D array with dimensions X. 
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format

The first line of input contains space separated values of  and . 
The next  lines contains  space separated integers.

Output Format

Compute the sum along axis . Then, print the product of that sum.

Sample Input

2 2
1 2
3 4
Sample Output

24
Explanation

The sum along axis  = [ ] 
The product of this sum = 

############################################CODE###################################################

import numpy as np
n,m = map(int , input().split())
kk = np.array([input().split() for _ in range(n)], int)
print( np.prod(np.sum(kk, axis=0)))

#################################################################################################
Task

You are given a 2-D array with dimensions X. 
Your task is to perform the min function over axis  and then find the max of that.

Input Format

The first line of input contains the space separated values of  and . 
The next  lines contains  space separated integers.

Output Format

Compute the min along axis  and then print the max of that result.

Sample Input

4 2
2 5
3 7
1 3
4 0
Sample Output

3
Explanation

The min along axis 1 =  
The max of  = 
############################################CODE###################################################

import numpy as np
n,m = map(int , input().split())
kk = np.array([input().split() for _ in range(n)], int)
print(np.max(np.min(kk, axis=1), axis=0))

####################################################################################################
mean

The mean tool computes the arithmetic mean along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5
By default, the axis is None. Therefore, it computes the mean of the flattened array.

var

The var tool computes the arithmetic variance along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25
By default, the axis is None. Therefore, it computes the variance of the flattened array.

std

The std tool computes the arithmetic standard deviation along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.

Task

You are given a 2-D array of size X. 
Your task is to find:

The mean along axis 
The var along axis 
The std along axis 
Input Format

The first line contains the space separated values of  and . 
The next  lines contains  space separated integers.

Output Format

First, print the mean. 
Second, print the var. 
Third, print the std.

Sample Input

2 2
1 2
3 4
Sample Output

[ 1.5  3.5]
[ 1.  1.]
1.11803398875


############################################CODE###################################################
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
n,m = map(int, input().split())
kk = np.array([input().split() for _ in range(n)], int)
print(np.mean(kk, axis=1), np.var(kk, axis=0), np.std(kk, axis=None), sep="\n")
###################################################################################################
dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11
cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
Task

You are given two arrays  and . Both have dimensions of X. 
Your task is to compute their matrix product.

Input Format

The first line contains the integer . 
The next  lines contains  space separated integers of array . 
The following  lines contains  space separated integers of array .

Output Format

Print the matrix multiplication of  and .

Sample Input

2
1 2
3 4
1 2
3 4
Sample Output

[[ 7 10]
 [15 22]]
##############################################CODE#################################################

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n =int(input())
kk1 = np.array([input().split() for _ in range(n)], int)
kk2 = np.array([input().split() for _ in range(n)], int)
print(np.dot(kk1,kk2))


############################################################################################
Task 
You are given a string , containing , and/or . and 0-9 digits. 
Your task is to re.split() all of the , and . symbols.

Input Format

A single line of input containing the string .

Output Format

Print the numbers obtained after splitting the string on separate lines.

Sample Input

100,000,000.000
Sample Output

100
000
000
000
########################################CODE################################################

import re 
kk = input()
kk = re.sub(r"[a-zA-Z]","",kk)
kk = re.split("\,|\.",kk)
print(*[i for i in list(filter(lambda x: len(x), kk))], sep="\n")
############################################################################################

You are the manager of a supermarket. 
You have a list of  items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item. 
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, . 
The next  lines contains the item's name and price, separated by a space.

Constraints


Output Format

Print the item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

########################################CODE################################################
from collections import OrderedDict
ordinary_dictionary = {}
dic = OrderedDict()
for i in range(int(input())):
    line = input().split()
    item, price = ' '.join(line[:-1]), int(line[-1])
    if item in dic:
        dic[item]+=price
    else:
        dic[item]=price
[print(i,j) for i, j in dic.items()]

############################################################################################
"""Word Order"""
Input Format

The first line contains the integer, . 
The next  lines each contain a word.

Output Format

Output  lines. 
On the first line, output the number of distinct words from the input. 
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.


##################################################################################################
from collections import OrderedDict
l = OrderedDict()
for i in range(int(input())):
    key = input()
    val = 1
    if key in l:  
        l[key]+=val
    else:
        l[key]=val
print(len(l))
print(*[j for i,j in l.items()], sep=" ")






By KK(krunal kalariya)