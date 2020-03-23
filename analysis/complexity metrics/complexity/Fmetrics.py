
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
print(db_st.__len__())
while(j<db_st.__len__()):
    print(db_st[j])
    db_list = db_st[j].split("\n")
    print(db_list)
    db_list= db_list[0:db_list.__len__()-3]
    print(db_list)
    db_st[j]=" "
    db_st2.extend(db_list)
    j = j + 4
#print(db_st)
db_st.extend(db_st2)
with open(' File Report.txt', 'w') as filehandle:
    for listitem in db_st:
        filehandle.write('%s\n' % listitem)
#print(db_st)
