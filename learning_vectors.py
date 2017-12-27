class Vector:

    # make jim.x and jim.y without explicitly stating them
    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_vector(x, y):
    v = Vector()
    v.x = x
    v.y = y
    return v