db_analyze = open("Class Metrics.txt","r")
db_analyze = db_analyze.read()
db_class_st=[]
db_class_st2=[]
db_class_st = db_analyze.split("\n\n")


i = 0
db_class_list=[]
db_st_temp=db_class_st[0].split('\n')
db_class_st = db_class_st[1:db_class_st.__len__()-1]
db_st_temp = db_st_temp[3:db_class_st.__len__()-1]
db_class_st.insert(0,db_st_temp)
db_temp2=""
j = 5

while(j<db_class_st.__len__()):
    # print(db_st[j])
    db__class_list = db_class_st[j].split("\n")
    # print(db_list)
    db_class_list = db_class_list[3:db_class_list.__len__()]
    # print(db_list)
    db_class_st[j] = ""
    db_class_st2.extend(db_class_list)
    j = j + 5

db_class_st.extend(db_class_st2)

print(db_class_st)
class_output=''

counter = 1
final_set=[]
analyze_counter=0
db_class_line=[]
db_class_insert=[]
#print(db_class_st)
while(counter<db_class_st.__len__()):
    db_class_line = db_class_st[counter].split('\n')
    #print(db_class_line)
    if db_class_line[0] != [] and db_class_line.__len__() > 1:
                #print(db_class_insert)
        name = []
        name = db_class_line[0].split("   ")
        name = name[name.__len__()-1]
        db_class_insert.append(name)

        line = []
        line = db_class_line[1].split("   ")
        line = line[line.__len__()-1]
        db_class_insert.append(line)

        blank_line = []
        blank_line = db_class_line[2].split("  ")
        blank_line = blank_line[blank_line.__len__()-1]
        db_class_insert.append(blank_line)

        line_code = []
        line_code = db_class_line[3].split("  ")
        line_code = line_code[line_code.__len__()-1]
        db_class_insert.append(line_code)

        line_comment = []
        line_comment = db_class_line[4].split("  ")
        line_comment = line_comment[line_comment.__len__() - 1]
        db_class_insert.append(line_comment)

        line_avg = []
        line_avg = db_class_line[5].split("  ")
        line_avg = line_avg[line_avg.__len__() - 1]
        db_class_insert.append(line_avg)

        line_comment_avg = []
        line_comment_avg = db_class_line[6].split("  ")
        line_comment_avg = line_comment_avg[line_comment_avg.__len__() - 1]
        db_class_insert.append(line_comment_avg)

        avg_complexity = []
        avg_complexity = db_class_line[7].split("  ")
        avg_complexity = avg_complexity[avg_complexity.__len__() - 1]
        db_class_insert.append(avg_complexity)

        max_complexity = []
        max_complexity = db_class_line[8].split("  ")
        max_complexity = max_complexity[max_complexity.__len__() - 1]
        db_class_insert.append(max_complexity)

        ratio = []
        ratio = db_class_line[9].split("  ")
        ratio = ratio[ratio.__len__() - 1]
        db_class_insert.append(ratio)


    analyze_counter = analyze_counter + 1





    final_set=(db_class_insert)


    counter = counter + 1


#print(final_set)
#print(final_table)
#print( dictionary_class)


#print(db_class_name_total)
#db_class_insert.append(used_classs)
print(final_set)

i=0
with open('Class Report.txt', 'w') as classhandle:

    #while i < final_set.__len__():
       for listitem in final_set:
            classhandle.write('%s;' % listitem)
            i= i +1
            if i %10 == 0:            classhandle.write('\n')
       #i = i+1




