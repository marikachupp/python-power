from learning_vectors import Vector

jim = Vector(6, 8)
tom = Vector(12, 16)

print "Jim:", (jim.x, jim.y)
print "Tom:", (tom.x, tom.y)

jim.x = 3
jim.y = 4

print "Jim:", (jim.x, jim.y)
print "Tom:", (tom.x, tom.y)

print jim

print jim == tom

tom.x = 3
tom.y = 4

print jim == tom
