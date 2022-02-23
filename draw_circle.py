# usr/bin/env python3

from math import sqrt


def draw_circle(r: int) -> None:
    d, rmin, rmax = r*2 + 1, -r, r+1
    grid = [["."]*d for _ in range(d)]
    for x in range(rmin, rmax):
        for y in range(rmin, rmax):
            if abs(sqrt(x*x + y*y) - r) < 0.5:
                grid[x+r][y+r] = "@"
    for row in grid:
        print(*row)


def main() -> None:
    radius = input("Type in the radius of the circle you want to draw: ")
    print()
    draw_circle(int(radius))


if __name__ == "__main__":
    main()
