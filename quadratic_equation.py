from math import sqrt


def get_roots(a, b, c):
    try:
        discriminant = b ** 2 - 4 * a * c
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    except ValueError:
        return None, None
    else:
        if discriminant == 0:
            return root1, None
        else:
            return root1, root2
