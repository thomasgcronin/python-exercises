def bar(a, b, *args, **kwargs):
    print a, b, args, kwargs

    for arg in args:
        print arg + '7'

    for val in kwargs.values():
        print val

(’a’, ’b’, ’c’, ’d’, ’e’, ’f’, g=’g’, h=’h’, i=’i’, j=’j’, another_arg="Hi Mom!", 'g': 'g')