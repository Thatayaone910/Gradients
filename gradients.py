def interpolate(start, end, t):
    return int(start + (end - start) * t)

def make_color(start_color, end_color, t):
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color

    r = interpolate(r1, r2, t)
    g = interpolate(g1, g2, t)
    b = interpolate(b1, b2, t)

    return (r, g, b)

for i in range(50):
    t = i / 49
    (r, g, b) = make_color((255, 0, 0), (0, 0, 255), t)
    print(r,g,b)
    print(f"\x1b[48;2;{r};{g};{b}m" + " " * 50 + "\x1b[0m")

#the print, is the Ansi escape,used to control terminal formatting \033[ → begin escape code, 48;2; → set background color,.. {r};{g};{b} → insert red, green, blue, ....m → end color command an *50 prints 50 spaces to make it a square image, \033[0m resets color bak to normal
