
def read_graph(file_name):

    with open(file_name, 'r') as file:
        content = file.read()

        edges = content.strip().split('),(')

        edges[0] = edges[0][1:]
        edges[-1] = edges[-1][:-1]

    graph = {}
    for edge in edges:
        u, v, w = edge.split(',')
        if u not in graph:
            graph[u] = []
        graph[u].append((v, int(w)))
    return graph

def find_min_distance_node(distances, visited):
    min_distance = float('inf')
    min_node = None
    for node, distance in distances.items():
        if not visited[node] and distance < min_distance:
            min_distance = distance
            min_node = node
    return min_node

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = {node: False for node in graph}
    previous_nodes = {node: None for node in graph}
    
    current_node = start
    
    while current_node is not None:
        visited[current_node] = True
        
        for neighbor, weight in graph.get(current_node, []):
            if not visited[neighbor]:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node
        
        current_node = find_min_distance_node(distances, visited)
        
        if current_node == end:
            break

    path, node = [], end
    while previous_nodes[node] is not None:
        path.insert(0, node)
        node = previous_nodes[node]
    if path:
        path.insert(0, start)
    
    return distances[end], path

graph = read_graph("dijkstra.txt")

start = input("Enter the origin node: ")
end = input("Enter the destination node: ")

distance, path = dijkstra(graph, start, end)

if distance == float('inf'):
    print(f"No path from {start} to {end}")
else:
    print(f"The shortest path from {start} to {end} is {path} with total distance {distance}")
