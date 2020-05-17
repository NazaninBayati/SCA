import understand
import sys


final_set=[]
report=[]
list_db = []
checklist = []
db_func=[]
def containedfunctions(db_file):
    func_name = []
    for func in db.ents("function"):

        func_name.append(func.longname())
        func_root_file = func_name[0].split(":")
        if func_root_file[0] == db_file:
            db_func.append(func)
        print(func_name)
    return db_func


def containedclasses():
    cls_name = []
    for cls in db.ents("class,Class,classes"):

        cls_name.append(cls.longname())
        print(cls_name)
    return cls_name


def fileList(db):
    for file in db.ents("File"):
        file_name = []
        file_qname = []
        # If file is from the Ada Standard library, skip to next
        if file.library() != "Standard":
            file_name.append(file.name())

            db_analyze_pfix = file_name[0].split('.')
            cont_func = containedfunctions(db_analyze_pfix[0])
            if len(db_analyze_pfix)>1 and( db_analyze_pfix[1] == 'cpp' or db_analyze_pfix[1] == 'h' or db_analyze_pfix[1] == 'C' or \
                    db_analyze_pfix[1] == 'hpp' or db_analyze_pfix[1] == 'hxx' or db_analyze_pfix[1] == 'cxx' or \
                    db_analyze_pfix[1] == 'H' or db_analyze_pfix[1] == 'inl' or db_analyze_pfix[1] == 'cc' or \
                    db_analyze_pfix[1] == 'hh'):
                    db_analyze_language = 'C++'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'c':
                    db_analyze_language = 'C'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'a' or db_analyze_pfix[1] == 'ads' or db_analyze_pfix[1] == 'gpr' or \
                        db_analyze_pfix[1] == 'ada' or db_analyze_pfix[1] == 'adb_analyze'):
                    db_analyze_language = 'Ada'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'cgi' or db_analyze_pfix[1] == 'pl' or db_analyze_pfix[1] == 'pm'):
                    db_analyze_language = 'Perl'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'css'):
                    db_analyze_language = 'CSS'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'dpr' or db_analyze_pfix[1] == 'dfm'):
                    db_analyze_language = 'Delphi'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'f77' or db_analyze_pfix[1] == 'f' or db_analyze_pfix[1] == 'f90' or \
                    db_analyze_pfix[1] == 'for' or db_analyze_pfix[1] == 'f03' or db_analyze_pfix[1] == 'f95' or \
                    db_analyze_pfix[1] == 'ftn'):
                    db_analyze_language = 'Fortran'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'jov' or db_analyze_pfix[1] == 'cpl'):
                    db_analyze_language = 'Jovidal'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'mm':
                    db_analyze_language = 'Objective-C++'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'py':
                    db_analyze_language = 'Python'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'sql':
                    db_analyze_language = 'Sql'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'tsx' or db_analyze_pfix[1] == 'ts'):
                    db_analyze_language = 'TypeScript'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'vb':
                    db_analyze_language = 'Basic'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'vhdl' or db_analyze_pfix[1] == 'vhd'):
                    db_analyze_language = 'VHDL'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'asm' or db_analyze_pfix[1] == 's'):
                    db_analyze_language = 'Assembly'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'cbl' or db_analyze_pfix[1] == 'cob' or db_analyze_pfix[1] == 'cpy'):
                    db_analyze_language = 'COBOL'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'htm' or db_analyze_pfix[1] == 'html'):
                    db_analyze_language = 'Html'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'js'):
                    db_analyze_language = 'Javascript'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'pas' or db_analyze_pfix[1] == 'sp'):
                    db_analyze_language = 'Pascal'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'plm':
                    db_analyze_language = 'Plm'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'tcl':
                    db_analyze_language = 'Tcl'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'txt' or db_analyze_pfix[1] == 'TXT'):
                    db_analyze_language = 'Text'
            if len(db_analyze_pfix)>1 and (db_analyze_pfix[1] == 'vh' or db_analyze_pfix[1] == 'v'):
                    db_analyze_language = 'Verilog'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'xml':
                    db_analyze_language = 'Xml'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'bat':
                    db_analyze_language = 'MSDos Batch'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'cs':
                    db_analyze_language = 'C#'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'java':
                    db_analyze_language = 'Java'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'm':
                    db_analyze_language = 'Objective-C'
            if len(db_analyze_pfix)>1 and db_analyze_pfix[1] == 'php':
                    db_analyze_language = 'Php'
            file_lang=[]
            file_lang.append(db_analyze_language)
            file_qname= file.longname()
            file_name_Qualified=[]
            file_name_Qualified = file_qname.split('/')
            last=[]

            last = file_name_Qualified[file_name_Qualified.__len__()-1].split('.')
            location=[]

            location = ".".join(file_name_Qualified[0:file_name_Qualified.__len__() - 1])
            qlast=[]
            qlast.append(location)
            qlast.append(last[0])
            file_name_Qualified='.'.join(qlast[0:qlast.__len__()])
            file_metric = []
            metrics = file.metric(file.metrics())

            for k, v in sorted(metrics.items()):

                file_metric.append(v)
            #print(file.ents("Class"))


        final_set.append(file_name[0])
        final_set.append(file_lang[0])
        final_set.append(file_name_Qualified)
        final_set.append(location)
        final_set.append(file_metric)
        final_set.append(cont_func)





        report.append(final_set)


file=[]
final=[]


class_db=[]
function_db=[]
metr=[]
if __name__ == '__main__':
    # Open Database
    args = sys.argv
    db = understand.open("/home/nazanin/New.udb")

    #function_db=containedfunctions()
    class_db = containedclasses()

    fileList(db)
    fil_list=[]
    file_list= db.ents('File')



#print(metr)
File_header=[]
File_header=['Name','ProgrammingLanguage','qualifiedName','location', 'Lines','CommentLines','BlankLines','PreprocessorLines','CodeLines','InactiveLines','ExecutableCodeLines','DeclarativeCodeLines', 'ExecutionStatements',  'DeclarationStatements',  'RatioComment/Code', 'Units', 'containedClasses','containedFunctions','usesSourceFiles','usedbySourceFiles']
#report.insert(0,File_header)

i=0
with open('FileLevel Report.txt', 'w') as classhandle:

    #while i < final_set.__len__():
       for listitem in report[i]:
            classhandle.write('%s;' % listitem)
            i= i +1
            if i %5 == 0:            classhandle.write('\n')
       #i = i+1

i=0
with open('File Level classes Report.txt', 'w') as filehandle:

    while i < report.__len__():
       for listitem in class_db:
            filehandle.write('%s;' % listitem)
            #if i %4 == 0: filehandle.write('\n')
       filehandle.write('\n')
       i = i+1
