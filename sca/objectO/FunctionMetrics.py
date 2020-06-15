import understand
import sys
import MainMetrics


class FunctionMetrics(MainMetrics.Metrics):

    def printCallPairs(self,ent):
        self.ent = ent
        lineString = ''
        ret = []
        for ref in sorted(ent.refs("call", "", True), key=lambda ref: ref.ent().name()):

            defineAref = ent.ref("definein")
            if defineAref is not None:
                lineString = ent.longname() + ","
                lineString += defineAref.file().longname() + ","
                # lineString += str(ref.line()) + ","

                callee = ref.ent()
                defineBref = callee.ref("definein")
                lineString = callee.longname()
                if defineBref is None:
                    ret.append(lineString)
                else:
                    name_qualify = str(defineBref.file().longname()).split('/')
                    name_qualify = '.'.join(name_qualify[1:name_qualify.__len__()])
                    temp = []
                    temp.append(name_qualify)
                    temp.append(str(callee))
                    ret.append('.'.join(temp[0:temp.__len__()]))

        return ret

    def CalledByFunc(self,name):
        self.name = name
        called = []
        for ref in sorted(self.ent.refs("call", "", True), key=lambda ref: ref.ent().name()):
            if ref.ent() == name:
                called.append(self.ent.longname())
        return called


    def main(self,db,func_list, func_final_list,function_list):
        self.db = db
        self.func_list = func_list
        self.func_final_list = func_final_list
        self.function_list = function_list
        for ent in sorted(db.ents("function, Method"), key=lambda ent: ent.name()):
            #, ~unknown, ~unresolved
            func_arr = []
            name = ent.name()
            location = ent.ref("defined in")
            def_str=''
            end_str=''
            defineAref = ent.ref("definein")
            if defineAref is not None:

                for ref in ent.refs("define"):
                    def_str = str(ref.line())
                for ref in ent.refs("End"):
                    end_str = str(ref.line())

                lineString = ent.longname() + ","
                lineString += defineAref.file().longname() + ","

                func_arr = lineString.split(',')
                temp = func_arr[1].split('/')
                temp.append(func_arr[0])
                qname = '.'.join(temp[1:len(temp)])

                func_metric = MainMetrics.Metrics.metric_val(self,ent)
                if func_metric.__len__()<20:
                    func_metric = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None',
                                   'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None',
                                   'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None',
                                   'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None',
                                   'None', 'None']

                # called functions
                function_list = FunctionMetrics.printCallPairs(self,ent)
                call = FunctionMetrics.CalledByFunc(self,ent)
                print(func_metric.__len__())

                func_list.append(func_arr[0])
                func_list.append(def_str)
                func_list.append(end_str)
                func_list.append(qname)
                func_list.append(func_arr[1])

                jj=0
                while jj < func_metric.__len__():
                    func_list.append(func_metric[jj])
                    jj = jj +1

                func_list.append(function_list)
                func_list.append(call)
                iterator = jj + 7

        func_final_list.append(func_list)

        name = 'Java Function Report.txt'
        header = 'FunctionName,StartLine,EndLine,Qualifiedname,Location,AltCountLineBlank,AltCountLineCode,AltCountLineComment,CountInput,CountLine,CountLineBlank,CountLineCode,CountLineCodeDecl,CountLineCodeExe,CountLineComment,CountLineInactive,CountLinePreprocessor,CountOutput,CountPath,CountPathLog,CountSemicolon,CountStmt,CountStmtDecl,CountStmtEmpty,CountStmtExe,Cyclomatic,CyclomaticModified,CyclomaticStrict,Essential,Knots,MaxEssentialKnots,MaxNesting,MinEssentialKnots,RatioCommentToCode,CalledFunctions,CalledByFunctions'
        MainMetrics.Metrics.printresult(name, func_final_list, iterator, header)

    def __init__(self):

        func_list = []
        func_final_list = []
        function_list = []
        args = sys.argv[1]
        db = MainMetrics.Metrics.DBlodb(str(args))
        MainMetrics.Metrics.__init__(self)
        self.db = db
        FunctionMetrics.main(self,db,func_list, func_final_list,function_list)

P1 = FunctionMetrics()

