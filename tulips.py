def fancy_tuple(n, d):
    return (n / d), (n % d)


print fancy_tuple(4, 3) == (1, 1)
print fancy_tuple(421, 33) == (12, 25)


def fancy_dict(n, d):
    return {'q': (n / d), 'r': (n % d)}


print fancy_dict(4, 3) == {'q': 1, 'r': 1}
print fancy_dict(421, 33) == {'q': 12, 'r': 25}
