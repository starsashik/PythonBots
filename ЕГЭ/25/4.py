dd = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
for i in dd:
    d = []
    for x1 in range(10):
        for x2 in range(10):
            for x3 in range(10):
                for x4 in range(10):
                    for x5 in range(10):
                        for x6 in range(10):
                            if x1 + x2 + x3 + x4 + x5 + x6 == i:
                                if int(f'1234{x1}{x2}{x3}{x4}{x5}{x6}') % ((i + 2) ** 3) == 0:
                                    d += [int(f'1234{x1}{x2}{x3}{x4}{x5}{x6}')]
                                if x6 == 0:
                                    if int(f'1234{x1}{x2}{x3}{x4}{x5}') % ((i + 2) ** 3) == 0:
                                        d += [int(f'1234{x1}{x2}{x3}{x4}{x5}')]
                                    if x5 == 0:
                                        if int(f'1234{x1}{x2}{x3}{x4}') % ((i + 2) ** 3) == 0:
                                            d += [int(f'1234{x1}{x2}{x3}{x4}')]
                                        if x4 == 0:
                                            if int(f'1234{x1}{x2}{x3}') % ((i + 2) ** 3) == 0:
                                                d += [int(f'1234{x1}{x2}{x3}')]
                                            if x3 == 0:
                                                if int(f'1234{x1}{x2}') % ((i + 2) ** 3) == 0:
                                                    d += [int(f'1234{x1}{x2}')]
                                                if x2 == 0:
                                                    if int(f'1234{x1}') % ((i + 2) ** 3) == 0:
                                                        d += [int(f'1234{x1}')]
                                                    if x1 == 0:
                                                        if int(f'1234') % ((i + 2) ** 3) == 0:
                                                            d += [int(f'1234')]
    if d:
        print(min(d), i)
