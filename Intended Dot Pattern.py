pattern_1 = lambda n: [print(' ' * (n - x) + '• ' * x) for x in range(1, n + 1)]
pattern_2 = lambda n: [print(' ' * (n - x) + '• ' * x) for x in range(n, 0, -1)]

pattern_1(10)
pattern_2(9)
