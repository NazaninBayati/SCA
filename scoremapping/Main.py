class Main:
    def Structural_data_load(args):
        #args, 'r'

        structural_dependency = open( '/home/nazanin/PycharmProjects/objectO/fils.csv')
        structural_dependency = structural_dependency.read()
        return structural_dependency

    def Logical_data_load(args):
        #args
        logical_dependency = open('/home/nazanin/PycharmProjects/ARM/result.txt')
        logical_dependency = logical_dependency.read()
        return logical_dependency
