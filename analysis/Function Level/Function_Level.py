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

