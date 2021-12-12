#artyomshutoff

pruf = list(map(int, input('Введите числа через пробел: ').split(' ')))
count = [i for i in range(1, len(pruf) + 2 + 1)]
edges = [[0, 0] for i in range(len(count)-1)]
for i in range(len(pruf)):
	min_elem = 0
	for j in count:
		if j not in pruf:
			min_elem = j
			break
	edges[i] = [min_elem, pruf[0]]
	count.remove(min_elem)
	pruf = pruf[1:]

edges[-1] = count

for i in edges:
	print(f'{i[0]}-{i[1]}', end='; ')
