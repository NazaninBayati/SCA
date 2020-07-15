import Main
import sys
import json

class score(Main.Main):

    def logical_data_cleaning(self,logical_db, file_bascket):
        self.logical_db = logical_db
        self.file_basket = file_bascket
        logic = logical_db.split('RelationRecord(items=frozenset({')
        for i in range(1, logic.__len__() - 1):

            bascket = logic[i].split('}')
            #print(bascket.__len__())
            #print(bascket)

            bascket_members = bascket[0]
            support = bascket[1].split(',')[1].split('=')[1]
            #if bascket.__len__() <4:
               # confidence1to2 = bascket[2].split(',')[1].split('=')[1]
                #lift1to2 =bascket[2].split(',')[2].split('=')[1].split(')')[0]

           # if bascket.__len__()>3:

                #confidence1to2 = bascket[2].split(',')[1].split('=')[1]
                #lift1to2 = bascket[2].split(',')[2].split('=')[1].split(')')[0]
               # confidence2to1 =bascket[4].split(',')[1].split('=')[1]
                #lift2to1 =bascket[4].split(',')[2].split('=')[1].split(')')[0]

            if bascket_members not in file_bascket:
                file_bascket[bascket_members] = []
            file_bascket[bascket_members].append(support)
            #file_bascket[bascket_members].append(confidence1to2)
            #file_bascket[bascket_members].append(lift1to2)

        return file_bascket

    def structural_data_cleaning(self,structural_db, file_structural):
        self.structural_db = structural_db
        self.file_structural = file_structural
        struct = ''
        struct = structural_db.split('\n')
        print(" ")
        for i in range(0, struct.__len__()-1):
            str_spliter = struct[i].split(',')
            if str_spliter.__len__()>1:
                j=0
                str_formatter =[]
                a = str_spliter.__len__()
                while j < str_spliter.__len__()-2:
                    str_formatter .append(str(str_spliter[j]))
                    j = j+1
                str_formatter .append( str(str_spliter[j]))
            if str(str_formatter) not in file_structural:
                file_structural[str(str_formatter)] = []
            #file_structural[struct[i]].append(support)
        return file_structural





    def merge_score(self, file_structural, support_dict):
        self.file_structural = file_structural
        self.support_dict = support_dict

        for i in range(0,file_structural.__len__()-1):
            a = file_structural[i]
            b = support_dict
            if file_structural[i] in support_dict:
                print(support_dict[str(file_structural[i])])


    def main(self,logical_db,structural_db, file_bascket,file_structural ):
        self.logical_db = logical_db
        self.structural_db = structural_db
        self.file_bascket = file_bascket
        self.file_structural  = file_structural
        support_dict = score.logical_data_cleaning(self,logical_db, file_bascket)

        score.structural_data_cleaning(self, structural_db, file_structural)

        score.merge_score(self, file_structural, support_dict)


        json.dump(support_dict, open("logical.json", "w"))
        json.dump(file_structural, open("structural.json", "w"))


    def __init__(self):
        file_bascket = {}
        file_structural = {}
        #args_logical = sys.argv[1]
        args_logical ='/home/nazanin/PycharmProjects/ARM/result.txt'
        #args_structural = sys.argv[2]
        args_structural = '/home/nazanin/PycharmProjects/objectO/fils.csv'
        logical_db = Main.Main.Logical_data_load(str(args_logical))
        structural_db = Main.Main.Structural_data_load(str(args_structural))
        self.logical_db = logical_db
        self.structural_db = structural_db
        score.main(self,logical_db,structural_db, file_bascket,file_structural )

P1 = score()






