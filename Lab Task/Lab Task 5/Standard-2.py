class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        self.size = size + 1                                            #Add one additional vertex to compensate
        for i in range(self.size):
            self.adjMatrix.append([0 for i in range(self.size)])

    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here

    def check_exist(self, arr, value):
        for i in range (0, len(arr)):
            if (value == arr[i]) :
                return True
        return False


    def add_vertex(self, vertex):
        if (self.check_exist(self.adjMatrix[0], vertex)):               #Checking for existance in the first row
            print("This value has already existed")
        else:
            copyAdjRow = self.adjMatrix[0]
            flag = True
            i = 1
            while (flag):                                               #Iterate through the first 
                if i > (self.size -1) :                                 #Check if there is space to add another vertex
                    print("There is no more space")
                    break
                if self.adjMatrix[0][i] == 0:                           #If the value hasnt been set
                    self.adjMatrix[0][i] = vertex                       #Set on the row
                    self.adjMatrix[i][0] = vertex                       #Set on the column
                    flag = False
                i+=1

    def add_edge(self, vertex1, vertex2):
        if (self.check_exist(self.adjMatrix[0], vertex1)) and (self.check_exist(self.adjMatrix[0], vertex2)):           #Check for existence of both the vertexes
            index1 = self.adjMatrix[0].index(vertex1)
            index2 = self.adjMatrix[0].index(vertex2)
            if self.adjMatrix[index1][index2] == 0:                                                                     #Check for edge existence
                self.adjMatrix[index1][index2] = 1
                self.adjMatrix[index2][index1] = 1
            else:
                print("The edge has already been added!")
        elif self.check_exist(self.adjMatrix[0], vertex1) == False :
            print("Cant add edge! The vertex [",vertex1,"] doesnt exist")
        else:
            print("Cant add edge! [",vertex2,"] doesnt exist")

    def remove_edge(self,vertex1, vertex2):
        if (self.check_exist(self.adjMatrix[0], vertex1)) and (self.check_exist(self.adjMatrix[0], vertex2)):           #Check for existence of both the vertexes
            index1 = self.adjMatrix[0].index(vertex1)
            index2 = self.adjMatrix[0].index(vertex2)
            if self.adjMatrix[index1][index2] == 1:                                                                     #Check for edge existence
                self.adjMatrix[index1][index2] = 0
                self.adjMatrix[index2][index1] = 0
            else:
                print("There is no connection between the 2 vetexes.")
        elif self.check_exist(self.adjMatrix[0], vertex1) == False :
            print("Cant remove edge! The vertex [",vertex1,"] doesnt exist")
        else:
            print("Cant remove edge! The vertex [",vertex2,"] doesnt exist")

    def printMatrix(self):
        line0 = "     "
        line1 = "     "
        for i in range (1, len(self.adjMatrix[0])):                             #Start with 1 because the first vertex's index is 1
            line0 += (str(self.adjMatrix[0][i]) +"     ")
            line1 += "-----"
        print(line0)
        print(line1)

        for i in range (1, len(self.adjMatrix)):
            line =""
            for j in range(0, len(self.adjMatrix[i])):
                if j == 0:
                    line += (str(self.adjMatrix[i][j]) +"|   ")
                else:
                    line += (str(self.adjMatrix[i][j]) +"     ")
            print(line,"\n")
            




#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)
def main():
        g = Graph(5)

        g.add_vertex(1)
        g.add_vertex(7)
        g.add_vertex(3)
        g.add_vertex(9)
        g.add_vertex(5)
        g.add_edge(1,7)
        g.printMatrix()




if __name__ == '__main__':
   main()
