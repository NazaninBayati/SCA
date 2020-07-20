class Main:
    def Structural_data_load(args):
        #args, 'r'

        structural_dependency = open( 'fils.csv')
        structural_dependency = structural_dependency.read()
        return structural_dependency

    def Logical_data_load(args):
        #args
        logical_dependency = open('res.txt')
        logical_dependency = logical_dependency.read()
        return logical_dependency

    def write(self,file_structural):
        self.file_structural = file_structural
        with open('MergedList.txt', 'w')as handler:
            for i in (file_structural):
                handler.write(i)
                handler.write(":")
                handler.write(str(file_structural[str(i)]))
                handler.write('\n')
