def approx_real_root(coeffs, interval):
    ### Replace with your own code (begin) ###
    c0 = coeffs[0]
    c1 = coeffs[1]
    c2 = coeffs[2]
    c3 = coeffs[3]

    def poly_value(x):
        return c0 + c1 * x + c2 * x * x + c3 * x * x * x

    a = float(interval[0])
    b = float(interval[1])

    fa = poly_value(a)
    fb = poly_value(b)

    if fa == 0.0:
        return a
    if fb == 0.0:
        return b

    tol = 1e-9

    while (b - a) > 2 * tol:
        m = 0.5 * (a + b)
        fm = poly_value(m)

        if fm == 0.0:
            return m

        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    root_approx = 0.5 * (a + b)
    return root_approx
    ### Replace with your own code (end)   ###
    
#q(x) = 1 - 4x + x^2
coeffs = [1, -4, 0, 1]
interval = (0.0, 1.0)
approx_real_root(coeffs, interval)
