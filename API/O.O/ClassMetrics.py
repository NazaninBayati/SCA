import understand
import MainMetrics

class_list=[]
cls_final_list=[]
lis=[]

db = MainMetrics.Metrics.DBlodb("/home/nazanin/cephDB.udb")

class classMetrics(MainMetrics.Metrics):
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
                lis.append(linestring)

    def cont_func(self,cls):
        i = 0
        self.cls = cls
        function_list = []
        while i < lis.__len__():
            temp = lis[i].split(',')
            function_name = temp[0]
            parent = temp[1]
            if parent == str(self.cls):
                function_list.append(function_name)
            i = i + 1
        return function_list

    def __init__(self):
        MainMetrics.Metrics.__init__(self)
        self.db = db

        if __name__ == '__main__':

            classMetrics.list_func(self, db)
            for ent in sorted(db.ents("class"), key=lambda ent: ent.name()):

                cls_qname_temp = []
                cls_name = classMetrics.cls_printCallPairs(self,ent)
                if cls_name != '':
                    temp = cls_name.split(',')
                    temp2 = temp[1].split('.')
                    temp3 = temp2[0].split('/')
                    cls_qname = '.'.join(temp3[0:temp3.__len__()])
                    cls_qname_temp.append(cls_qname)
                    cls_qname_temp.append(temp[0])

                    cls_qname = '.'.join(cls_qname_temp[0:cls_qname_temp.__len__()])

                    cls_metric = classMetrics.metric_val(self,ent)
                    contained_func = classMetrics.cont_func(self,ent)

                    class_list.append(ent.name())
                    class_list.append(cls_qname)
                    class_list.append(temp2[0])
                    class_list.append(cls_metric)
                    class_list.append(contained_func)

            cls_final_list.append(class_list)
            name = 'Class Level Report.txt'
            header=''
            iterator = 5
            MainMetrics.Metrics.printresult(name,cls_final_list,iterator,header)


P1 = classMetrics()