import pandas as pd
import re

db_cr = open("Program Unit Cross Reference.txt","r")
db_cr = db_cr.read()
db_cr_st=[]

db_cr_st = db_cr.split("\n\n")

db_cr_temp = db_cr_st[1:db_cr_st.__len__()]
db_cr_st=db_cr_temp

c=0
temp=[]

func=[]
def crossref(func):
    len_counter=0
    compare_func=[]
    compare_func.append(func)
    cr_root_file = []
    cr_callby_func = []
    flag = False
    flag2 = False
    c=0
    while (c < db_cr_st.__len__() - 1):
        temp = db_cr_st[c].split('\n')
        temp2 = temp[0].split('(')
        temp2 = temp2[0].split(' ')
        #print(temp2[0])

        if compare_func[0] == temp2[0]:
            temp = db_cr_st[c].split(' ')

            t=0
            while t< temp.__len__()-1 :
                if temp[t]== 'Call':
                    cr_root_file =  temp[t+1]
                    len_counter = len_counter + 1
                    t = t+3
                    chase = t
                    flag=True
                if flag== True:
                    if temp[chase] == '':
                       chase= t
                    else:
                        cr_callby_func = temp[chase]
                        flag2=True
                        break
                t= t+1
        if flag2 == False:        c = c + 1
        else: break
    if cr_root_file==[]: cr_root_file = ''
    if cr_callby_func ==[] : cr_callby_func= ''

    return (cr_root_file,cr_callby_func)




db = open("File Contents.txt","r")
db = db.read()
db_st=[]
db_st2=[]
db_st = db.split("\n\n")

db_temp = db_st[1:db_st.__len__()]
db_st=db_temp
types = ['  Types']
loc_var = ['  Local Variables']
glob_var = ['  Global Variables']
loc_func = ['  Local Functions']
glob_func=['  Global Functions']

function_name=[]
function_type=[]
final_table=[]
glob_func_number =0
global_function=[]

db_list=[]
counter = 0
while counter < db_st.__len__():
    db_list=db_st[counter].split("\n")

    i=0
    loc_func_number=0
    glob_func_number=0
    loc_var_number=0
    glob_var_number=0
    while(i<db_list.__len__()):
        if db_list[i]==types[0]:
          function_name.append(db_list[i-1])
          function_type.append( db_list[i+1])
    #    print(i)
        if db_list[i]==loc_var[0]:
            loc_var_number= i+1
      #  print(loc_var_number)
        if db_list[i]==glob_var[0]:
            glob_var_number= i+1
      #  print(glob_var_number)
        if db_list[i]==loc_func[0]:
            loc_func_number= i+1
            break
        if db_list[i]==glob_func[0]:
            glob_func_number= i+1
            break
        #print(loc_func_number)

        i = i+1

    local_variables=db_list[loc_var_number:glob_var_number-2]
    global_variables=db_list[glob_var_number:loc_func_number-2]
    if  loc_func_number != 0:
        function = db_list[loc_func_number: db_list.__len__() ]
    elif glob_func_number != 0 : function = db_list[glob_func_number:db_list.__len__()]
    else:
        function= ' '
        root_call_by = ' '
        call_by = ' '

    if function != ' ':
        call_by=[]
        root_call_by=[]
        r=0
        function_ref=[]
        fun=[]
        while(r<function.__len__()):
            temp_ref= function[r].split('(')
            # temp_ref =temp_ref[0].split(' ')
            #local_function_ref= temp_ref[0]

            #local_function_ref= local_function_ref+temp_ref[0]
            function_ref.append(temp_ref[0])
            r = r + 1
        print(function_ref)
        lo = 0
        while(lo < function_ref.__len__()):
            local=re.sub(' +', ' ', function_ref[lo])
            local = local.split(' ')
            havij = crossref(local[1])

   # ret1 = havij[0].split('[')
            ret1=havij[0]
    #ret2 = havij[1].split('(')
            ret2= havij[1]
            call_by.append(ret2)
            root_call_by.append(ret1)

            lo = lo + 1

    counter = counter +1

    dependency_dictionary=[]
    dependency_dictionary= [function_name,function_type]
    dependency_dictionary.extend(local_variables)
    dependency_dictionary.extend(global_variables)
    dependency_dictionary.extend(function)


#df = pandas.DataFrame(data=data)
    s1 = pd.Series(function_name, name='Function Name')
    s2 = pd.Series(function_type, name='Function Type')
    s3 = pd.Series(local_variables, name ='local_variables')
    s4 = pd.Series(global_variables, name ='Global_variables')
    s5 = pd.Series(function, name ='Functions')
    s6 = pd.Series(root_call_by, name='Called By')
    s7 = pd.Series(call_by, name='dependent by')
#pd.set_option('display.max_colwidth', -1)
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None

    pd.set_option('expand_frame_repr', True)
    df = pd.concat([s1,s2,s3,s4,s5,s6,s7], axis=1)
    final_table.append(df)
#print(final_table)
with open(' File Contents Report.txt', 'w') as filehandle:
    filehandle.write('%s\n' % final_table)


print(call_by)
print(root_call_by)
