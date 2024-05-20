
# Отображение графа на Python с networkx
# https://habr.com/ru/companies/skillfactory/articles/721838/
# How to show multiple images in one figure?
# https://translated.turbopages.org/proxy_u/en-ru.ru.fe8ab87e-6648b864-8fd98157-74722d776562/https/stackoverflow.com/questions/17111525/how-to-show-multiple-images-in-one-figure?

import networkx as nx

# Для визуализации графа
# in Linux: apt-get install elementary-icon-theme
import matplotlib
import matplotlib.pyplot as plt

# 1. Задаём Меры-центральности-поСтепени/Centrality-Measure-byDegree
#    как Dictionary/Словарь
centrality2 = { 0: 0.2,
                1: 0.4,
                2: 0.54,
                3: 0.6,
                4: 0.6,
                5: 0.54,
                6: 0.4,
                7: 0.2 }
print( "Заданные меры центральности по степени 'centrality2'=(as Dictionary/Словарь)\n", centrality2 ) # from 0.0 upto 1.0
dict25 = centrality2  # для удобства использования этого отладочного отображения в других проектах
fig26 = plt.figure()  # создаём пустое окно/фигуру
a27=fig26.add_subplot(2, 2, 1)  # Определяем: две строки, два столбца, последняя "1" - Номер/1 of Plot_picture_картинки
# Draw as LineChart/ЛинейныйГрафик
list29 = sorted(dict25.items())
x30, y30 = zip(*list29)
plt.plot(x30, y30, 1 )  # Используем: последняя "1" - - Масштаб до 1.0
# plt.show()  # show figure constructed, from RAM to screen

# 2. Задаём граф

# 2.1. Сначала создаём граф линейный
G = nx.path_graph(8)

# 2.2. Затем добавляем связи между вершинами графа
G.add_edge(2, 4)
G.add_edge(3, 1)
G.add_edge(3, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)

centrality1 = nx.eigenvector_centrality_numpy(G)
print( "Вычисленные меры центральности по степени 'centrality1'=(as Dictionary/Словарь)" ) # from 0.0 upto 1.0
for n in centrality1:
    print("centrality1(", n, ")=", format(centrality1[n], ".4f") )  # выводить только 4 знака дробной части

# print( "(as Distionary/Словарь): ", centrality1 ) # from 0.0 upto 1.0
dict52 = centrality1  # для удобства использования этого отладочного отображения в других проектах
# fig26 = plt.figure()  # создаём пустое окно/фигуру
a54=fig26.add_subplot(2, 2, 2)  # Определяем: две строки, два столбца, последняя "2" - Номер/2 of Plot_picture_картинки
# Draw as LineChart/ЛинейныйГрафик
list56 = sorted(dict52.items())
x57, y57 = zip(*list56)
plt.plot(x57, y57, 1 )  # Используем: последняя "1" - Масштаб до 1.0
# plt.show()  # show figure constructed, from RAM to screen

# Визуализация графа
# print (G)  # show graph text description
a63=fig26.add_subplot(2, 2, 3 )  # Определяем: две строки, два столбца, последняя "3" - Номер/2 of Plot_picture_картинки
# nx.draw(G)  # construct graph visualization, in RAM
nx.draw(G, node_size=500, with_labels=True, node_color='y') # construct graph visualization, in RAM
plt.show()  # show graph visualization constructed, from RAM to screen


