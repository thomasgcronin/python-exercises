"""print [x for x in range(1, 10)]
print [x if x % 2 else x * 100 for x in range(1, 10)] if x % 3 == 0]"""


l = [lambda x: x **2,
     lambda x: x **3,
     lambda x: x **4 ]

#for f  in l
    #
    #print
#  print (f(4))

def raise_to_second(x):
    return x**2

print raise_to_second(5)
print l[0](5)






