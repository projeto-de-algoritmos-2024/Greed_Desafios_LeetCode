class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n  # Inicialmente, cada nó é um componente separado

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union
            if self.rank[rootX] < self.rank[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            if self.rank[rootX] == self.rank[rootY]:
                self.rank[rootX] += 1

            self.components -= 1
            return True
        return False

class Solution(object):
    def minCostConnectPoints(self, points):

        n = len(points)
        
        # Gerar todas as arestas (distância de Manhattan) do grafo
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        # Ordenar as arestas pelo custo (distância)
        edges.sort(key=lambda element: element[0])
        
        # Iterar sobre as arestas e unir usando Union-Find
        uf = UnionFind(n)

        min_cost = 0
        for dist, i, j in edges:
            if uf.union(i, j):
                min_cost += dist
                if uf.components == 1:
                    break
        
        return min_cost

points = [[3,12],[-2,5],[-4,1]]

# Instancia a solução
sol = Solution()

# Calcula o custo mínimo
resultado = sol.minCostConnectPoints(points)
print(resultado)


