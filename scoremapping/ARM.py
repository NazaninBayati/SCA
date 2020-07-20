from apyori import apriori
import sys

class arm:
    def __init__(self):
        args = "/home/nazanin/modified_DB_Ceph_summary.csv"
        db = open(str(args))
        db = db.read()
        arm.associationRM(self, db)

    def write(self, association_rules):
        with open('result.txt', 'w')as handler:
            for i in range(len(association_rules)):
                handler.write(str(association_rules[i]))
                handler.write('\n')

    def datacleaning(self,db):
        self.db = db
        temp = db.split('\n')
        i = 0
        while i < temp.__len__():
            temp[i] = temp[i].split(',')
            i = i + 1
        m=0
        n=0
        for m in range(0,len(temp)-1):
            for n in range(0,len(temp[m])-1):
                a = temp[m]
                b = temp[m][n]
                if str(temp[m][n]) == '':
                    counter = n
                    temp[m] = temp[m][0:n]
                    break
        return temp
    def associationRM(self,db):
        self.db = db
        dataset = arm.datacleaning(self,db)
        association_rules = apriori(dataset, min_support=0.1, min_confidence=0.2)
        association_rules = list(association_rules)
        arm.write(self,association_rules)



p1 = arm()