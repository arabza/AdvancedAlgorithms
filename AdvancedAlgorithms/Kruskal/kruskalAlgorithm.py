
###################################################################################################
#READ MATRIX

def read_matrix(file_name):
    with open(file_name, "r") as file:
        data = file.read().strip()

    # Replace line breaks and split by semicolon to get rows
    rows = data.split(";")

    adj_matrix = [
        [int(value) for value in row.split(",") if value.strip()] 
        for row in rows if row.strip()
    ] #be sure no empty rows or elements included

    return adj_matrix


def graph_from_matrix(adj_matrix):
    #Convert adjacency matrix to edge list
    #format of edges is (weight, node 1, node 2)
    edges = []
    num_nodes = len(adj_matrix)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adj_matrix[i][j] != 0:
                edges.append((adj_matrix[i][j], i, j))

    edges.sort()
    return edges, num_nodes #return the edges sorted and the number of nodes

###################################################################################################
#UNION - FIND
# Finding root of an element
def find(i):
    # Chase parent of current element until it reaches root
    while parent[i] != i:
        i = parent[i]
    return i

# Modified union function to connect elements by changing the root of one of them
def union(A, B):
    root_A = find(A)
    root_B = find(B)
    parent[root_A] = root_B  # Setting parent of root(A) as root(B)

# Check if two elements are connected
def is_connected(A, B):
    return find(A) == find(B)  # If A and B have the same root, they are connected

###################################################################################################
# KRUSKAL ALGORITHM FOR MST
def kruskal_mst(n_nodes, edges):
    
    # Initialize parent array with each node as its own parent
    global parent
    parent = list(range(n_nodes))
    
    mst = []
    mst_weight = 0
    
    for weight, node1, node2 in edges:
        # Check if adding this edge would form a cycle
        if not is_connected(node1, node2):
            union(node1, node2)   # Connect the two nodes
            mst.append((weight, node1, node2))
            mst_weight += weight
    
    return mst, mst_weight

###################################################################################################
#GENERATE OUTPUT
def mst_to_adjacency_matrix(mst, num_nodes):
    # Initialize an adjacency matrix with zeros
    adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    # Populate the adjacency matrix with edges from MST
    for weight, node1, node2 in mst:
        adj_matrix[node1][node2] = weight
        adj_matrix[node2][node1] = weight  # For undirected graph, mirror the edge

    formatted_matrix = ";".join(
        [",".join(map(str, row)) for row in adj_matrix]
    )

    # Write the formatted matrix to a file
    with open("outputKruskal.txt", "w") as file: #OUTPUT FILE NAME FIXED
        file.write(formatted_matrix)

###################################################################################################

input_matrix_name = input("Enter file name of matrix: ")
matrix = read_matrix(input_matrix_name) #read adjacency matrix from txt file

edges, num_nodes = graph_from_matrix(matrix) # generate graph

mst, mst_weight = kruskal_mst(num_nodes, edges) #generate mst

mst_to_adjacency_matrix(mst, num_nodes) #generate output

print("MST adjacency matrix saved to outputKruskal.txt")