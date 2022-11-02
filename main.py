import matplotlib.pyplot as plt

doc_input = open("graphic.csv")

file = doc_input.read()
doc_input.close()

time_graph = []
temperature_graph = []

list = file.replace(';','\n')
list = list.splitlines()

for x in range(len(list)):
    if x % 2 == 0:
        time_graph.append(list[x])
    else:
        temperature_graph.append(list[x])

#print(time_graph)
print(temperature_graph)

time_graph.pop(0)
temperature_graph.pop(0)

for i in range(len(temperature_graph)):
    temperature_graph[i] = temperature_graph[i].replace(',', '.')
    temperature_graph[i] = float(temperature_graph[i])

print(temperature_graph)

fig = plt.figure()
ax = fig.add_subplot(111)

#ax.set_xlim([-10, 10])
ax.set_ylim([10, 150])
ax.set_title('График')
ax.set_xlabel('Время')
ax.set_ylabel('Температура')

ax.plot(time_graph, temperature_graph)  # Plot some data on the axes.

plt.show()