import understand
import sys

file_list=[]
final_list=[]
file_dependency=[]
file_dependentby=[]
cls_CallPairs=[]
CallPairs=[]


def included_files(db):
    for file in sorted(db.ents("File")):
       file_dependency.append(list(file.depends()))

def used_by_file(db):
    for file in sorted(db.ents("File")):
       file_dependentby.append(list(file.dependsby()))


def file_dependency_list(file):
    i = 0
    dep_list=[]
    while i < len(file_dependency):
        j = 1
        while j < len(file_dependency[i]):
            if file_dependency[i][0]==file:

                dep_list.append(str(file_dependency[i][j]))
            j = j +1
        i = i + 1

    return dep_list

def file_dependent_list(file):
    i = 0
    dep_list=[]
    while i < len(file_dependentby):
        j = 1
        while j < len(file_dependentby[i]):
            if file_dependentby[i][0]==file:
                dep_list.append(str(file_dependentby[i][j]))
            j = j +1
        i = i + 1
    return dep_list


def Language(pfix):
    pfix = pfix[0]
    db_analyze_language = ''
    if pfix == 'cpp' or pfix == 'h' or pfix == 'C' or pfix == 'hpp' or pfix == 'hxx' or pfix == 'cxx' or \
            pfix == 'H' or pfix == 'inl' or pfix == 'cc' or pfix == 'hh':
        db_analyze_language = 'C++'
    if pfix == 'c':
        db_analyze_language = 'C'
    if pfix == 'a' or pfix == 'ads' or pfix == 'gpr' or pfix == 'ada' or pfix == 'adb_analyze':
        db_analyze_language = 'Ada'
    if pfix == 'cgi' or pfix == 'pl' or pfix == 'pm':
        db_analyze_language = 'Perl'
    if pfix == 'css':
        db_analyze_language = 'CSS'
    if pfix == 'dpr' or pfix == 'dfm':
        db_analyze_language = 'Delphi'
    if pfix == 'f77' or pfix == 'f' or pfix == 'f90' or pfix == 'for' or pfix == 'f03' or \
            pfix == 'f95' or pfix == 'ftn':
        db_analyze_language = 'Fortran'
    if pfix == 'jov' or pfix == 'cpl':
        db_analyze_language = 'Jovidal'
    if pfix == 'mm':
        db_analyze_language = 'Objective-C++'
    if pfix == 'py':
        db_analyze_language = 'Python'
    if pfix == 'sql':
        db_analyze_language = 'Sql'
    if pfix == 'tsx' or pfix == 'ts':
        db_analyze_language = 'TypeScript'
    if pfix == 'vb':
        db_analyze_language = 'Basic'
    if pfix == 'vhdl' or pfix == 'vhd':
        db_analyze_language = 'VHDL'
    if pfix == 'asm' or pfix == 's':
        db_analyze_language = 'Assembly'
    if pfix == 'cbl' or pfix == 'cob' or pfix == 'cpy':
        db_analyze_language = 'COBOL'
    if pfix == 'htm' or pfix == 'html':
        db_analyze_language = 'Html'
    if pfix == 'js':
        db_analyze_language = 'Javascript'
    if pfix == 'pas' or pfix == 'sp':
        db_analyze_language = 'Pascal'
    if pfix == 'plm':
        db_analyze_language = 'Plm'
    if pfix == 'tcl':
        db_analyze_language = 'Tcl'
    if pfix == 'txt' or pfix == 'TXT':
        db_analyze_language = 'Text'
    if pfix == 'vh' or pfix == 'v':
        db_analyze_language = 'Verilog'
    if pfix == 'xml':
        db_analyze_language = 'Xml'
    if pfix == 'bat':
        db_analyze_language = 'MSDos Batch'
    if pfix == 'cs':
        db_analyze_language = 'C#'
    if pfix == 'java':
        db_analyze_language = 'Java'
    if pfix == 'm':
        db_analyze_language = 'Objective-C'
    if pfix == 'php':
        db_analyze_language = 'Php'
    return db_analyze_language


def fileList(file):
    location=[]
    last2=[]
    file_qname = file.longname()
    file_name_Qualified = file_qname.split('/')
    location.append(file_qname)
    last = file_name_Qualified[file_name_Qualified.__len__() - 1].split('.')
    last2.append(file_name_Qualified[0:len(file_name_Qualified)-1])
    last2[0].append(last[0])
    last2=last2[0]
    last = ".".join(last2[1:last2.__len__()])
    qlast = []
    qlast.append(location[0])
    qlast.append(last)
    file_name_Qualified = '.'.join(qlast[1:qlast.__len__()-1])

    return (qlast[1], location[0])




def cls_printCallPairs(ent):

    lineString = ''
    defineAref = ent.ref("definein")
    if defineAref is not None:
            lineString = ent.longname() + ","
            lineString += defineAref.file().longname()

    return lineString


def printCallPairs(ent):
    lineString = ''
    defineAref = ent.ref("definein")
    if defineAref is not None:
            lineString = ent.longname() + ","
            lineString += defineAref.file().longname()

    return lineString



def class_cont(file):
    list_ret = []
    for item in cls_CallPairs:
        list_cls = item.split(',')
        if list_cls[1] == str(file.longname()):
            list_ret.append(list_cls[0])
    return list_ret


def function_cont(file):
    list_ret = []
    for item in CallPairs:
        list_func = item.split(',')
        if list_func[1] == str(file.longname()):
            list_ret.append(list_func[0])
    return list_ret




def metric(file):
    file_metric = []
    metrics = file.metric(file.metrics())
    for k, v in sorted(metrics.items()):
        file_metric.append(v)

    return file_metric





if __name__ == '__main__':
    # Open Database
    args = sys.argv
    # db = understand.open(args[1])
    db = understand.open("/home/nazanin/cephDB.udb")
    included_files(db)
    used_by_file(db)

    for ent in sorted(db.ents("class,method,struct,procedure"), key=lambda ent: ent.name()):
        seen = {}
        calls = cls_printCallPairs(ent)
        if calls != '':
            cls_CallPairs.append(calls)


    for ent in sorted(db.ents("function ~unknown ~unresolved"), key=lambda ent: ent.name()):
        seen = {}
        calls = printCallPairs(ent)
        if calls != '':
            CallPairs.append(calls)



    for file in sorted(db.ents("File")):

        if file.library() != "Standard":
           file_name=(file.name())
           db_analyze_pfix = file_name.split('.')
           if len(db_analyze_pfix) > 1:
               file_lang = (Language(db_analyze_pfix[1]))
           name_qname_loc = fileList(file)
           file_metric = metric(file)

           contained_classes = class_cont(file)
           contained_function = function_cont(file)
           dep = (file_dependency_list(file))
           depBy = (file_dependent_list(file))





           file_list.append(str(file.name()))
           file_list.append(file_lang)
           file_list.append(name_qname_loc[0])
           file_list.append(name_qname_loc[1])
           file_list.append(file_metric)
           file_list.append(contained_function)
           file_list.append(contained_classes)
           file_list.append(dep)
           file_list.append(depBy)

    final_list.append(file_list)

print(final_list)
header = 'Filename,ProgrammingLanguage,FileQualifiedname,Location,Metrics,ContainedFunctions,ContainedClasses,calledFiles,CalledByFiles'
with open('FileLevel Report.txt', 'w') as classhandle:
    i = 0
    classhandle.write(header)
    classhandle.write('\n')
    for listitem in file_list:
        classhandle.write('%s;' % listitem)
        i = i + 1
        if i % 9 == 0:            classhandle.write('\n')
