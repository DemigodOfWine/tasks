import numpy as np
import matplotlib.pyplot as plt


class ConstantGraph(object):
    ONE_NODE = 0
    ADD_NODE = 1
    REVERS = -1
    SIZE_CIRCLE = 4
    BIN = 2
    ZEROS = 0


class Graph(ConstantGraph):

    def __init__(self):
        self._matrix = np.array([self.ONE_NODE])

    def getMatrix(self):
        return self._matrix

    def addNode(self, num_node):
        node = len(self._matrix) + num_node
        self._matrix = self._matrix + np.zeros([node, node], dtype=int)

    def addEdge(self, node_first, node_second):
        if node_first == node_second:
            return
        elif node_first > node_second:
            self._matrix[node_first][node_second] = self.ADD_NODE
        else:
            self._matrix[node_second][node_first] = self.ADD_NODE

        self._matrix = np.tril(self._matrix) + np.tril(self._matrix, self.REVERS).T

    def plotGraph(self):
        fig, ax = plt.subplots()
        naming = []
        for _ in range(len(self._matrix)):
            naming.append(np.random.randint(np.size(self._matrix), size=2, dtype=int))

        for label, dot in enumerate(naming):
            ax.add_patch(plt.Circle(tuple(dot), len(self._matrix) / self.SIZE_CIRCLE, facecolor='#9ebcda', alpha=0.8))
            plt.text(dot[0], dot[1], label)

        ax.set_aspect('equal', adjustable='datalim')
        ax.set_xbound([3, 4])

        [i_true, j_true] = np.where(self._matrix == True)

        for i in range(len(i_true)):
            plt.plot([naming[i_true[i]][0], naming[j_true[i]][0]],
                     [naming[i_true[i]][1], naming[j_true[i]][1]])

        plt.plot()
        plt.show()

    def picnic(self):
        # picnic = []
        for i, edge in enumerate(self._matrix):
            picnic = []
            friends = [0] * len(self._matrix)
            friends += edge

            for j, edge_status in enumerate(self._matrix):
                # print('проход', i, j)
                # print(friends + edge_status)
                if max(friends + edge_status) <= 1:
                    friends += edge_status
                    picnic.append(i)
                    picnic.append(j)
            print('Возмжно пригласить на пикник', picnic)





class RandomGraph(Graph):
    def __init__(self, num_node):
        super().__init__()
        self._matrix = self._random_graph(num_node)

    def _random_graph(self, num_node):
        graph = np.random.randint(self.BIN, size=[num_node, num_node], dtype=int)
        np.fill_diagonal(graph, self.ZEROS)
        graph = np.tril(graph) + np.tril(graph, self.REVERS).T
        return graph







