romenia = {
"Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
"Zerind": {"Oradea": 71, "Arad": 75},
"Timisoara": {"Lugoj": 111, "Arad": 118},
"Lugoj": {"Timisoara": 111, "Mehadia": 70},
"Mehadia": {"Lugoj": 70, "Drobeta": 75},
"Drobeta": {"Mehadia": 75, "Craiova": 120},
"Craiova": {"Rimnicu Vilcea": 146, "Pitesti": 138, "Drobeta": 120,},
"Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146,},
"Sibiu": {"Rimnicu Vilcea": 80, "Oradea": 151, "Fagaras": 99, "Arad": 140,},
"Oradea": {"Zerind": 71, "Sibiu": 151},
"Fagaras": {"Sibiu": 99, "Bucharest": 211},
"Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
"Bucharest": {"Urziceni": 85, "Pitesti": 101, "Giurgiu": 90, "Fagaras": 211},
"Giurgiu": {"Bucharest": 90},
"Urziceni": {"Vaslui": 142, "Hirsova": 98, "Bucharest": 85,},
"Hirsova": {"Urziceni": 98, "Eforie": 86},
"Eforie": {"Hirsova": 86},
"Vaslui": {"Urziceni": 142, "Iasi": 92},
"Iasi": {"Vaslui": 92, "Neamt": 87},
"Neamt": {"Iasi": 87}
}

def dfs(start, goal):
    visitados = []
    fringe = [start]
    path = []

    while fringe:
        visitando = fringe.pop()
        if visitando not in visitados:
            visitados.append(visitando)
            path.append(visitando)

            if visitando == goal:
                return path

            for vizinho in romenia[visitando]:
                fringe.append(vizinho)

dfs("Arad", "Bucharest")
