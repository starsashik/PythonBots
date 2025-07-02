for i in range(1, 9999):
    for j in range(1, 10):
        s = f'32{i}54{j}123'
        if int(s) % 519 == 0:
            if len(s) % 2 == 0:
                if s.count('0') == 0:
                    s1 = s[:len(s) // 2]
                    s2 = s[len(s) // 2:]
                    if sum([int(x) for x in s1]) == sum([int(g) for g in s2]):
                        print(s, int(s) // 519)
