d = "FEDCBA9876543210"
k = 0
for i1 in d:
    for i2 in d[d.index(i1) + 1 :: 2]:
        for i3 in d[d.index(i2) + 1:: 2]:
            for i4 in d[d.index(i3) + 1:: 2]:
                for i5 in d[d.index(i4) + 1:: 2]:
                    for i6 in d[d.index(i5) + 1:: 2]:
                        for i7 in d[d.index(i6) + 1:: 2]:
                            for i8 in d[d.index(i7) + 1:: 2]:
                                for i9 in d[d.index(i8) + 1:: 2]:
                                    for i10 in d[d.index(i9) + 1:: 2]:
                                        for i11 in d[d.index(i10) + 1:: 2]:
                                            for i12 in d[d.index(i11) + 1:: 2]:
                                                k += 1
print(k)


