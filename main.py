a, b, c = map(float, input().split())
d = b ** 2 - 4 * a * c
if a != 0:
    print(([(-b + (d) ** 0.5) / (2 * a), (-b - (d) ** 0.5) / (2 * a)] if (d) > 0 else -b / (2 * a) if (
                                                                                                          d) == 0 else 'корней нет'))
else:
    print(-c / b)
