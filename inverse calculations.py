#our codes
import math
#use a set of (x, y, z) in a list
x = 2
y = 2
z = 2
goal = (x, y, z)

def anglesolver(coords):
    xcoord = coords[0]
    ycoord = coords[1]
    zcoord = coords[2]
    base_length = math.sqrt((xcoord**2) + (zcoord**2))
    #base_length = math.sqrt(base_length)
    origin_to_point_hypotenuse = math.sqrt((base_length**2) + (zcoord**2))
    angle_base = math.atan(zcoord/base_length)
    #a^2 = b^2 + c^2 -2bccos(A)
    limb_a_length = 3 #cm
    limb_b_length = 3 #cm
    #theta = acos((-origin_to_base_hypotenuese^2 + limb_a_length^2 + limb_b_length^2)/(2*limb_a_length))
    #theta_internal = math.acos(((1-origin_to_point_hypotenuse**2) + limb_a_length**2 + limb_b_length**2)/(2*limb_a_length))
    #complete_data_set = (theta_internal, angle_base, origin_to_point_hypotenuse)
    complete_data_set = (angle_base, origin_to_point_hypotenuse)
    return complete_data_set

coord = ( 1, 2, 2)
solved = anglesolver(coord)
print(solved)

