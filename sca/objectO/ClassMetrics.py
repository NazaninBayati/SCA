import understand
import MainMetrics

lis={}
class_dependency={}
class_dependentby={}
db = MainMetrics.Metrics.DBlodb("/home/nazanin/cephDB.udb")

class classMetrics(MainMetrics.Metrics):
    def used_classes(self,db):
        self.db = db
        for cls in sorted(db.ents("Class")):
            if str(cls.name()) not in class_dependency:
                class_dependency[str(cls.name())] = []
            for item in cls.depends():
                kindname = str(item.kindname()).split(' ')
                if 'Class' in kindname:
                    scissor = str(item).split('@')
                    class_dependency[str(cls.name())].append((scissor[0]))

    def used_by_classes(self,db):
        self.db = db
        for cls in sorted(db.ents("Class")):
            if str(cls.name()) not in class_dependentby:
                class_dependentby[str(cls.name())] = []
            for item in cls.dependsby():
                kindname = str(item.kindname()).split(' ')
                if 'Class' in kindname:
                    scissor = str(item).split('@')
                    class_dependentby[str(cls.name())].append((scissor[0]))

    def called_classes(self,cls_name):
        if str(cls_name) in class_dependency:
            return class_dependency[str(cls_name)]

    def called_by_classes(self,cls_name):
        if str(cls_name) in class_dependentby:
            return class_dependentby[str(cls_name)]


    def cls_printCallPairs(self,ent):
        self.ent = ent
        lineString = ''
        defineAref = self.ent.ref("definein")
        if defineAref is not None:
            lineString = self.ent.longname() + ","
            lineString += defineAref.file().longname()

        return lineString


    def list_func(self,db):
        self.db = db
        linestring = ''
        for ent in sorted(self.db.ents("Function"), key=lambda ent: ent.name()):
            linestring = str(ent.name()) + ','
            linestring += str(ent.parent())
            if ent.parent() is not None:
                if (str(ent.parent()) not in  lis):

                    lis[str(ent.parent())]=[]
                lis[str(ent.parent())].append(str(ent.name()))


                #lis.append(linestring)

    def cont_func(self,cls):
        if str(cls) in lis:
            return lis[str(cls)]
        else: return ' '




    def main(self,db):
        self.db = db

        counter=0

        class_list = []
        cls_final_list = []

        if __name__ == '__main__':

            classMetrics.list_func(self, db)
            classMetrics.used_classes(self, db)
            classMetrics.used_by_classes(self, db)
            for ent in sorted(db.ents("class"), key=lambda ent: ent.name()):
                def_str=''
                end_str=''
                cls_qname_temp = []
                cls_name = classMetrics.cls_printCallPairs(self,ent)
                if cls_name != '':
                    for ref in ent.refs("define"):
                        def_str = str(ref.line())
                    for ref in ent.refs("End"):
                        end_str = str(ref.line())

                    temp = cls_name.split(',')
                    temp2 = temp[1].split('.')
                    temp3 = temp2[0].split('/')
                    cls_qname = '.'.join(temp3[0:temp3.__len__()])
                    cls_qname_temp.append(cls_qname)
                    cls_qname_temp.append(temp[0])

                    cls_qname = '.'.join(cls_qname_temp[0:cls_qname_temp.__len__()])

                    cls_metric = classMetrics.metric_val(self,ent)
                    if cls_metric.__len__()<20:
                        cls_metric = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None',
                                       'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None',
                                       'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None',
                                       'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None',
                                       'None', 'None']

                    contained_func = classMetrics.cont_func(self,ent.name())
                    call_class = classMetrics.called_classes(self,ent.name())
                    call_by_class = classMetrics.called_by_classes(self,ent.name())


                    class_list.append(ent.name())
                    class_list.append(def_str)
                    class_list.append(end_str)
                    class_list.append(cls_qname)
                    class_list.append(temp2[0])
                    class_list.append(cls_metric[0])
                    class_list.append(cls_metric[1])
                    class_list.append(cls_metric[2])
                    class_list.append(cls_metric[3])
                    class_list.append(cls_metric[4])
                    class_list.append(cls_metric[5])
                    class_list.append(cls_metric[6])
                    class_list.append(cls_metric[7])
                    class_list.append(cls_metric[8])
                    class_list.append(cls_metric[9])
                    class_list.append(cls_metric[10])
                    class_list.append(cls_metric[11])
                    class_list.append(cls_metric[12])
                    class_list.append(cls_metric[13])
                    class_list.append(cls_metric[14])
                    class_list.append(cls_metric[15])
                    class_list.append(cls_metric[16])
                    class_list.append(cls_metric[17])
                    class_list.append(cls_metric[18])
                    class_list.append(cls_metric[19])
                    class_list.append(cls_metric[20])
                    class_list.append(cls_metric[21])
                    class_list.append(cls_metric[22])
                    class_list.append(cls_metric[23])
                    class_list.append(cls_metric[24])
                    class_list.append(cls_metric[25])
                    class_list.append(cls_metric[26])
                    class_list.append(cls_metric[27])
                    class_list.append(cls_metric[28])
                    class_list.append(cls_metric[29])
                    class_list.append(cls_metric[30])
                    class_list.append(cls_metric[31])
                    class_list.append(cls_metric[32])
                    class_list.append(cls_metric[33])
                    class_list.append(cls_metric[34])
                    class_list.append(cls_metric[35])
                    class_list.append(cls_metric[36])
                    class_list.append(cls_metric[37])
                    class_list.append(cls_metric[38])
                    class_list.append(contained_func)
                    class_list.append(call_class)
                    class_list.append(call_by_class)

                    counter = counter+1


            cls_final_list.append(class_list)
            cls_final_list.append(counter)
            name = 'Class Level Report.txt'
            header='ClassName,StartLine,EndLine,QualifiedName,Location,AltAvgLineBlank,AltAvgLineCode,AltAvgLineComment,AltCountLineBlank,AltCountLineCode,AltCountLineComment,AvgCyclomatic,AvgCyclomaticModified,AvgCyclomaticStrict,AvgEssential,AvgLine,AvgLineBlank,AvgLineCode,AvgLineComment,CountDeclClass,CountDeclFunction,CountLine,CountLineBlank,CountLineCode,CountLineCodeDecl,CountLineCodeExe,CountLineComment,CountLineInactive,CountLinePreprocessor,CountSemicolon,CountStmt,CountStmtDecl,CountStmtEmpty,CountStmtExe,MaxCyclomatic,MaxCyclomaticModified,MaxCyclomaticStrict,MaxEssential,MaxNesting,RatioCommentToCode,SumCyclomatic,SumCyclomaticModified,SumCyclomaticStrict,SumEssential,ContainedFunctionS,CalledClasses,CalledByClasses'
            iterator = 47
            MainMetrics.Metrics.printresult(name,cls_final_list,iterator,header)

    def __init__(self):
        MainMetrics.Metrics.__init__(self)
        self.db = db
        classMetrics.main(self,db)

P1 = classMetrics()