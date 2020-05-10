class_address=[]
def contained_function(class_address):
    cls_func = open('cephdb._dictionary.txt', 'r')
    cls_func = cls_func.read()
    cls_int = []
    used_funcs = []
    db_cls_fun=[]
    cls_int = cls_func.split("\n\n")

    db_cls_fun = cls_int[1:cls_int.__len__()]
    print(db_cls_fun[18+18])
    cls_fun_counter = 0
    cls_list=[]

    flag = False
    while cls_fun_counter < db_cls_fun.__len__():
        if cls_fun_counter%18 == 0 and cls_fun_counter != 0:
            temp = db_cls_fun[cls_fun_counter].split('\n')
            temp = temp[0:temp.__len__()-3]
            db_cls_fun[cls_fun_counter] = ' '.join(temp)
            if db_cls_fun[cls_fun_counter+1].split('[').__len__()< 1:
                flag = True

        cls_list = db_cls_fun[cls_fun_counter].split('\n')
        cls_ckeck = cls_list[0].split('(')
        cls_func_name = []
        cls_func_name = cls_ckeck[0]
        if cls_ckeck[cls_ckeck.__len__()-1]=='Function)':
            #print("5555555")
            cls_temp_address=[]
            cls_address=[]
            if cls_list.__len__()>1 and cls_list.__len__()<4 and flag==False:
                #print(cls_list)
                cls_temp_address = cls_list[1].split('[')
                cls_address = cls_temp_address[1].split(',')
                if cls_address[0]== class_address:
                    print("**********************")
                    used_funcs.append(cls_func_name)

        cls_fun_counter = cls_fun_counter+1
    return used_funcs

a = contained_function("RELATIVE:\ceph\src\common\dout.h")
print(a)