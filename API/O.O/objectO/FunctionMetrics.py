import understand
import sys
import MainMetrics


db = MainMetrics.Metrics.DBlodb("/home/nazanin/cephDB.udb")


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
                defineBref = callee.ref("definein");
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
                    # ret.append(lineString + defineBref.file().longname())
        return ret

    def CalledByFunc(self,name):
        self.name = name
        called = []
        for ref in sorted(self.ent.refs("call", "", True), key=lambda ref: ref.ent().name()):
            if ref.ent() == name:
                called.append(self.ent.longname())
        return called

    def __init__(self):

        func_list = []
        func_final_list = []
        function_list = []


        counter=0

        MainMetrics.Metrics.__init__(self)
        self.db = db
        for ent in sorted(db.ents("function ~unknown ~unresolved"), key=lambda ent: ent.name()):
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


                func_list.append(func_arr[0])
                func_list.append(def_str)
                func_list.append(end_str)
                func_list.append(qname)
                func_list.append(func_arr[1])
                func_list.append(func_metric[0])
                func_list.append(func_metric[1])
                func_list.append(func_metric[2])
                func_list.append(func_metric[3])
                func_list.append(func_metric[4])
                func_list.append(func_metric[5])
                func_list.append(func_metric[6])
                func_list.append(func_metric[7])
                func_list.append(func_metric[8])
                func_list.append(func_metric[9])
                func_list.append(func_metric[10])
                func_list.append(func_metric[11])
                func_list.append(func_metric[12])
                func_list.append(func_metric[13])
                func_list.append(func_metric[14])
                func_list.append(func_metric[15])
                func_list.append(func_metric[16])
                func_list.append(func_metric[17])
                func_list.append(func_metric[18])
                func_list.append(func_metric[19])
                func_list.append(func_metric[20])
                func_list.append(func_metric[21])
                func_list.append(func_metric[22])
                func_list.append(func_metric[23])
                func_list.append(func_metric[24])
                func_list.append(func_metric[25])
                func_list.append(func_metric[26])
                func_list.append(func_metric[27])
                func_list.append(func_metric[28])


                func_list.append(function_list)
                func_list.append(call)


                counter = counter+1

        func_final_list.append(func_list)
        func_final_list.append(counter)

        name = 'Function Level Report.txt'
        header = 'FunctionName,StartLine,EndLine,Qualifiedname,Location,AltCountLineBlank,AltCountLineCode,AltCountLineComment,CountInput,CountLine,CountLineBlank,CountLineCode,CountLineCodeDecl,CountLineCodeExe,CountLineComment,CountLineInactive,CountLinePreprocessor,CountOutput,CountPath,CountPathLog,CountSemicolon,CountStmt,CountStmtDecl,CountStmtEmpty,CountStmtExe,Cyclomatic,CyclomaticModified,CyclomaticStrict,Essential,Knots,MaxEssentialKnots,MaxNesting,MinEssentialKnots,RatioCommentToCode,CalledFunctions,CalledByFunctions'
        iterator = 36
        MainMetrics.Metrics.printresult(name, func_final_list, iterator, header)

P1 = FunctionMetrics()

