import understand
import sys

final_set = []
report = []
db_func = []
file = []
class_db = []
db_cls = []

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


def containedfunctions(db_file):
    func_name = []
    for func in db.ents("function"):

        func_name = (func.longname())
        func_root_file = func_name.split(":")
        if func_root_file[0] == db_file:
            db_func.append(func)

    return db_func


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
    CallPairs=[]
    # Open Database
    args = sys.argv
    #db = understand.open(sys.argv[1])
    db = understand.open("/home/nazanin/Downloads/Understand/scitools/bin/linux64/New.udb")
    listfunctions(db)
    print("Caller, Caller File, Call Line, Callee, Callee File\n")
    for ent in sorted(db.ents("function ~unknown ~unresolved"), key=lambda ent: ent.name()):
        seen = {}
        calls = printCallPairs(ent)
        if calls != None:
            CallPairs.append(calls)
            CallPairs.append("\n")

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
            cont_func = containedfunctions(db_analyze_pfix[0])

            # How to get long name????????
            cont_cls = containedclasses(db_analyze_pfix[0])
            class_db.append(cont_cls)

            if len(db_analyze_pfix) > 1:
                file_lang = (Language(db_analyze_pfix[1]))
            file_metric = metric(file)

        final_set.append(name_qname_loc[0])
        final_set.append(file_lang)
        final_set.append(name_qname_loc[1])
        final_set.append(name_qname_loc[2])
        final_set.append(file_metric)
        final_set.append(cont_func)
        final_set.append(cont_cls)
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
        if i % 7 == 0:            classhandle.write('\n')

with open('dependency.txt', 'w') as classhandle:
        i = 0

        for listitem in depe:
            classhandle.write('%s;' % listitem)
            i = i + 1
            classhandle.write('\n')