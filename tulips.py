def fancy_tuple(n, d):
    return (n / d), (n % d)


print fancy_tuple(4, 3) == (1, 1)
print fancy_tuple(421, 33) == (12, 25)


def fancy_dict(n, d):
    return {'q': (n / d), 'r': (n % d)}


print fancy_dict(4, 3) == {'q': 1, 'r': 1}
print fancy_dict(421, 33) == {'q': 12, 'r': 25}


class Complex:
    def __init__(self, q, r):
        self.q = q
        self.r = r

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.q == other.q and self.r == other.r


def fancy_complex(n, d):
    return Complex(n / d, n % d)


print fancy_complex(4, 3) == 1.33
print fancy_complex(4, 3) == Complex(1, 1)
print fancy_complex(421, 33) == Complex(12, 25)
