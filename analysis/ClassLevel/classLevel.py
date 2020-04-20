def contained_functions(name):
    db_class_cross = open("Program Unit Cross Reference.txt", 'r')
    db_class_cross = db_class_cross.read()
    #name = 'final'
    join_name = ''
    join_name = ("  ") + (name)
    class_cross = db_class_cross.split("\n\n")
    class_cross = class_cross[1:class_cross.__len__()]
    class_i = 0
    class_cross_temp = []
    class_function = []
    while class_i < class_cross.__len__():
        class_cross_temp = class_cross[class_i].split("   ")
        # print(class_cross_temp)
        class_i_temp = 0
        class_item = []

        class_j = 0
        while class_j < class_cross_temp.__len__():
            if name == class_cross_temp[class_j] or class_cross_temp[class_j] == join_name:
                class_function.append(class_cross_temp[0])
            class_j = class_j + 1
        class_i = class_i + 1

    return (class_function)


########################################################################
################################################################################
######################################################################################
db_dependency = open("File Contents.txt", "r")
db_dependency = db_dependency.read()
db_dependency_st = []
db_dependency_st2 = []
db_dependency_st = db_dependency.split("\n\n")

db_dependency_temp = db_dependency_st[1:db_dependency_st.__len__()]
#print(db_dependency_temp[0])
db_dependency_st = db_dependency_temp
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
globmethod=[]
locmethod=[]
class_qualifed_dict=[]
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

    i = 0
    type_num = 0
    class_num = 0
    loc_func_number = 0
    glob_func_number = 0
    loc_var_number = 0
    glob_var_number = 0
    loc_method_number = 0
    glob_method_number = 0

    while (i < db_dependency_list.__len__()):
        if db_dependency_list[i] == classes[0]:
            class_num = i+1


        if db_dependency_list[i] == types[0]:
            type_num = i+1

            file_type = db_dependency_list[i + 1]


        #    print(i)
        if db_dependency_list[i] == loc_var[0]:
            loc_var_number = i + 1
        #  print(loc_var_number)
        if db_dependency_list[i] == glob_var[0]:
            glob_var_number = i + 1
        #  print(glob_var_number)
        if db_dependency_list[i] == loc_func[0]:
            loc_func_number = i + 1
            #break
        if db_dependency_list[i] == glob_func[0]:
            glob_func_number = i + 1
            #break
        if db_dependency_list[i] == loc_method[0]:
            loc_method_number = i + 1
        if db_dependency_list[i] == glob_method[0]:
            glob_method_number = i + 1
        # print(loc_func_number)

        i = i + 1
    if type_num != 0 and class_num != 0:
        class_mem = db_dependency_list[class_num: type_num - 1]
    elif loc_var_number != 0 and class_num != 0:
        class_mem = db_dependency_list[class_num: loc_var_number - 1]
    elif glob_var_number != 0 and class_num != 0:
        if class_num < glob_var_number:
             class_mem = db_dependency_list[class_num: glob_var_number - 1]
        if class_num > glob_var_number:
            class_mem = db_dependency_list[class_num:db_dependency_list.__len__()]
    elif loc_func_number != 0 and class_num != 0:
        class_mem = db_dependency_list[class_num: loc_func_number - 1]
    elif glob_func_number != 0 and class_num != 0:
        class_mem = db_dependency_list[class_num: glob_func_number - 1]
    elif loc_method_number != 0 and class_num != 0:
        class_mem = db_dependency_list[class_num: loc_method_number - 1]
    elif glob_method_number != 0 and class_num != 0:
        class_mem = db_dependency_list[class_num: glob_method_number - 1]
    elif class_num != 0:
        class_mem = db_dependency_list[class_num:db_dependency_list.__len__()]

    f = ['add_ops_list_test.UnaryOpBenchmark']
    if class_mem == f:
        print("YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASSSSSSSSSSSSSSSSSSSS")




    cls_i = 0
    cls_temp = []
    cls_temp_mirror = []
    while cls_i < class_mem.__len__():
        cls_temp = class_mem[cls_i].split('(')
        cls_temp_mirror = cls_temp[0].split(" ")
        if cls_temp_mirror != ['']:
            class_mem[cls_i] = cls_temp_mirror[4]

            class_qualifed_temp = class_mem[cls_i]
            class_qualifed_temp = class_qualifed_temp.split('.')
            class_qualifed_temp = class_qualifed_temp[class_qualifed_temp.__len__()-1]
            qulified_name = file_name_temp
            qulified_name.append(class_qualifed_temp)
            class_qualifed_dict.append(class_mem[cls_i])
            class_qualifed_dict.append('.'.join(qulified_name[1:len(qulified_name)]))
            class_qualifed_dict.append('\n')
        cls_i = cls_i + 1

   # print(final_table)
    counter_dependency = counter_dependency+1
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

def name_qualifedname(name):
    qd_n_i =2
    #if name.split('.').__len__()>1:
    qname =[]
    value=['','']
    qname.append(name)
    while qd_n_i < class_qualifed_dict.__len__()-1:
        if class_qualifed_dict[qd_n_i] == '\n':
            ch = class_qualifed_dict[qd_n_i-2]
            if qname[0] == class_qualifed_dict[qd_n_i-2]:
                value = [class_qualifed_dict[qd_n_i-2],class_qualifed_dict[qd_n_i-1]]
                return value
        qd_n_i = qd_n_i +3

########################################################################
################################################################################
######################################################################################

db_analyze = open("Class Metrics.txt","r")
db_analyze = db_analyze.read()
db_class_st=[]
db_class_st2=[]
db_class_st = db_analyze.split("\n\n")


i = 0
db_class_list=[]
db_st_temp=db_class_st[0].split('\n')
db_class_st = db_class_st[1:db_class_st.__len__()-1]
db_st_temp = db_st_temp[3:db_st_temp.__len__()]
db_class_st.insert(0,db_st_temp)
db_temp2=""
j = 5

while(j<db_class_st.__len__()):
    # print(db_st[j])
    db__class_list = db_class_st[j].split("\n")
    # print(db_list)
    db_class_list = db_class_list[3:db_class_list.__len__()]
    # print(db_list)
    db_class_st[j] = ""
    db_class_st2.extend(db_class_list)
    j = j + 5

db_class_st.extend(db_class_st2)

counter = 1
final_set=[]
analyze_counter=0
db_class_line=[]
db_class_insert=[]

#print(db_class_st[0])
class_output=''

name = []
name = db_class_st[0][0].split("   ")
name = name[name.__len__() - 1]
name = name.split(':')
class_name = name_qualifedname(name[0])
db_class_insert.append(class_name[0])
db_class_insert.append(class_name[1])
contained_func=contained_functions(name[0])
total_calass_name=[]
total_calass_name.append(name[0])

line = []
line = db_class_st[0][1].split("   ")
line = line[line.__len__() - 1]
db_class_insert.append(line)

blank_line = []
blank_line = db_class_st[0][2].split("  ")
blank_line = blank_line[blank_line.__len__() - 1]
db_class_insert.append(blank_line)

line_code = []
line_code = db_class_st[0][3].split("  ")
line_code = line_code[line_code.__len__() - 1]
db_class_insert.append(line_code)

line_comment = []
line_comment = db_class_st[0][4].split("  ")
line_comment = line_comment[line_comment.__len__() - 1]
db_class_insert.append(line_comment)

line_avg = []
line_avg = db_class_st[0][5].split("  ")
line_avg = line_avg[line_avg.__len__() - 1]
db_class_insert.append(line_avg)

line_comment_avg = []
line_comment_avg = db_class_st[0][6].split("  ")
line_comment_avg = line_comment_avg[line_comment_avg.__len__() - 1]
db_class_insert.append(line_comment_avg)

avg_complexity = []
avg_complexity = db_class_st[0][7].split("  ")
avg_complexity = avg_complexity[avg_complexity.__len__() - 1]
db_class_insert.append(avg_complexity)

max_complexity = []
max_complexity = db_class_st[0][8].split("  ")
max_complexity = max_complexity[max_complexity.__len__() - 1]
db_class_insert.append(max_complexity)

ratio = []
ratio = db_class_st[0][9].split("  ")
ratio = ratio[ratio.__len__() - 1]
db_class_insert.append(ratio)

db_class_insert.append(contained_func)
#print(db_class_st)
while(counter<db_class_st.__len__()):
    db_class_line = db_class_st[counter].split('\n')
    #print(db_class_line)
    if db_class_line[0] != [] and db_class_line.__len__() > 1:
                #print(db_class_insert)
        name = []
        name = db_class_line[0].split("   ")
        name = name[name.__len__()-1]
        name = name.split(':')
        class_name = name_qualifedname(name[0])
        db_class_insert.append(class_name[0])
        db_class_insert.append(class_name[1])
        total_calass_name.append(name[0])
        contained_func = contained_functions(name[0])

        line = []
        line = db_class_line[1].split("   ")
        line = line[line.__len__()-1]
        db_class_insert.append(line)

        blank_line = []
        blank_line = db_class_line[2].split("  ")
        blank_line = blank_line[blank_line.__len__()-1]
        db_class_insert.append(blank_line)

        line_code = []
        line_code = db_class_line[3].split("  ")
        line_code = line_code[line_code.__len__()-1]
        db_class_insert.append(line_code)

        line_comment = []
        line_comment = db_class_line[4].split("  ")
        line_comment = line_comment[line_comment.__len__() - 1]
        db_class_insert.append(line_comment)

        line_avg = []
        line_avg = db_class_line[5].split("  ")
        line_avg = line_avg[line_avg.__len__() - 1]
        db_class_insert.append(line_avg)

        line_comment_avg = []
        line_comment_avg = db_class_line[6].split("  ")
        line_comment_avg = line_comment_avg[line_comment_avg.__len__() - 1]
        db_class_insert.append(line_comment_avg)

        avg_complexity = []
        avg_complexity = db_class_line[7].split("  ")
        avg_complexity = avg_complexity[avg_complexity.__len__() - 1]
        db_class_insert.append(avg_complexity)

        max_complexity = []
        max_complexity = db_class_line[8].split("  ")
        max_complexity = max_complexity[max_complexity.__len__() - 1]
        db_class_insert.append(max_complexity)

        ratio = []
        ratio = db_class_line[9].split("  ")
        ratio = ratio[ratio.__len__() - 1]
        db_class_insert.append(ratio)

        db_class_insert.append(contained_func)

    analyze_counter = analyze_counter + 1





    final_set=(db_class_insert)


    counter = counter + 1


#print(final_set)
#print(final_table)
#print( dictionary_class)


#print(db_class_name_total)
#db_class_insert.append(used_classs)
print(final_set)

i=0
with open('Class Report.txt', 'w') as classhandle:

    #while i < final_set.__len__():
       for listitem in db_class_insert:
            classhandle.write('%s;' % listitem)
            i= i +1
            if i %12 == 0:            classhandle.write('\n')
       #i = i+1
    
