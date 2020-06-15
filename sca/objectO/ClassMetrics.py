import understand
import sys
import MainMetrics


class classMetrics(MainMetrics.Metrics):
    def used_classes(self,db,class_dependency):
        self.db = db
        self.class_dependency = class_dependency
        for cls in sorted(db.ents("Class")):
            if str(cls.name()) not in class_dependency:
                class_dependency[str(cls.name())] = []
            for item in cls.depends():
                kindname = str(item.kindname()).split(' ')
                if 'Class' in kindname:
                    scissor = str(item).split('@')
                    class_dependency[str(cls.name())].append((scissor[0]))

    def used_by_classes(self,db, class_dependentby):
        self.db = db
        self.class_dependency = class_dependentby
        for cls in sorted(db.ents("Class")):
            if str(cls.name()) not in class_dependentby:
                class_dependentby[str(cls.name())] = []
            for item in cls.dependsby():
                kindname = str(item.kindname()).split(' ')
                if 'Class' in kindname:
                    scissor = str(item).split('@')
                    class_dependentby[str(cls.name())].append((scissor[0]))

    def called_classes(self,cls_name,class_dependency):
        if str(cls_name) in class_dependency:
            return class_dependency[str(cls_name)]

    def called_by_classes(self,cls_name,class_dependentby):
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


    def list_func(self,db,lis):
        self.db = db
        self.lis=lis
        linestring = ''
        for ent in sorted(self.db.ents("Function"), key=lambda ent: ent.name()):
            linestring = str(ent.name()) + ','
            linestring += str(ent.parent())
            if ent.parent() is not None:
                if (str(ent.parent()) not in  lis):

                    lis[str(ent.parent())]=[]
                lis[str(ent.parent())].append(str(ent.name()))


    def cont_func(self,cls,lis):
        if str(cls) in lis:
            return lis[str(cls)]
        else: return ' '


    def main(self,db,lis,class_dependency,class_dependentby,class_list,cls_final_list):
        self.db = db
        self.lis = lis
        self.class_dependency = class_dependency
        self.class_dependentby = class_dependentby
        self.class_list = class_list
        self.cls_final_list = cls_final_list




        classMetrics.list_func(self, db,lis)
        classMetrics.used_classes(self, db,class_dependency)
        classMetrics.used_by_classes(self, db,class_dependentby)
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

                contained_func = classMetrics.cont_func(self,ent.name(),lis)
                call_class = classMetrics.called_classes(self,ent.name(),class_dependency)
                call_by_class = classMetrics.called_by_classes(self,ent.name(),class_dependentby)


                class_list.append(ent.name())
                class_list.append(def_str)
                class_list.append(end_str)
                class_list.append(cls_qname)
                class_list.append(temp2[0])
                jj=0
                while jj <  cls_metric.__len__():
                    class_list.append(cls_metric[jj])
                    jj = jj + 1

                class_list.append(contained_func)
                class_list.append(call_class)
                class_list.append(call_by_class)

        print("Class level done!")
        cls_final_list.append(class_list)

        name = 'Class report.txt'
        header='ClassName,StartLine,EndLine,QualifiedName,Location,AltAvgLineBlank,AltAvgLineCode,AltAvgLineComment,AltCountLineBlank,AltCountLineCode,AltCountLineComment,AvgCyclomatic,AvgCyclomaticModified,AvgCyclomaticStrict,AvgEssential,AvgLine,AvgLineBlank,AvgLineCode,AvgLineComment,CountDeclClass,CountDeclFunction,CountLine,CountLineBlank,CountLineCode,CountLineCodeDecl,CountLineCodeExe,CountLineComment,CountLineInactive,CountLinePreprocessor,CountSemicolon,CountStmt,CountStmtDecl,CountStmtEmpty,CountStmtExe,MaxCyclomatic,MaxCyclomaticModified,MaxCyclomaticStrict,MaxEssential,MaxNesting,RatioCommentToCode,SumCyclomatic,SumCyclomaticModified,SumCyclomaticStrict,SumEssential,ContainedFunctionS,CalledClasses,CalledByClasses'
        iterator = jj + 6
        MainMetrics.Metrics.printresult(name,cls_final_list,iterator,header)

    def __init__(self):

        args = sys.argv[1]
        db = MainMetrics.Metrics.DBlodb(str(args))
        self.db = db
        MainMetrics.Metrics.__init__(self)
        lis = {}
        class_dependency = {}
        class_dependentby = {}
        class_list = []
        cls_final_list = []
        classMetrics.main(self,db,lis,class_dependency,class_dependentby,class_list,cls_final_list)


P1 = classMetrics()