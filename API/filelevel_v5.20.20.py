import understand
import sys

final_set = []
report = []
db_func = []
file = []
class_db = []
db_cls = []
CallPairs=[]
cls_CallPairs=[]

include_dictionary=[]
def included():
    a_temp=[]
    b_temp=[]
    corpus = open("dependency.txt",'r')
    corpus = corpus.read()
    f =  (corpus.split('{'))
    print(f)
    i=0
    while i < f.__len__():
        temp = f[i].split('[')
        if temp != ['']:
            for list in temp:
                a_temp.append(list.split(' '))
            j1=0
            j=a_temp.__len__()
            for item in a_temp:
                le = 0
                while le < item.__len__():
                    if item[le]=='Include':
                        include_dictionary.append(item[le+2])
                        unc = item[le + 4].split('(')
                        include_dictionary.append(unc[0])
                        le = le +3
                    le = le + 1
        i = i +1
    print(f)


def include_file(file):
    i=0
    included=[]
    while i < include_dictionary.__len__():
        if include_dictionary[i]== file:
            included.append(include_dictionary[i+1])

        i = i + 2
    return included

def used_by_file(file):
    i = 1
    used = []
    while i < include_dictionary.__len__():
        if include_dictionary[i] == file:
            used.append(include_dictionary[i - 1])

        i = i + 2
    return used

def listfunctions(db):
    func_name=[]
    for func in db.ents("function"):
        func_name.append(func.longname())
    with open('functionlist.txt', 'w') as classhandle:
        i = 0

        for listitem in func_name:
            classhandle.write('%s;' % listitem)
            i = i + 1
            classhandle.write('\n')

class Cls:
  def __init__(self, name):
    self.name = name
    #self.address = address




def containedfunctions(db_file):
    i=4
    func_list=[]
    while i < CallPairs.__len__():
        if CallPairs[i] == '\n':
            c = CallPairs[i-1].split(',')
            if c.__len__()==6 and c[2]== db_file:
                b = c[2]
                func_list.append(c[0])
            if c.__len__()==5 and c[1]== db_file:
                func_list.append(c[0])

        i = i +1

    return func_list


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


def containedclasses(db_file):
    cls_name = []
    for cls in db.ents("class,Class,classes"):
        p1 = (str(cls.longname()))
        cls_name.append(cls.longname())
        cls_root_file = cls_name[0].split(":")
        if cls_root_file[0] == db_file:
            db_cls.append(cls)

    return cls_name


def metric(file):
    file_metric = []
    metrics = file.metric(file.metrics())
    for k, v in sorted(metrics.items()):
        file_metric.append(v)

    return file_metric


def fileList(file):
    file_qname = file.longname()
    file_name_Qualified = file_qname.split('/')
    last = file_name_Qualified[file_name_Qualified.__len__() - 1].split('.')
    location = ".".join(file_name_Qualified[0:file_name_Qualified.__len__() - 1])
    qlast = []
    qlast.append(location)
    qlast.append(last[0])
    file_name_Qualified = '.'.join(qlast[0:qlast.__len__()])

    return (file_name[0], file_name_Qualified, location)


def printCallPairs(ent):
    list_of_cls=[]
    for ref in sorted(ent.refs("call", "", True), key=lambda ref: ref.ent().name()):
        defineAref = ent.ref("definein")

        lineString = ent.longname() + "(\"" + str(ent.parameters()) + "\"),"
        lineString += defineAref.file().longname() + ","
        lineString += str(ref.line()) + ","

        callee = ref.ent()
        defineBref = callee.ref("definein");
        lineString += callee.longname() + "(\"" + str(callee.parameters()) + "\"),"
        if defineBref is None:
            return lineString
            continue
        return (lineString + defineBref.file().longname())



def cls_printCallPairs(ent):
    list_of_cls=[]
    for ref in sorted(ent.refs("call", "", True), key=lambda ref: ref.ent().name()):
        defineAref = ent.ref("definein")

        lineString = ent.longname() + "(\"" + str(ent.parameters()) + "\"),"
        lineString += defineAref.file().longname() + ","
        lineString += str(ref.line()) + ","

        callee = ref.ent()
        defineBref = callee.ref("definein");
        lineString += callee.longname() + "(\"" + str(callee.parameters()) + "\"),"
        if defineBref is None:
            return lineString
            continue
        return (lineString + defineBref.file().longname())


depe=[]
if __name__ == '__main__':

    # Open Database
    args = sys.argv
    included()
    #db = understand.open(sys.argv[1])
    db = understand.open("/home/nazanin/Downloads/Understand/scitools/bin/linux64/New.udb")
    listfunctions(db)
    print("Caller, Caller File, Call Line, Callee, Callee File\n")
    for ent in sorted(db.ents("function ~unknown ~unresolved"), key=lambda ent: ent.name()):
        seen = {}
        calls = printCallPairs(ent)
        #depe.append(ent.depends())
        if calls != None:
            CallPairs.append(calls)
            CallPairs.append("\n")
    for ent in sorted(db.ents("class"), key=lambda ent: ent.name()):
        seen = {}
        calls = cls_printCallPairs(ent)
        if calls != None:
            cls_CallPairs.append(calls)
            cls_CallPairs.append("\n")

   # print(CallPairs[0])
    for file in db.ents("File"):
        file_name = []

        file_qname = []
        a = understand.Ent.depends(file)
        print(file.depends())
        depe.append(file.depends())

        # If file is from the Ada Standard library, skip to next
        if file.library() != "Standard":
            file_name.append(file.name())
            name_qname_loc = fileList(file)
            db_analyze_pfix = file_name[0].split('.')


            # How to get long name????????
            cont_cls = containedclasses(db_analyze_pfix[0])
            cont_func = containedfunctions(file.longname())
            class_db.append(cont_cls)

            if len(db_analyze_pfix) > 1:
                file_lang = (Language(db_analyze_pfix[1]))
            file_metric = metric(file)

            inc_file = include_file(file.longname())
            used_by = used_by_file(file.longname())
        final_set.append(name_qname_loc[0])
        final_set.append(file_lang)
        final_set.append(name_qname_loc[1])
        final_set.append(name_qname_loc[2])
        final_set.append(file_metric)
        final_set.append(cont_func)
        final_set.append(cont_cls)
        final_set.append(inc_file)
        final_set.append(used_by)
        #final_set.append(CallPairs)
        report.append(final_set)

File_header = []
File_header = ['Name', 'ProgrammingLanguage', 'qualifiedName', 'location', 'Lines', 'CommentLines', 'BlankLines',
               'PreprocessorLines', 'CodeLines', 'InactiveLines', 'ExecutableCodeLines', 'DeclarativeCodeLines',
               'ExecutionStatements', 'DeclarationStatements', 'RatioComment/Code', 'Units', 'containedClasses',
               'containedFunctions', 'usesSourceFiles', 'usedbySourceFiles']
# report.insert(0,File_header)


with open('FileLevel Report.txt', 'w') as classhandle:
    i = 0

    for listitem in report[i]:
        classhandle.write('%s;' % listitem)
        i = i + 1
        if i % 9 == 0:            classhandle.write('\n')

with open('dependency.txt', 'w') as classhandle:
        i = 0

        for listitem in depe:
            classhandle.write('%s;' % listitem)
            i = i + 1
            classhandle.write('\n')