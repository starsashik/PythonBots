s = open('24(1).txt').readline().replace('AB', '1').replace('AC', '1')
s = s.replace('A',' ').replace('B',' ').replace('C',' ')
print(max(len(x) for x in s.split()))