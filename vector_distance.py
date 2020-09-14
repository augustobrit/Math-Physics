import math

def eval(a, b):
    x = a.x - b.x
    y = b.y - b.y
    z = a.z - b.z

    return math.sqrt(x * x + y * y + z * z)
