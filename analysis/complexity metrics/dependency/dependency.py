import pandas as pd


db_cr = open("Program Unit Cross Reference.txt","r")
db_cr = db_cr.read()
db_cr_st=[]

db_cr_st = db_cr.split("\n\n")

db_cr_temp = db_cr_st[1:db_cr_st.__len__()]
db_cr_st=db_cr_temp

c=0
temp=[]


def crossref(func):
    cr_root_file=[]
    cr_callby_func=[]
    flag = False
    c=0
    while (c < db_cr_st.__len__() - 1):
        temp = db_cr_st[c].split('\n')
        temp2 = temp[0].split('(')
        temp2 = temp2[0].split(' ')
        #print(temp2[0])

        if func == temp2[0]:
            temp = db_cr_st[c].split(' ')

            t=0
            while t< temp.__len__()-1 :
                if temp[t]== 'Call':
                    cr_root_file = temp[t+1]
                    t = t+3
                    chase = t
                    flag=True
                if flag== True:
                    if temp[chase] == '':
                       chase= t
                    else:
                        cr_callby_func = temp[chase]
                        break
                t= t+1

        c = c + 1
        if cr_root_file==[]: cr_root_file = ''
        if cr_callby_func ==[] : cr_callby_func=''

    return (cr_root_file,cr_callby_func)




db = open("File Contents.txt","r")
db = db.read()
db_st=[]
db_st2=[]
db_st = db.split("\n\n")

db_temp = db_st[1:db_st.__len__()-1]
db_st=db_temp


db_list=[]
db_list=db_st[0].split("\n")

i=0
types=['  Types']
loc_var=['  Local Variables']
glob_var=['  Global Variables']
loc_func=['  Local Functions']

while(i<db_list.__len__()-1):
    if db_list[i]==types[0]:
        function_name = db_list[i-1]
        function_type = db_list[i+1]
    #    print(i)
    if db_list[i]==loc_var[0]:
        loc_var_number= i
      #  print(loc_var_number)
    if db_list[i]==glob_var[0]:
        glob_var_number= i
      #  print(glob_var_number)
    if db_list[i]==loc_func[0]:
        loc_func_number= i
        #print(loc_func_number)

    i = i+1

local_variables=db_list[loc_var_number:glob_var_number-1]
global_variables=db_list[glob_var_number:loc_func_number-1]
local_function=db_list[loc_func_number:db_list.__len__()-1]
lo = 1
call_by=[]
root_call_by=[]
r=0
local_function_ref=[]
while(r<local_function.__len__()-1):
    temp_ref= local_function[r].split('(')
   # temp_ref =temp_ref[0].split(' ')
    local_function_ref= temp_ref[0]
    r = r+1
print(local_function_ref)
while(lo < local_function.__len__()-1):

    havij = crossref(local_function[lo])

   # ret1 = havij[0].split('[')
    ret1=havij[0]
    #ret2 = havij[1].split('(')
    ret2= havij[1]
    call_by.extend(ret2)
    root_call_by.extend(ret1)

    lo = lo + 1

dependency_dictionary=[]
dependency_dictionary= [function_name,function_type]
dependency_dictionary.extend(local_variables)
dependency_dictionary.extend(global_variables)
dependency_dictionary.extend(local_function)


#df = pandas.DataFrame(data=data)
s1 = pd.Series(function_name, name='Function Name')
s2 = pd.Series(function_type, name='Function Type')
s3=pd.Series(local_variables, name ='local_variables')
s4=pd.Series(global_variables, name ='Global_variables')
s5=pd.Series(local_function, name ='local_Function')
#s6=pd.Series(call_by, name='Called By')
#pd.set_option('display.max_colwidth', -1)
pd.options.display.max_rows = None
pd.options.display.max_columns = None

pd.set_option('expand_frame_repr', True)
df = pd.concat([s1,s2,s3,s4,s5], axis=1)
#print(df)
with open(' File Contents Report.txt', 'w') as filehandle:
    filehandle.write('%s\n' % df)


print(call_by)
print(root_call_by)
