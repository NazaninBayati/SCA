import understand
import sys


final_set=[]
def fileList(db):
    for file in db.ents("File"):
        file_name = []
        # If file is from the Ada Standard library, skip to next
        if file.library() != "Standard":
            file_name.append(file.name())

            db_analyze_pfix = file_name[0].split('.')
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

        final_set.append(file_name)
        final_set.append(file_lang)
        #metric=''
        ##metric = (projectMetrics(file_name))
        #final_set.append(metric)

file=[]
def projectMetrics(db):
    i = 0
    for i in range( len(db)):

        metrics = db[i].metric(db[i].metrics())
        for k, v in sorted(metrics.items()):
           print(k, "=", v)
           file.append(db[i])
           file.append(k)
           file.append(v)
           #file.append("\n")
           final_set.append(file)
           file=[]
    print("For metric details see: http://www.scitools.com/documents/metrics.php")
    #return  file


file_metric=[]
metr=[]
if __name__ == '__main__':
    # Open Database
    args = sys.argv
    db = understand.open("/home/nazanin/ceph.udb")

    fileList(db)
    metr = projectMetrics(db.ents("File"))

print(metr)
File_header=[]
File_header=['Name','ProgrammingLanguage','qualifiedName','location', 'Lines','CommentLines','BlankLines','PreprocessorLines','CodeLines','InactiveLines','ExecutableCodeLines','DeclarativeCodeLines', 'ExecutionStatements',  'DeclarationStatements',  'RatioComment/Code', 'Units', 'ontainedGlobalVariables', 'containedClasses','containedFunctions','usesSourceFiles','usedbySourceFiles']
final_set.insert(0,File_header)
i = 0
with open('File Level Report.txt', 'w') as filehandle:

    while i < final_set.__len__():
       for listitem in final_set[i]:
            filehandle.write('%s;' % listitem)
       filehandle.write('\n')
       i = i+1