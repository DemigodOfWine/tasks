from custom_graph.custom_graph import Graph, RandomGraph

# определяем граф
graph = Graph()
# добавляем 6
print(graph.addNode(6))
#
print(graph.addEdge(2, 1))
#
print(graph.addEdge(2, 4))


# print(graph.getMatrix())

#
graph.plotGraph()

#
graph = RandomGraph(20)
print(graph.getMatrix())
graph.plotGraph()
graph.picnic()



