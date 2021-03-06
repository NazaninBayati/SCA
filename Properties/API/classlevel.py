import understand
import sys

class_list=[]
final_list=[]
lis=[]

def cls_printCallPairs(ent):

    lineString = ''
    defineAref = ent.ref("definein")
    if defineAref is not None:
            lineString = ent.longname() + ","
            lineString += defineAref.file().longname()

    return lineString


def metric(ent):
    cls_metric = []
    metrics = ent.metric(ent.metrics())
    for k, v in sorted(metrics.items()):
        cls_metric.append(v)

    return cls_metric


def list_func(db):
    linestring=''
    for ent in sorted(db.ents("Function"), key=lambda ent: ent.name()):
        linestring = str(ent.name()) + ','
        linestring += str(ent.parent())
        if ent.parent() is not None:
            lis.append(linestring)



def cont_func(cls):
    i=0
    function_list = []
    while i < lis.__len__():
        temp = lis[i].split(',')
        function_name = temp[0]
        parent = temp[1]
        if parent == str(cls):
            function_list.append(function_name)
        i = i + 1
    return function_list



if __name__ == '__main__':
    # Open Database
    args = sys.argv
    # db = understand.open(args[1])
    db = understand.open("/home/nazanin/cephDB.udb")
    list_func(db)
    for ent in sorted(db.ents("class"), key=lambda ent: ent.name()):
        seen = {}
        cls_qname_temp=[]
        cls_name = cls_printCallPairs(ent)
        if cls_name != '':
            temp = cls_name.split(',')
            temp2 =temp[1].split('.')
            temp3 = temp2[0].split('/')
            cls_qname = '.'.join(temp3[0:temp3.__len__()])
            cls_qname_temp.append(cls_qname)
            cls_qname_temp.append(temp[0])

            cls_qname = '.'.join(cls_qname_temp[0:cls_qname_temp.__len__()])

            cls_metric = metric(ent)
            contained_func = cont_func(ent)





            class_list.append(ent.name())
            class_list.append(cls_qname)
            class_list.append(temp2[0])
            class_list.append(cls_metric)
            class_list.append(contained_func)

    final_list.append(class_list)
    print(final_list)




with open('ClassLevel Report.txt', 'w') as classhandle:
    i = 0

    for listitem in final_list[i]:
        classhandle.write('%s;' % listitem)
        i = i + 1
        if i % 5 == 0:            classhandle.write('\n')

