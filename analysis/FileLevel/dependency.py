
#db = open("File Contents.txt", "r")
db = open("pytorch.txt", "r")
db = db.read()
db_st = []
db_st2 = []
db_st = db.split("\n\n")

db_temp = db_st[1:db_st.__len__()]
print(db_temp[0])
db_st = db_temp
classes = ['  Classes']
types = ['  Types']
loc_var = ['  Local Variables']
glob_var = ['  Global Variables']
loc_func = ['  Local Functions']
glob_func = ['  Global Functions']
loc_method=['  Local Methods']
glob_method=['  Global Methods']

db_arr=['','','']
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

db_list = []
counter = 0
while counter < db_st.__len__()-1:
    db_list = db_st[counter].split("\n")
    file_name = db_list[0]
    file_name_total.append(db_list[0])

    i = 0
    type_num = 0
    class_num = 0
    loc_func_number = 0
    glob_func_number = 0
    loc_var_number = 0
    glob_var_number = 0
    loc_method_number = 0
    glob_method_number = 0

    while (i < db_list.__len__()):
        if db_list[i] == classes[0]:
            class_num= i+1


        if db_list[i] == types[0]:
            type_num= i+1

            file_type=db_list[i + 1]


        #    print(i)
        if db_list[i] == loc_var[0]:
            loc_var_number = i + 1
        #  print(loc_var_number)
        if db_list[i] == glob_var[0]:
            glob_var_number = i + 1
        #  print(glob_var_number)
        if db_list[i] == loc_func[0]:
            loc_func_number = i + 1
            #break
        if db_list[i] == glob_func[0]:
            glob_func_number = i + 1
            #break
        if db_list[i] == loc_method[0]:
            loc_method_number = i + 1
        if db_list[i] == glob_method[0]:
            glob_method_number = i + 1
        # print(loc_func_number)

        i = i + 1
    if type_num!= 0 and class_num !=0:
        class_mem = db_list[class_num: type_num-1]
    elif loc_var_number != 0 and class_num !=0:
        class_mem = db_list[class_num: loc_var_number - 1]
    elif glob_var_number != 0 and class_num !=0:
        class_mem = db_list[class_num: glob_var_number - 1]
    elif loc_func_number != 0 and class_num !=0:
        class_mem = db_list[class_num: loc_func_number- 1]
    elif glob_func_number != 0 and class_num !=0:
        class_mem = db_list[class_num: glob_func_number - 1]
    elif loc_method_number!=0 and class_num != 0:
        class_mem = db_list[class_num: loc_method_number - 1]
    elif glob_method_number != 0 and class_num != 0:
        class_mem = db_list[class_num: glob_method_number - 1]
    elif class_num!=0:
        class_mem = db_list[class_num:db_list.__len__()]





    if loc_func_number!= 0 and glob_func_number!=0:
        locfunction= db_list[loc_func_number:glob_func_number-1]
    elif loc_func_number!=0 and loc_method_number!=0 :
        locfunction= db_list[loc_func_number:loc_method_number-1]
    elif loc_func_number!=0 and glob_method_number!=0:
        locfunction = db_list[loc_func_number:glob_method_number - 1]
    elif loc_func_number!=0 and glob_func_number==0 and loc_method_number==0 and glob_method_number==0:
        locfunction= db_list[loc_func_number:db_list.__len__()]

    if glob_func_number != 0 and loc_method_number != 0:
        globfunction = db_list[glob_func_number:loc_method_number - 1]
    elif glob_func_number != 0 and glob_method_number != 0:
        globfunction = db_list[glob_func_number:glob_method_number - 1]
    elif glob_func_number != 0 and loc_method_number==0 and glob_method_number==0:
        globfunction = db_list[glob_func_number:db_list.__len__()]

    function.extend(locfunction)
    function.extend(globfunction)

    if loc_method_number !=0 and glob_method_number==0:
        locmethod= db_list[loc_method_number:db_list.__len__()]
    elif loc_method_number !=0 and glob_method_number!=0:
        locmethod = db_list[loc_method_number:glob_method_number-1]

    if glob_method_number!=0:
        globmethod = db_list[glob_method_number:db_list.__len__()]

    function.extend(locmethod)
    function.extend(globmethod)
    #final_table.append(file_name)
    #if class_mem==[]:
     #   class_mem=["0"]
    #final_table.extend(class_mem)
    #if function==[]:
    #    function=["0"]
    #final_table.extend(function)
    db_arr=[file_name,class_mem,function]
    final_table.append(db_arr)
    counter = counter+1
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

# print(final_table)
with open(' File Contents Report.txt', 'w') as filehandle:
    #filehandle.write('%s\n' % final_table)
    for listitem in final_table:
        filehandle.write('%s\n' % listitem)

print(final_table[0])
# print(root_call_by)
