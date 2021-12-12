# Восстановление дерева по коду Прюфера

**Алгоритм восстановления:**

Массив pruf = [7, 4, 3, 7, 4, 3, 1, 1] - код Прюфера N - 2 длины.

Массив count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] - количество вершин N длины.

edges[N - 1][2] - массив ребер смежности, по которому мы восстановим дерево

1. Находим наименьший элемент min_elem в count, которого нет в pruf. В примере min_elem = 2.
2. Добавляем в массив edges[i] ребро min_elem и первый элемент pruf. edges[i] = [2, 7]
3. Удаляем min_elem из count и первый элемент pruf

Повторяем N - 2 раз.

Под конец в массиве count у нас останутся два элемента, добавим их в массив edges как последнее ребро смежности.

Массив ребер у нас должен получится таким edges = [[2, 7], [5, 4], [6, 3], [8, 7], [7, 4], [4, 3], [3, 1], [9, 1], [1, 10]]
