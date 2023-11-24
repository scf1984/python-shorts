from operator import add, sub, mul, truediv
from decimal import Decimal

inverse = {
    add: sub,
    sub: add,
    mul: truediv,
    truediv: mul
}


def compose(factors, composite):
    if factors and not isinstance(factors[0], Decimal):
        composite = Decimal(composite)
        factors = tuple(Decimal(_) for _ in factors)

    if len(factors) == 1 and composite == factors[0]:
        return [('start', factors[0])]
    if not factors and composite != 0:
        return None

    for op in (add, sub, mul, truediv):
        op_inverse = inverse[op]
        for i in range(len(factors)):
            factor = factors[i]
            new_composite = op_inverse(composite, factor)
            recurse = compose(factors[:i] + factors[i+1:], new_composite)
            if recurse is not None:
                recurse.append((op.__name__, factor))
                return recurse


print(compose((2, 4, 5, 6), 28))
