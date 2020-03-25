import pandas as pd
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
dependency_dictionary=[]
dependency_dictionary= [function_name,function_type]
dependency_dictionary.extend(local_variables)
dependency_dictionary.extend(global_variables)
dependency_dictionary.extend(local_function)

call_by =[]
#df = pandas.DataFrame(data=data)
s1 = pd.Series(function_name, name='Function Name')
s2 = pd.Series(function_type, name='Function Type')
s3=pd.Series(local_variables, name ='local_variables')
s4=pd.Series(global_variables, name ='Global_variables')
s5=pd.Series(local_function, name ='local_Function')
s6=pd.Series(call_by, name='Called By')
#pd.set_option('display.max_colwidth', -1)
pd.options.display.max_rows = None
pd.options.display.max_columns = None

pd.set_option('expand_frame_repr', True)
df = pd.concat([s1,s2,s3,s4,s5,s6], axis=1)
print(df)
with open(' File Contents Report.txt', 'w') as filehandle:
    filehandle.write('%s\n' % df)

def crossref(root_file, func):
    {
        print(i)
    }