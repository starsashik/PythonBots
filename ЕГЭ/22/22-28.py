import csv
with open('22-28.csv') as f:
    r = list(csv.reader(f, delimiter=','))[1:]
final_time = {}
data_source = {}

for i in r:
    id_pr, time_pr = int(i[0]), int(i[1])
    depends = [int(x) for x in i[2].split(";")]
    if depends == [0]:
        final_time[id_pr] = time_pr
    else:
        data_source[id_pr] = (time_pr, depends)

while data_source:
    keys = list(data_source.keys())
    for i in keys:
        time_pr, depends = data_source[i]
        if all(x in final_time for x in depends):
            max_time = max([final_time[x] for x in depends])
            final_time[i] = time_pr + max_time
            del data_source[i]
print(max(final_time.values()))