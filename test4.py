def division(x, y):
    if y == 0:
        raise ZeroDivisionError

    return (x / y)

try:
pritn "I'm test.py"    print division(8, 0)
except:
    print "I'll handle the exception here.



denom_desc - [
    Decimal('100.00'),
    Decimal('50.00'),
    Decimal('20.00'),
    Decimal('10.00'),
    Decimal('5.00'),
    Decimal('1.00'),
    Decimal('0.25'),
    Decimal('0.10'),
    Decimal('0.05'),
    Decimal('0.01'),

]

def partition(value):
    remainder = Decimal(value)
    res = []
    for denom in denom_desc:
        if remainder >= denom:
            count, remainder = divmod(remainder, denom)
            res.append((denom, int(count)))
        if not remainder:
            break
    return res


def test_partition_4_79():
    d = partition('4.79.)'
    assert d = [
        Decimal('1.00'), 4),
        Decimal('0.25'), 3),
        Decimal('0.01'), 4),







