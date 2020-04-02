db = open("File Metrics.txt","r")
db = db.read()
db_st=[]
db_st2=[]
db_st = db.split("\n\n")

i = 0
db_list=[]

db_temp = db_st[1:db_st.__len__()]
db_st=db_temp

db_temp2 = ""
j = 3

while(j<db_st.__len__()):

    db_list = db_st[j].split("\n")

    db_list = db_list[0:db_list.__len__()-3]

    db_st[j] =" "
    db_st2.extend(db_list)
    #print(db_st2)
    j = j + 4

db_st.extend(db_st2)

file_output=''

space = [' ']
rel = 'RELATIVE:'
counter = 0
final_set=[]

#print(db_st)
while(counter<db_st.__len__()):
    db_line = db_st[counter].split('\n')
    #print(db_line)
    if db_line != space:
        db_stmt = db_line[0].split("\\")
        db_insert = []

        if db_stmt[0] == rel:
            db_insert=[]
            db_insert=db_line[1:db_line.__len__()]

            db_address = "/".join(db_stmt[1:db_stmt.__len__()-1])
            db_proj_name = db_stmt[db_stmt.__len__()-1]
            db_pfix = db_proj_name.split('.')
            if db_pfix[1] == 'cpp' or db_pfix[1] == 'h' or db_pfix[1] == 'C' or db_pfix[1] == 'hpp' or db_pfix[1] == 'hxx' or db_pfix[1] == 'cxx' or db_pfix[1] == 'H' or db_pfix[1] == 'inl' or db_pfix[1] == 'cc' or db_pfix[1] == 'hh':
                db_language = 'C++'
            if db_pfix[1] == 'c' :
                db_language = 'C'
            if db_pfix[1] == 'a' or db_pfix[1] == 'ads' or db_pfix[1] == 'gpr' or db_pfix[1] == 'ada' or db_pfix[1] == 'adb':
                db_language = 'Ada'
            if db_pfix[1] == 'cgi' or db_pfix[1] == 'pl' or db_pfix[1] == 'pm':
                db_language = 'Perl'
            if db_pfix[1] == 'css' :
                db_language = 'CSS'
            if db_pfix[1] == 'dpr' or db_pfix[1] == 'dfm':
                db_language = 'Delphi'

            if db_insert != []:
                #print(db_insert)
                line = []
                line = db_insert[0].split("   ")
                line = line[7]
                db_insert[0]=line

                comment = []
                comment = db_insert[1].split("   ")
                comment= comment[comment.__len__()-1]
                db_insert[1]=comment

                blank = []
                blank = db_insert[2].split("   ")
                blank = blank[blank.__len__() - 1]
                db_insert[2] = blank

                Prep_Lines = []
                Prep_Lines = db_insert[3].split("   ")
                Prep_Lines = Prep_Lines[Prep_Lines.__len__() - 1]
                db_insert[3] = Prep_Lines

                Code_Lines = []
                Code_Lines = db_insert[4].split("   ")
                Code_Lines = Code_Lines[Code_Lines.__len__() - 1]
                db_insert[4] = Code_Lines

                Inactive_Lines=[]
                Inactive_Lines = db_insert[5].split("   ")
                Inactive_Lines = Inactive_Lines[Inactive_Lines.__len__()-1]
                db_insert[5] = Inactive_Lines

                Exe_Lines = []
                Exe_Lines = db_insert[6].split("   ")
                Exe_Lines = Exe_Lines[Exe_Lines.__len__() - 1]
                db_insert[6] = Exe_Lines

                Decl_Lines = []
                Decl_Lines = db_insert[7].split("  ")
                Decl_Lines = Decl_Lines[Decl_Lines.__len__() - 1]
                db_insert[7] = Decl_Lines

                Exe_stmt = []
                Exe_stmt = db_insert[8].split("  ")
                Exe_stmt = Exe_stmt[Exe_stmt.__len__() - 1]
                db_insert[8] = Exe_stmt

                Decl_stmt = []
                Decl_stmt = db_insert[9].split("  ")
                Decl_stmt = Decl_stmt[Decl_stmt.__len__() - 1]
                db_insert[9] = Decl_stmt

                ratio = []
                ratio = db_insert[10].split("  ")
                ratio = ratio[ratio.__len__() - 1]
                db_insert[10] = ratio

                units = []
                units = db_insert[11].split("  ")
                units = units[units.__len__() - 1]
                db_insert[11] = units

            else:
                db_insert=[]

                j= counter + 1
                line = db_st[j].split("   ")
                line = line[7]
                db_insert.append( line)

                j = counter + 2
                comment = db_st[j].split("   ")
                comment= comment[comment.__len__()-1]
                db_insert.append(comment)

                j = counter + 3
                blank = db_st[j].split("   ")
                blank = blank[blank.__len__() - 1]
                db_insert.append(blank)

                j = counter + 4
                Prep_Lines = db_st[j].split("   ")
                Prep_Lines = Prep_Lines[Prep_Lines.__len__() - 1]
                db_insert.append(Prep_Lines)

                j = counter + 5
                Code_Lines = db_st[j].split("   ")
                Code_Lines = Code_Lines[Code_Lines.__len__() - 1]
                db_insert.append(Code_Lines)

                j = counter + 6
                Inactive_Lines = db_st[j].split("   ")
                Inactive_Lines = Inactive_Lines[Inactive_Lines.__len__() - 1]
                db_insert.append(Inactive_Lines)

                j = counter + 7
                Exe_Lines = db_st[j].split("   ")
                Exe_Lines = Exe_Lines[Exe_Lines.__len__() - 1]
                db_insert.append(Exe_Lines)

                j = counter + 8
                Decl_Lines = db_st[j].split("  ")
                Decl_Lines = Decl_Lines[Decl_Lines.__len__() - 1]
                db_insert.append(Decl_Lines)

                j = counter + 9
                Exe_stmt = db_st[j].split("  ")
                Exe_stmt = Exe_stmt[Exe_stmt.__len__() - 1]
                db_insert.append(Exe_stmt)

                j = counter + 10
                Decl_stmt = db_st[j].split("  ")
                Decl_stmt = Decl_stmt[Decl_stmt.__len__() - 1]
                db_insert.append(Decl_stmt)

                j = counter + 11
                ratio = db_st[j].split("  ")
                ratio = ratio[ratio.__len__() - 1]
                db_insert.append(ratio)

                j = counter + 12
                units = db_st[j].split("  ")
                units = units[units.__len__() - 1]
                db_insert.append(units)

            db_insert.insert(0,db_proj_name)
            db_insert.insert(1, db_language)
            db_insert.insert(2,db_address)







            final_set.append(db_insert)

    counter = counter + 1




i=0
with open('File Report.txt', 'w') as filehandle:

    while i < final_set.__len__():
       for listitem in final_set[i]:
            filehandle.write('%s;' % listitem)
       filehandle.write('\n')
       i = i+1




