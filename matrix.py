class matrix:
    def __init__(self,rows,col):
        self.rows=rows
        self.col=col
        self.data=[]
    def input_matrix(self):
        print("enter matrix element")
        for i in range(self.rows):
            row=list(map(int,input().split()))
            self.data.append(row)
    def display(self):
        print("matrix")
        for row in self.data:
            print(row)
m=matrix(2,2)
m.input_matrix()
m.display()                  
