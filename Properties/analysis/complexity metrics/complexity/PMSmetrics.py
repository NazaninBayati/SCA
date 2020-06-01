
db = open("Project Metrics Summary.txt","r")
db = db.read()
db_st=[]
db_st2=[]
db_st = db.split("\n")
#print(db_st.__len__())
i = 0
db_list=[]
print(db_st[0])
#print(db.split("\n"))
db_temp = db_st[2:db_st.__len__()-1]
db_st=db_temp
#print(db_st)

with open('Project Metrics Summary Report.txt', 'w') as filehandle:
    for listitem in db_st:
        filehandle.write('%s\n' % listitem)
#print(db_st)
