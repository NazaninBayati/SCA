import subprocess
import subprocess
import time
#ubprocess.call([r'C:\Users\nazanin\Documents\api.bat'])
#subprocess.run([r'C:\Users\Lion\PycharmProjects\SCA-master (1)\SCA-master\analysis\FileLevel\Auto\metrics.bat'])
#time.sleep(1)
#subprocess.run([r'C:\Users\Lion\PycharmProjects\SCA-master (1)\SCA-master\analysis\FileLevel\Auto\contents.bat'])
#time.sleep(1)
#subprocess.run([r'C:\Users\Lion\PycharmProjects\SCA-master (1)\SCA-master\analysis\FileLevel\Auto\include.bat'])
#time.sleep(1)


dictionary_file = []
def file_dictionary(file_name,file_address,file_call):

    di_file = 0

    dictionary_file.append(file_name)
    dictionary_file.append(file_address)
    while di_file < file_call.__len__():

        dictionary_file.append(file_call[di_file])
        dictionary_file.append('\n')
        if di_file < file_call.__len__() - 1:
            dictionary_file.append(file_name)
            #if file_address.__len__()>1:
            dictionary_file.append(file_address)

        di_file = di_file + 1

##########################################################################
################################################################################
######################################################################################

def who_call(file_name):
    dc=dictionary_file
    who_file_i = 2
    who_file=[]
    while who_file_i < dictionary_file.__len__():
        if dictionary_file[who_file_i] =='\n':

            if file_name == dictionary_file[who_file_i-1]:
                who_file.append(dictionary_file[who_file_i-3])
        who_file_i = who_file_i + 1
    return  who_file


########################################################################
################################################################################
#########################################################################################
#db_file = open("python Include File.txt",'r')
#db_file = open("Include File_pytorch.txt",'r')
#db_file = open("Include File.txt",'r')
#db_file = open(r"C:\sca\analysis\FileLevel\include_file.txt",'r')

db_file = open(r"newceph_include.txt",'r')

db_file = db_file.read()
db_file_st = []
db_file_st2 = []
rel = 'RELATIVE:'
space = ['']
def file_included(name,address):
    db_file_st = db_file.split("\n")
    db_file_st = db_file_st[4:db_file_st.__len__()]
    file_call=[]
    i_file = 0
    file_name=[]
    db_file_temp=[]
    File_flag= False
    #name = 'help.h'
    #address='couchdb-master/couchdb-master/src/couch/priv/couch_js/1.8.5'

    while i_file < db_file_st.__len__():

        if db_file_st[i_file] != '':
            db_file_temp = db_file_st[i_file].split('\\')
            db_file_check = db_file_temp[0].split('[')
            db_check = db_file_check[0]
            if db_file_temp.__len__() > 2 and (db_check =='   Include ' or db_check=='C:'):
                file_address = db_file_st[i_file]
                if db_file_temp.__len__() > 4 and db_file_temp[3] == 'RELATIVE:':
                    file_address = "/".join(db_file_temp[4:db_file_temp.__len__()])
                file_address2 = []

                i_file = i_file + 3
                file_name = db_file_st[i_file]
                if address.__len__()>2:
                    file_address2 = address.split('/')
                    file_address2 = "/".join(file_address2[0:file_address2.__len__() - 1])
                elif address != '':
                    file_address2 = name

                if  file_name == name and (file_address == address or file_address2 == file_address or file_address2==address[0]):
                    file_flag = True
                    while file_flag == True and i_file < db_file_st.__len__()-1:
                        i_file = i_file + 1
                        db_file_call = db_file_st[i_file].split(" ")
                        if db_file_call[db_file_call.__len__()-2] == 'Page':
                            i_file = i_file +3
                            db_file_call = db_file_st[i_file].split(" ")
                        file_call.append( db_file_call[db_file_call.__len__()-1])
                        j_file = i_file + 1

                        if j_file < db_file_st.__len__():
                            a = db_file_st[j_file]
                            file_chase = db_file_st[j_file].split(' ')
                        if j_file < db_file_st.__len__() and db_file_st[j_file] != '':
                            if file_chase.__len__() < 2:
                                file_call = file_call[0:file_call.__len__()-1]
                                File_flag = False
                                #break
                            if file_chase.__len__()<11 and file_chase.__len__()>4:
                                if file_chase[4] != 'Include':
                                    file_flag = False
                            if file_chase.__len__()>11:
                                if file_chase[file_chase.__len__()-2]=='Page':
                                    i_file = i_file + 3
                #print(file_call)
        i_file = i_file + 1
    print("***********************")
    return file_call

###########################################################
##################################################################
#########################################################################

#db_dependency = open("python File Contents.txt", "r")
#db_dependency = open("pytorch.txt", "r")
#db_dependency = open("File Contents.txt", "r")
#db_dependency = open(r"C:\sca\analysis\FileLevel\file_contents.txt",'r')

db_dependency = open(r"newceph_contents.txt",'r')


db_dependency = db_dependency.read()
db_dependency_st = []
db_dependency_st2 = []
db_dependency_st = db_dependency.split("\n\n")
file_name_Qualified_r=[]
db_dependency_temp = db_dependency_st[1:db_dependency_st.__len__()]
#print(db_dependency_temp[0])
db_dependency_st = db_dependency_temp
functions_item = ['  Functions']
classes = ['  Classes']
types = ['  Types']
loc_var = ['  Local Variables']
glob_var = ['  Global Variables']
loc_func = ['  Local Functions']
loc_func_2 = ['  Functions']
glob_func = ['  Global Functions']
loc_method=['  Local Methods']
glob_method=['  Global Methods']

db_dependency_arr=['','','']
class_mem=[]
file_name = []
file_type = []
final_table = []
file_name_total=[]
glob_func_number = 0
global_function = []
local_variables = []
locfunction=[]
globfunction=[]
function=[]
functions_mem=[]
globmethod=[]
locmethod=[]

db_dependency_list = []
counter_dependency = 0
while counter_dependency < db_dependency_st.__len__():
    db_dependency_list = db_dependency_st[counter_dependency].split("\n")
    file_name = db_dependency_list[0]
    file_name_total.append(db_dependency_list[0])
    file_name_temp=[]
    file_name_temp = file_name.split("\\")
    if (file_name_temp.__len__()>2):
        file_name = file_name_temp[file_name_temp.__len__()-1]
        file_name_Qualified = ".".join(file_name_temp[1:file_name_temp.__len__()])
        file_name_Qualified_r=file_name_Qualified
        file_name_Qualified_temp = file_name_Qualified.split('.')
        file_name_Qualified= ".".join(file_name_Qualified_temp[0:file_name_Qualified_temp.__len__()-1])
    else: file_name_Qualified_r = file_name_temp
    i = 0
    type_num = 0
    class_num = 0
    loc_func_number = 0
    glob_func_number = 0
    loc_var_number = 0
    glob_var_number = 0
    loc_method_number = 0
    glob_method_number = 0
    functions_item_var = 0
    queue = []

    print("&&&&&&&&&&&&&&&&&&&&&&&")
    while (i < db_dependency_list.__len__()):
        if db_dependency_list[i] == classes[0]:
            class_num = i+1
            queue.append(i+1)

        if db_dependency_list[i] == functions_item[0]:
            functions_item_var = i+1
            queue.append(i+1)

        if db_dependency_list[i] == types[0]:
            type_num = i+1
            queue.append(i+1)
            file_type = db_dependency_list[i + 1]


        if db_dependency_list[i] == loc_var[0]:
            loc_var_number = i + 1
            queue.append(i+1)
        #  print(loc_var_number)

        if db_dependency_list[i] == glob_var[0]:
            glob_var_number = i + 1
            queue.append(i+1)
        #  print(glob_var_number)

        if db_dependency_list[i] == loc_func[0]:
            loc_func_number = i + 1
            queue.append(i+1)
            #break
        if db_dependency_list[i] == glob_func[0]:
            glob_func_number = i + 1
            queue.append(i+1)
            #break
        if db_dependency_list[i] == loc_method[0]:
            loc_method_number = i + 1
            queue.append(i+1)
        if db_dependency_list[i] == glob_method[0]:
            glob_method_number = i + 1
            queue.append(i+1)
        # print(loc_func_number)
        i = i + 1
    queue.append(db_dependency_list.__len__())


    print(queue)
    queue_counter = 0
    while queue_counter < queue.__len__():

        if queue[queue_counter]== class_num:
            if queue[queue_counter+1] == db_dependency_list.__len__():
                end = queue[queue_counter+1]
            else:
                end = queue[queue_counter + 1] - 1
            class_mem = db_dependency_list[class_num:end]

        if queue[queue_counter] == functions_item_var:
            if queue[queue_counter + 1] == db_dependency_list.__len__():
                end = queue[queue_counter + 1]
            else:
                end = queue[queue_counter + 1] - 1
            functions_mem = db_dependency_list[functions_item_var:end]

        #if queue[queue_counter] == type_num:
        #    end = queue[queue_counter + 1] - 2
        #    ty = db_dependency_list[functions_item_var:end]

        #if queue[queue_counter] == loc_var_number:
        #    end = queue[queue_counter + 1] - 2
        #    functions_mem = db_dependency_list[functions_item_var:end]

        #if queue[queue_counter] == glob_var_number:
        #    end = queue[queue_counter + 1] - 2
        #    functions_mem = db_dependency_list[functions_item_var:end]

        if queue[queue_counter] == loc_func_number:
            if queue[queue_counter + 1] == db_dependency_list.__len__():
                end = queue[queue_counter + 1]
            else:
                end = queue[queue_counter + 1] - 1
            locfunction = db_dependency_list[loc_func_number:end]

        if queue[queue_counter] == glob_func_number:
            if queue[queue_counter + 1] == db_dependency_list.__len__():
                end = queue[queue_counter + 1]
            else:
                end = queue[queue_counter + 1] - 1
            globfunction = db_dependency_list[glob_func_number:end]

        if queue[queue_counter] == loc_method_number:
            if queue[queue_counter + 1] == db_dependency_list.__len__():
                end = queue[queue_counter + 1]
            else:
                end = queue[queue_counter + 1] - 1
            locmethod = db_dependency_list[loc_method_number:end]

        if queue[queue_counter] == glob_method_number:
            if queue[queue_counter + 1] == db_dependency_list.__len__():
                end = queue[queue_counter + 1]
            else:
                end = queue[queue_counter + 1] - 1
            globmethod = db_dependency_list[glob_method_number:end]

        queue_counter = queue_counter + 1



    function.extend(functions_mem)
    function.extend(locfunction)
    function.extend(globfunction)


    function.extend(locmethod)
    function.extend(globmethod)

   # print(class_mem)
   # print(function)
    func_i=0
    func_temp=[]
    func_temp_mirror=[]
    while func_i < function.__len__():
        func_temp= function[func_i].split('(')
        func_temp_mirror = func_temp[0].split(" ")
        mirror_i =0
       # while mirror_i < func_temp
        if func_temp_mirror !=['']:
            function[func_i] = func_temp_mirror[4]
        func_i = func_i +1
    cls_i = 0
    cls_temp = []
    cls_temp_mirror = []
    while cls_i < class_mem.__len__():
        cls_temp = class_mem[cls_i].split('(')
        cls_temp_mirror = cls_temp[0].split(" ")
        if cls_temp_mirror != ['']:
            class_mem[cls_i] = cls_temp_mirror[4]
        cls_i = cls_i + 1

    db_dependency_arr = [file_name_Qualified_r,class_mem, function]
    final_table.append(db_dependency_arr)
   # print(final_table)
    counter_dependency = counter_dependency + 1
    class_mem = []
    file_name = []
    file_type = []
    glob_func_number = 0
    global_function = []
    local_variables = []
    locfunction = []
    globfunction = []
    function = []
    globmethod = []
    locmethod = []
    functions_mem=[]


#########################################
################################################
########################################################

#db_analyze = open("python file metrics.txt","r")
#db_analyze = open("File Metrics.txt","r")
#db_analyze = open("couchdatabase.txt","r")

#db_analyze =  open(r"C:\sca\analysis\FileLevel\file_Metrics.txt",'r')

db_analyze = open(r"newceph_metrics.txt",'r')

db_analyze = db_analyze.read()
db_analyze_st=[]
db_analyze_st2=[]
db_analyze_st = db_analyze.split("\n\n")

i = 0
db_analyze_list=[]
db_file_name_total=[]

db_analyze_temp = db_analyze_st[1:db_analyze_st.__len__()]
db_analyze_st=db_analyze_temp

db_analyze_temp2 = ""
j = 3

while(j<db_analyze_st.__len__()-1):

    db_analyze_list = db_analyze_st[j].split("\n")

    db_analyze_list = db_analyze_list[0:db_analyze_list.__len__()-3]

    db_analyze_st[j] =" "
    db_analyze_st2.extend(db_analyze_list)
    #print(db_analyze_st2)
    j = j + 4

db_analyze_st.extend(db_analyze_st2)

file_output=''

used_files = []

space = [' ']
rel = 'RELATIVE:'
counter = 0
final_set=[]
analyze_counter=0
#print(db_analyze_st)
while(counter<db_analyze_st.__len__()):
    db_analyze_line = db_analyze_st[counter].split('\n')
    #print(db_analyze_line)
    if db_analyze_line != space:
        total_name = []
        total_name = db_analyze_line[0]
        db_analyze_stmt = db_analyze_line[0].split("\\")
        db_analyze_insert = []

        #if db_analyze_stmt[0] != rel:
        db_analyze_insert=[]
        db_analyze_insert=db_analyze_line[1:db_analyze_line.__len__()]
        if db_analyze_stmt.__len__()>2 :
            db_analyze_address = "/".join(db_analyze_stmt[1:db_analyze_stmt.__len__()])
            db_qualified_name = ".".join(db_analyze_stmt[1:db_analyze_stmt.__len__()])
            file_name_Qualified_ref = db_qualified_name
            db_qualified_name = db_qualified_name.split(".")
            db_qualified_name = ".".join(db_qualified_name[0:db_qualified_name.__len__()-1])
        elif db_analyze_stmt!='':
            db_analyze_address = db_analyze_stmt
            db_qualified_name = db_analyze_stmt
            file_name_Qualified_ref = db_qualified_name
            db_qualified_name = db_qualified_name[0].split(".")
            db_qualified_name = ".".join(db_qualified_name[0:db_qualified_name.__len__() - 1])
        db_analyze_proj_name = db_analyze_stmt[db_analyze_stmt.__len__()-1]
        db_analyze_pfix = db_analyze_proj_name.split('.')
        if db_analyze_pfix.__len__()>1:
            if db_analyze_pfix[1] == 'cpp' or db_analyze_pfix[1] == 'h' or db_analyze_pfix[1] == 'C' or db_analyze_pfix[1] == 'hpp' or db_analyze_pfix[1] == 'hxx' or db_analyze_pfix[1] == 'cxx' or db_analyze_pfix[1] == 'H' or db_analyze_pfix[1] == 'inl' or db_analyze_pfix[1] == 'cc' or db_analyze_pfix[1] == 'hh':
                db_analyze_language = 'C++'
            elif db_analyze_pfix[1] == 'c' :
                db_analyze_language = 'C'
            elif db_analyze_pfix[1] == 'a' or db_analyze_pfix[1] == 'ads' or db_analyze_pfix[1] == 'gpr' or db_analyze_pfix[1] == 'ada' or db_analyze_pfix[1] == 'adb_analyze':
                db_analyze_language = 'Ada'
            elif db_analyze_pfix[1] == 'cgi' or db_analyze_pfix[1] == 'pl' or db_analyze_pfix[1] == 'pm':
                db_analyze_language = 'Perl'
            elif db_analyze_pfix[1] == 'css' :
                db_analyze_language = 'CSS'
            elif db_analyze_pfix[1] == 'dpr' or db_analyze_pfix[1] == 'dfm':
                db_analyze_language = 'Delphi'
            elif db_analyze_pfix[1] == 'f77' or db_analyze_pfix[1] == 'f' or db_analyze_pfix[1] == 'f90' or db_analyze_pfix[1] == 'for' or db_analyze_pfix[1] == 'f03' or db_analyze_pfix[1] == 'f95' or db_analyze_pfix[1] == 'ftn':
                db_analyze_language = 'Fortran'
            elif db_analyze_pfix[1] == 'jov' or db_analyze_pfix[1] == 'cpl':
                db_analyze_language = 'Jovidal'
            elif db_analyze_pfix[1] == 'mm':
                db_analyze_language = 'Objective-C++'
            elif db_analyze_pfix[1] == 'py' :
                db_analyze_language = 'Python'
            elif db_analyze_pfix[1] == 'sql':
                db_analyze_language = 'Sql'
            elif db_analyze_pfix[1] == 'tsx' or db_analyze_pfix[1] == 'ts':
                db_analyze_language = 'TypeScript'
            elif db_analyze_pfix[1] == 'vb':
                db_analyze_language = 'Basic'
            elif db_analyze_pfix[1] == 'vhdl' or db_analyze_pfix[1] == 'vhd':
                db_analyze_language = 'VHDL'
            elif db_analyze_pfix[1] == 'asm' or db_analyze_pfix[1] == 's':
                db_analyze_language = 'Assembly'
            elif db_analyze_pfix[1] == 'cbl' or db_analyze_pfix[1] == 'cob' or db_analyze_pfix[1] == 'cpy':
                db_analyze_language = 'COBOL'
            elif db_analyze_pfix[1] == 'htm' or db_analyze_pfix[1] == 'html':
                db_analyze_language = 'Html'
            elif db_analyze_pfix[1] == 'js':
                db_analyze_language = 'Javascript'
            elif db_analyze_pfix[1] == 'pas' or db_analyze_pfix[1] == 'sp':
                db_analyze_language = 'Pascal'
            elif db_analyze_pfix[1] == 'plm':
                db_analyze_language = 'Plm'
            elif db_analyze_pfix[1] == 'tcl':
                db_analyze_language = 'Tcl'
            elif db_analyze_pfix[1] == 'txt' or db_analyze_pfix[1] == 'TXT':
                db_analyze_language = 'Text'
            elif db_analyze_pfix[1] == 'vh' or db_analyze_pfix[1] == 'v':
                db_analyze_language = 'Verilog'
            elif db_analyze_pfix[1] == 'xml':
                db_analyze_language = 'Xml'
            elif db_analyze_pfix[1] == 'bat' :
                db_analyze_language = 'MSDos Batch'
            elif db_analyze_pfix[1] == 'cs':
                db_analyze_language = 'C#'
            elif db_analyze_pfix[1] == 'java':
                db_analyze_language = 'Java'
            elif db_analyze_pfix[1] == 'm':
                db_analyze_language = 'Objective-C'
            elif db_analyze_pfix[1] == 'php':
                db_analyze_language = 'Php'
            else: db_analyze_language = 'NULL'
            if db_analyze_insert != [] and db_analyze_language != 'NULL':
                #print(db_analyze_insert)
                line = []
                line = db_analyze_insert[0].split("   ")
                line = line[7]
                db_analyze_insert[0]=line

                comment = []
                comment = db_analyze_insert[1].split("   ")
                comment= comment[comment.__len__()-1]
                db_analyze_insert[1]=comment

                blank = []
                blank = db_analyze_insert[2].split("   ")
                blank = blank[blank.__len__() - 1]
                db_analyze_insert[2] = blank

                Prep_Lines = []
                Prep_Lines = db_analyze_insert[3].split("   ")
                Prep_Lines = Prep_Lines[Prep_Lines.__len__() - 1]
                db_analyze_insert[3] = Prep_Lines

                Code_Lines = []
                Code_Lines = db_analyze_insert[4].split("   ")
                Code_Lines = Code_Lines[Code_Lines.__len__() - 1]
                db_analyze_insert[4] = Code_Lines

                Inactive_Lines=[]
                Inactive_Lines = db_analyze_insert[5].split("   ")
                Inactive_Lines = Inactive_Lines[Inactive_Lines.__len__()-1]
                db_analyze_insert[5] = Inactive_Lines

                Exe_Lines = []
                Exe_Lines = db_analyze_insert[6].split("   ")
                Exe_Lines = Exe_Lines[Exe_Lines.__len__() - 1]
                db_analyze_insert[6] = Exe_Lines

                Decl_Lines = []
                Decl_Lines = db_analyze_insert[7].split("  ")
                Decl_Lines = Decl_Lines[Decl_Lines.__len__() - 1]
                db_analyze_insert[7] = Decl_Lines

                Exe_stmt = []
                Exe_stmt = db_analyze_insert[8].split("  ")
                Exe_stmt = Exe_stmt[Exe_stmt.__len__() - 1]
                db_analyze_insert[8] = Exe_stmt

                Decl_stmt = []
                Decl_stmt = db_analyze_insert[9].split("  ")
                Decl_stmt = Decl_stmt[Decl_stmt.__len__() - 1]
                db_analyze_insert[9] = Decl_stmt

                ratio = []
                ratio = db_analyze_insert[10].split("  ")
                ratio = ratio[ratio.__len__() - 1]
                db_analyze_insert[10] = ratio

                units = []
                units = db_analyze_insert[11].split("  ")
                units = units[units.__len__() - 1]
                db_analyze_insert[11] = units

            elif db_analyze_language != 'NULL':
                db_analyze_insert=[]

                j= counter + 1
                line = db_analyze_st[j].split("   ")
                line = line[7]
                db_analyze_insert.append( line)

                j = counter + 2
                comment = db_analyze_st[j].split("   ")
                comment= comment[comment.__len__()-1]
                db_analyze_insert.append(comment)

                j = counter + 3
                blank = db_analyze_st[j].split("   ")
                blank = blank[blank.__len__() - 1]
                db_analyze_insert.append(blank)

                j = counter + 4
                Prep_Lines = db_analyze_st[j].split("   ")
                Prep_Lines = Prep_Lines[Prep_Lines.__len__() - 1]
                db_analyze_insert.append(Prep_Lines)

                j = counter + 5
                Code_Lines = db_analyze_st[j].split("   ")
                Code_Lines = Code_Lines[Code_Lines.__len__() - 1]
                db_analyze_insert.append(Code_Lines)

                j = counter + 6
                Inactive_Lines = db_analyze_st[j].split("   ")
                Inactive_Lines = Inactive_Lines[Inactive_Lines.__len__() - 1]
                db_analyze_insert.append(Inactive_Lines)

                j = counter + 7
                Exe_Lines = db_analyze_st[j].split("   ")
                Exe_Lines = Exe_Lines[Exe_Lines.__len__() - 1]
                db_analyze_insert.append(Exe_Lines)

                j = counter + 8
                Decl_Lines = db_analyze_st[j].split("  ")
                Decl_Lines = Decl_Lines[Decl_Lines.__len__() - 1]
                db_analyze_insert.append(Decl_Lines)

                j = counter + 9
                Exe_stmt = db_analyze_st[j].split("  ")
                Exe_stmt = Exe_stmt[Exe_stmt.__len__() - 1]
                db_analyze_insert.append(Exe_stmt)

                j = counter + 10
                Decl_stmt = db_analyze_st[j].split("  ")
                Decl_stmt = Decl_stmt[Decl_stmt.__len__() - 1]
                db_analyze_insert.append(Decl_stmt)

                j = counter + 11
                ratio = db_analyze_st[j].split("  ")
                ratio = ratio[ratio.__len__() - 1]
                db_analyze_insert.append(ratio)

                j = counter + 12
                units = db_analyze_st[j].split("  ")
                units = units[units.__len__() - 1]
                db_analyze_insert.append(units)

            if db_analyze_language != 'NULL':

                db_analyze_insert.insert(0,db_analyze_proj_name)
                db_analyze_insert.insert(1, db_analyze_language)
                db_analyze_insert.insert(2, db_qualified_name)
                if db_analyze_address.__len__()>1:
                    db_analyze_insert.insert(3,db_analyze_address)
                else:
                    db_analyze_insert.insert(3, db_analyze_address[0])

                db_file_name_total.append(total_name)
                for item in final_table:
                    p=(item[0])
                    if item[0] == file_name_Qualified_ref:

                        db_analyze_insert.append(item[1])
                        db_analyze_insert.append(item[2])
                        break
                analyze_counter = analyze_counter + 1

                call_function = file_included(db_analyze_proj_name, db_analyze_address)

                file_dictionary(total_name, db_analyze_address, call_function)

                db_analyze_insert.append(call_function)
                print("$$$$$$$$$$$$$$")


                final_set.append(db_analyze_insert)
        print("$$$$$$$$$$$$$$&&&&&**************")


    counter = counter + 1


print("##########################")
db_file_i=0
while db_file_i < db_file_name_total.__len__():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    used_files = who_call(db_file_name_total[db_file_i])
    final_set[db_file_i].append(used_files)
    db_file_i = db_file_i + 1
#print(used_files)

print("*******************************")
#print(db_file_name_total)
#db_analyze_insert.append(used_files)
#print(final_set)
File_header=[]
File_header=['Name','ProgrammingLanguage','qualifiedName','location', 'Lines','CommentLines','BlankLines','PreprocessorLines','CodeLines','InactiveLines','ExecutableCodeLines','DeclarativeCodeLines', 'ExecutionStatements',  'DeclarationStatements',  'RatioComment/Code', 'Units',  'containedClasses','containedFunctions','usesSourceFiles','usedbySourceFiles']
final_set.insert(0,File_header)
i = 0
with open('Ceph Automate File-level report.txt', 'w') as filehandle:

    while i < final_set.__len__():
       for listitem in final_set[i]:
            filehandle.write('%s;' % listitem)
       filehandle.write('\n')
       i = i+1




