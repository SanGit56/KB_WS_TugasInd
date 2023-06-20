# Sumber: https://www.geeksforgeeks.org/m-coloring-problem/

def isSafe(graph, color):
	for i in range(6):
		for j in range(i + 1, 6):
			if (graph[i][j] and color[j] == color[i]):
				return False
	return True

def graphColoring(graph, m, i, color):
	if (i == 6):
		if (isSafe(graph, color)):
			printSolution(color)
			return True
		return False

	for j in range(1, m + 1):
		color[i] = j

		if (graphColoring(graph, m, i + 1, color)):
			return True
		color[i] = 0
	return False

def printSolution(color):
	for i in range(6):
		if(color[i]==1):
			print("node", i, "= red")
		elif(color[i]==2):
			print("node", i, "= green")
		elif(color[i]==3):
			print("node", i, "= blue")

if __name__ == '__main__':
	graph = [
		[0, 1, 1, 0, 0, 0],
		[1, 0, 1, 1, 0, 0],
		[1, 1, 0, 1, 1, 1],
		[0, 1, 1, 0, 1, 0],
		[0, 0, 1, 1, 0, 1],
		[0, 0, 1, 0, 1, 0],
	]

	color_num = 3

	color = [0 for i in range(6)]

	if (not graphColoring(graph, color_num, 0, color)):
		print("Solusi tidak ditemukan")