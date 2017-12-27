from learning_vectors import Vector
from we_made_a_ball import Ball, move_ball

bouncy = Ball(pos=Vector(4, 9), vel=Vector(3, -2))

print "Pos:", (bouncy.pos.x, bouncy.pos.y), "Vel:", (bouncy.vel.x, bouncy.vel.y)

updated_bouncy = move_ball(bouncy, 1)

print "new pos:", (updated_bouncy.pos.x, updated_bouncy.pos.y), "Vel:", (updated_bouncy.vel.x, updated_bouncy.vel.y)
