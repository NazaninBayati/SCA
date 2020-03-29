
db = open("File Metrics.txt","r")
db = db.read()
db_st=[]
db_st2=[]
db_st = db.split("\n\n")
#print(db_st.__len__())
i = 0
db_list=[]
#print(db_st[98])
#print(db.split("\n"))
db_temp = db_st[1:db_st.__len__()-1]
db_st=db_temp

db_temp2=""
j = 3
#print(db_st.__len__())
while(j<db_st.__len__()):
    #print(db_st[j])
    db_list = db_st[j].split("\n")

    db_list= db_list[0:db_list.__len__()-3]

    db_st[j]=" "
    db_st2.extend(db_list)
    #print(db_st2)
    j = j + 4
#print(db_st)
db_st.extend(db_st2)


space = [' ']
rel = 'RELATIVE:'
counter = 0
final_set=[]
while(counter<db_st.__len__()):
    db_line = db_st[counter].split('\n')
    print(db_line)
    if db_line != space:
        db_stmt = db_line[0].split("\\")
        db_insert = []
        #print(db_stmt)
        #len = db_line.__len__()
        #print(db_stmt)
        if db_stmt[0] == rel:
            db_insert=[]
            db_insert=db_line[1:db_line.__len__()]
            db_len=[]
            db_len= db_insert[1:db_line.__len__()]
            #db_insert=
            db_address = "/".join(db_stmt[1:db_stmt.__len__()-1])
            db_proj_name = db_stmt[db_stmt.__len__()-1]
            db_pfix = db_proj_name.split('.')
            if db_pfix[1]=='cpp' or db_pfix[1]=='h' or db_pfix[1]=='C':
                db_language = '   Language:                C++'
            if db_pfix[1] == 'c':
                db_language = '   Language:                C'
            #print(db_address)
            #print(db_proj_name)
            db_insert.insert(0,db_proj_name)
            db_insert.insert(1,db_address)
            db_insert.insert(2,db_language)
            #db_insert.append(db_len)
        else: final_set.append(db_line)
        final_set.append(db_insert)



    #print(db_stmt)
    counter = counter + 1


#with open(' File Report Version2.txt', 'w') as filehandle:
#    for listitem in db_st:
#        filehandle.write('%s\n' % listitem)
#print(db_st)

i=0
with open(' File Report.txt', 'w') as filehandle:
    while i < final_set.__len__():
        for listitem in final_set[i]:
            filehandle.write('%s\n' % listitem)
        i = i+1
