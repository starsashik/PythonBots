class SeaMap:
    dd = [['.'] * 10 for i in range(10)]

    def cell(self, row, col):
        return self.dd[row][col]

    def shoot(self, row, col, result):
        row1, col1 = row, col
        s = ''
        if result == 'miss':
            self.dd[row][col] = '*'
        elif result == 'hit':
            self.dd[row][col] = 'X'
        elif result == 'sink':
            # сам корабль и диагонали
            self.dd[row][col] = 'X'
            if row + 1 < 10 and col + 1 < 10:
                self.dd[row + 1][col + 1] = '*'
            if row - 1 > 0 and col - 1 > 0:
                self.dd[row - 1][col - 1] = '*'
            if row + 1 < 10 and col - 1 > 0:
                self.dd[row + 1][col - 1] = '*'
            if row - 1 > 0 and col + 1 < 10:
                self.dd[row - 1][col + 1] = '*'
            row, col = row1, col1
            flag_vniz = False
            while not flag_vniz:
                if row + 1 < 10:
                    if self.dd[row + 1][col] == '.':
                        flag_vniz = True
                        self.dd[row + 1][col] = '*'
                    else:
                        if row + 2 < 10 and col + 1 < 10:
                            self.dd[row + 2][col + 1] = '*'
                        if row + 2 < 10 and col - 1 > 0:
                            self.dd[row + 2][col - 1] = '*'
                    row += 1
                    if self.dd[row][col] == '*':
                        flag_vniz = True
                else:
                    flag_vniz = True
            row, col = row1, col1
            flag_verh = False
            while not flag_verh:
                if row - 1 > 0:
                    if self.dd[row - 1][col] == '.':
                        flag_verh = True
                        self.dd[row - 1][col] = '*'
                    else:
                        if row - 2 < 10 and col + 1 < 10:
                            self.dd[row - 2][col + 1] = '*'
                        if row - 2 < 10 and col - 1 > 0:
                            self.dd[row - 2][col - 1] = '*'
                    row -= 1
                    if self.dd[row][col] == '*':
                        flag_verh = True
                else:
                    flag_verh = True
            row, col = row1, col1
            flag_vpravo = False
            while not flag_vpravo:
                if col + 1 < 10:
                    if self.dd[row][col + 1] == '.':
                        flag_vpravo = True
                        self.dd[row][col + 1] = '*'
                    else:
                        if row + 1 < 10 and col + 2 < 10:
                            self.dd[row + 1][col + 2] = '*'
                        if row - 1 > 0 and col + 2 < 10:
                            self.dd[row - 1][col + 2] = '*'
                    col += 1
                    if self.dd[row][col] == '*':
                        flag_vpravo = True
                else:
                    flag_vpravo = True
            row, col = row1, col1
            flag_vlevo = False
            while not flag_vlevo:
                if col - 1 > 0:
                    if self.dd[row][col - 1] == '.':
                        flag_vlevo = True
                        self.dd[row][col - 1] = '*'
                    else:
                        if row + 1 < 10 and col - 2 > 0:
                            self.dd[row + 1][col - 2] = '*'
                        if row - 1 > 0 and col - 2 > 0:
                            self.dd[row - 1][col - 2] = '*'
                    col -= 1
                    if self.dd[row][col] == '*':
                        flag_vlevo = True
                else:
                    flag_vlevo = True


sm = SeaMap()
sm.shoot(5,5,'sink')
sm.shoot(0,0,'sink')
sm.shoot(0,9,'sink')
sm.shoot(9,0,'sink')
sm.shoot(9,9,'sink')
sm.shoot(0,3,'hit')
sm.shoot(7,3,'miss')


sm.shoot(3,0,'hit')
sm.shoot(4,0,'hit')
sm.shoot(5,0,'sink')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()