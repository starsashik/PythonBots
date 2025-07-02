f = open('26.txt')
boxes = []
for x in f:
    a, b = x.split()
    a = int(a)
    boxes.append((a, b))

boxes = sorted(boxes)[::-1]
warehouse = []
while len(boxes) > 0:
    block = [boxes.pop(0)]
    for i in range(len(boxes)):
        if boxes[i][1] != block[-1][1] and block[-1][0] - boxes[i][0] >= 5:
            block.append(boxes[i])
            boxes[i] = ''
    warehouse.append(block)
    boxes = [x for x in boxes if x != '']
print(max(len(x) for x in warehouse), len(warehouse))
