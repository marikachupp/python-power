from we_made_a_ball import Ball, move_ball

bouncy = Ball(4, 9, 3, -2)

print "Pos:", (bouncy.delta_x, bouncy.delta_y), "Vel:", (bouncy.vel_x, bouncy.vel_y)

updated_bouncy = move_ball(bouncy, 1)

print "new pos:", (updated_bouncy.delta_x, updated_bouncy.delta_y), "Vel:", (updated_bouncy.vel_x, updated_bouncy.vel_y)
