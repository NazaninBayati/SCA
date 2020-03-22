
db = open("couchdb_complexity.txt","r")
db = db.read()
db_st=[]
db_st = db.split("\n\n")
#print(db_st.__len__())
i = 0
db_list=[]
#print(db_st[7])
#print(db.split("\n"))
db_temp = db_st[1:235]
db_st=db_temp

db_temp2=""
j = 6

while(j<91):
    #print(db_st[j])
    db_list = db_st[j].split("\n")
    print(db_list)
    db_list= db_list[0:8]
    print(db_list)
    db_st[j]=""
    db_st.extend(db_list)

    j = j + 7
#print(db_st)

with open(' Program Unit Complexity Report.txt', 'w') as filehandle:
    for listitem in db_st:
        filehandle.write('%s\n' % listitem)
#print(db_st)
