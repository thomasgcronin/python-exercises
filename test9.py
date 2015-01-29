"""def g( c, d):
    print c + d

def  f(a, b, c, d):
    print a + b
    g(c, d)

f(1, 2, 3, 4)

def foo():
    foo()
foo()

while True:
    print


#while True:
   # print "Hi!"

   #def foo():
    print "Hi!"
    foo()
foo()


def f (a,b):
    print a

def g (b)
    print b

f (5,7)


def foo(n):
    if n < 0:
        return
    print n
    n -= 1
    foo(n)
    print "We've reached the end of foo(), where n was equal to:  " + str(n)

foo(10)

def f():
    print "I've just started f()"
    g()
    print "I'm at the end of f ()"

def g():
    print "I've just started g()"
    print "I'm at the end of g()"

f()"""

def second_element(t):
    return t[1]
zepp = [(’Guitar’, ’Jimmy’), (’Vocals’, ’Robert’), (’Bass’, ’John Paul’),
(’Drums’, ’John’)]
print sorted(zepp, key=second_element)
print sorted(zepp, key=lambda x: x[1])
