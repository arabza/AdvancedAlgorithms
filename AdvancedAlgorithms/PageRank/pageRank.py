from collections import defaultdict

#Obtain all lines of the txt file
def readFile(fileName):
    with open(fileName, mode="r") as file:
        lines = file.readlines()
        return lines

#auxiliary function to print out nodes, values and its rank
def printRound(values, i):
    print(f"Values at round {i}:")

    # Pair each value with its corresponding node (1-indexed)
    nodes_with_values = [(index + 1, value) for index, value in enumerate(values)]
    
    # Sort the nodes by their value to determine rank (ascending order)
    sorted_nodes = sorted(nodes_with_values, key=lambda x: x[1])
    
    # Create a rank dictionary: node -> rank
    rank_dict = {node: rank + 1 for rank, (node, value) in enumerate(sorted_nodes)}

    # Print the values along with their rank
    for node, value in nodes_with_values:
        print(f"Node {node}, value = {value:.5f}, Rank: {rank_dict[node]}")

#calculate the outlinks for each node
def calculate_outlinks(lines):
    # Dictionary to store outlinks for each node
    outlinks = defaultdict(int)
    # Parse each line and update the outlinks count
    for line in lines:
        # Remove spaces and parentheses, then split by commas
        line = line.strip().replace('(', '').replace(')', '')
        A, B = line.split(',')
        A, B = int(A), int(B)

        # Increment the count of outlinks for node A
        outlinks[A] += 1

    return outlinks

#calculate the rank value in a round considering the values of previous round
def calculateRank(prevValues):
    rp1 = prevValues[1]/outlinksRes[2] + prevValues[2]/outlinksRes[3] + prevValues[3]/outlinksRes[4] + prevValues[4]/outlinksRes[5] + prevValues[5]/outlinksRes[6] + prevValues[6]/outlinksRes[7] + prevValues[8]/outlinksRes[9] 
    rp2 = prevValues[0]/outlinksRes[1] + prevValues[2]/outlinksRes[3] + prevValues[6]/outlinksRes[7] + prevValues[8]/outlinksRes[9]
    rp3 = prevValues[5]/outlinksRes[6] + prevValues[6]/outlinksRes[7]
    rp4 = prevValues[1]/outlinksRes[2] + prevValues[2]/outlinksRes[3] + prevValues[4]/outlinksRes[5] + prevValues[5]/outlinksRes[6] + prevValues[6]/outlinksRes[7] + prevValues[7]/outlinksRes[8] + prevValues[8]/outlinksRes[9]
    rp5 = prevValues[1]/outlinksRes[2] + prevValues[2]/outlinksRes[3] + prevValues[3]/outlinksRes[4] + prevValues[6]/outlinksRes[7] + prevValues[7]/outlinksRes[8]
    rp6 = prevValues[1]/outlinksRes[2] + prevValues[2]/outlinksRes[3] + prevValues[3]/outlinksRes[4] + prevValues[4]/outlinksRes[5] + prevValues[6]/outlinksRes[7] + prevValues[7]/outlinksRes[8] + prevValues[8]/outlinksRes[9]
    rp7 = prevValues[1]/outlinksRes[2] + prevValues[8]/outlinksRes[9]
    rp8 = prevValues[2]/outlinksRes[3] + prevValues[8]/outlinksRes[9]
    rp9 = prevValues[0]/outlinksRes[1] + prevValues[1]/outlinksRes[2]
    calcRank = [rp1, rp2, rp3, rp4, rp5, rp6, rp7, rp8, rp9] #calc rank is equal to the results for the current round

    return calcRank

def calculateRanks(numberOfRounds, noOfNodes):
    values = [1/noOfNodes] * noOfNodes  # Initial values (round 0)
    printRound(values, 0)  # Print round 0
    
    for i in range(1, numberOfRounds + 1):
        values = calculateRank(values)  # Update the values for this round
        printRound(values, i)  # Print values and ranks for this round

#begin of execution
fileName = input("Enter file path: ")
nodes = readFile(fileName)
outlinksRes = calculate_outlinks(nodes)
noOfNodes = len(outlinksRes)
noOfRounds = int(input("Enter the number of rounds to be processed: "))
calculateRanks(noOfRounds, noOfNodes)
