import understand
import sys

func_list = []
final_list = []
function_list = []


def metric(file):
    file_metric = []
    metrics = file.metric(file.metrics())
    for k, v in sorted(metrics.items()):
        file_metric.append(v)

    return file_metric


def printCallPairs(ent):
    lineString = ''
    ret=[]
    for ref in sorted(ent.refs("call", "", True), key=lambda ref: ref.ent().name()):

        defineAref = ent.ref("definein")
        if defineAref is not None:
            lineString = ent.longname() + ","
            lineString += defineAref.file().longname() + ","
        #lineString += str(ref.line()) + ","

            callee = ref.ent()
            defineBref = callee.ref("definein");
            lineString = callee.longname()
            if defineBref is None:
                ret.append(lineString)
            else:
                name_qualify = str(defineBref.file().longname()).split('/')
                name_qualify = '.'.join(name_qualify[1:name_qualify.__len__()])
                temp=[]
                temp.append(name_qualify)
                temp.append(str(callee))
                ret.append('.'.join(temp[0:temp.__len__()]))
                #ret.append(lineString + defineBref.file().longname())
    return  ret


def CalledByFunc(name):
    called=[]
    for ref in sorted(ent.refs("call", "", True), key=lambda ref: ref.ent().name()):
        if ref.ent() == name:
            called.append(ent.longname())
    return called




if __name__ == '__main__':
  # Open Database
    args = sys.argv
  #db = understand.open(args[1])
    db = understand.open("/home/nazanin/cephDB.udb")

    for ent in sorted(db.ents("function ~unknown ~unresolved"),key= lambda ent: ent.name()):
        func_arr =[]
        name = ent.name()
        location = ent.ref("defined in")

        defineAref = ent.ref("definein")
        if defineAref is not None:
            lineString = ent.longname() + ","
            lineString += defineAref.file().longname() + ","

            func_arr = lineString.split(',')
            temp = func_arr[1].split('/')
            temp.append(func_arr[0])
            qname = '.'.join(temp[1:len(temp)])

            func_metric = metric(ent)
            #called functions
            function_list=(printCallPairs(ent))
            call = CalledByFunc(ent)
            print(function_list)

            func_list.append(func_arr[0])
            func_list.append(qname)
            func_list.append(func_arr[1])
            func_list.append(func_metric)
            func_list.append(function_list)
            func_list.append(call)

    final_list.append(func_list)


with open('Function Report.txt', 'w') as classhandle:
    i = 0

    for listitem in final_list[i]:
        classhandle.write('%s;' % listitem)
        i = i + 1
        if i % 6 == 0:            classhandle.write('\n')

