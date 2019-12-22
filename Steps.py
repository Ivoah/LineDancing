from math import *

from util import *

def cast(dancer, meta, t):
    if dancer.couple%2 == (meta['couple'] == '2nd'):
        return (
            (
                (-cos(t*pi)/2 + 0.5)*int(meta['places'])*(-1 if meta['direction'] == 'up' else 1),
                sin(t*pi)/3*(-1 if dancer.gender == 'F' else 1)
            ),
            t*360*(-1 if dancer.gender == 'F' else 1)*(-1 if meta['direction'] == 'up' else 1)
        )

    return False

def lead(dancer, meta, t):
    if dancer.couple%2 == (meta['couple'] == '2nd'):
        return (
            (
                (-cos(t*pi)/2 + 0.5)*int(meta['places'])*(-1 if meta['direction'] == 'up' else 1),
                -sin(t*pi)/3*(-1 if dancer.gender == 'F' else 1)
            ),
            -sin(t*pi)*90*(-1 if dancer.gender == 'F' else 1)*(-1 if meta['direction'] == 'up' else 1)
        )
    return False

def corners_cross_right(dancer, meta, t):
    pos, angle = (
        (cos(t*pi/2) - 1, sin(t*pi/2)),
        t*180*(-1 if meta['corners'] == '1st' else 1)
    )

    if dancer.couple%2 and dancer.gender == 'F' and meta['corners'] == '1st': pos = multiply_pos(pos, (1, 1))
    elif not dancer.couple%2 and dancer.gender == 'M' and meta['corners'] == '1st': pos = multiply_pos(pos, (-1, -1))
    elif not dancer.couple%2 and dancer.gender == 'F' and meta['corners'] == '2nd': pos = multiply_pos(pos, (-1, 1))
    elif dancer.couple%2 and dancer.gender == 'M' and meta['corners'] == '2nd': pos = multiply_pos(pos, (1, -1))
    else: return False

    return (pos, angle)

def circle_halfway(dancer, meta, t):
    # pos, angle = ((0, 0), 0)
    # if t < 1/3:
    #     pos = (t/2, t/2)
    #     angle = t*3*45*(1 if dancer.couple%2 else -1)*(-1 if dancer.gender == 'F' else 1)

    #     if dancer.couple%2 and dancer.gender == 'F': pos = multiply_pos(pos, (1, -1))
    #     elif dancer.couple%2 and dancer.gender == 'M': pos = multiply_pos(pos, (1, 1))
    #     elif not dancer.couple%2 and dancer.gender == 'M': pos = multiply_pos(pos, (-1, 1))
    #     elif not dancer.couple%2 and dancer.gender == 'F': pos = multiply_pos(pos, (-1, -1))
    # else:
    #     pass
    # return (pos, angle)

    if dancer.couple%2 and dancer.gender == 'M': pos = (sin(t*pi/2), -cos(t*pi/2) + 1)
    elif not dancer.couple%2 and dancer.gender == 'M': pos = (cos(t*pi/2) - 1, sin(t*pi/2))
    elif not dancer.couple%2 and dancer.gender == 'F': pos = (-sin(t*pi/2), cos(t*pi/2) - 1)
    elif dancer.couple%2 and dancer.gender == 'F': pos = (-cos(t*pi/2) + 1, -sin(t*pi/2))
    return (pos, -t*180)


steps = {
    'cast': cast,
    'lead': lead,
    'corners_cross_right': corners_cross_right,
    'circle_halfway': circle_halfway
}
