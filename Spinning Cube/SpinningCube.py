import os
import math
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def rotate_cube(t):
    vertices = [
        (-15, -15, -15),
        (-15, -15, 15),
        (-15, 15, -15),
        (-15, 15, 15),
        (15, -15, -15),
        (15, -15, 15),
        (15, 15, -15),
        (15, 15, 15),
    ]

    edges = [
        (0, 1), (0, 2), (0, 4),
        (7, 6), (7, 5), (7, 3),
        (1, 3), (1, 5),
        (2, 3), (2, 6),
        (4, 5), (4, 6),
    ]

    def rot_x(v, angle):
        x, y, z = v
        return x, y * math.cos(angle) - z * math.sin(angle), y * math.sin(angle) + z * math.cos(angle)

    def rot_y(v, angle):
        x, y, z = v
        return x * math.cos(angle) + z * math.sin(angle), y, -x * math.sin(angle) + z * math.cos(angle)

    def rot_z(v, angle):
        x, y, z = v
        return x * math.cos(angle) - y * math.sin(angle), x * math.sin(angle) + y * math.cos(angle), z

    def project(v):
        x, y, z = v
        return int(x + w // 2), int(y + h // 2)

    w, h = os.get_terminal_size()

    clear_terminal()

    rotated_vertices = [rot_x(rot_y(rot_z(v, t), t), t) for v in vertices]
    projected_vertices = [project(v) for v in rotated_vertices]

    buffer = [[' ' for _ in range(w)] for _ in range(h)]

    for v1, v2 in edges:
        x1, y1 = projected_vertices[v1]
        x2, y2 = projected_vertices[v2]
        dx, dy = x2 - x1, y2 - y1
        steps = max(abs(dx), abs(dy))

        for i in range(steps):
            x = x1 + i * dx // steps
            y = y1 + i * dy // steps
            if 0 <= x < w and 0 <= y < h:
                buffer[y][x] = '#'

    for line in buffer:
        print(''.join(line))

# main
t = 0
while True:
    rotate_cube(t)
    time.sleep(0.1)
    t += 0.1