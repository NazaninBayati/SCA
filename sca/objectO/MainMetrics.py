import understand
import sys

class Metrics:
    def __int__(self,db):
        self.db = db

    def DBlodb(args):
        db = understand.open(str(args))
        return db

    def metric_val(self,file):
        self.file = file
        file_metric = []
        metrics = self.file.metric(self.file.metrics())

        for k, v in sorted(metrics.items()):
            file_metric.append(v)
        return file_metric

    def printresult(name,final_list,iterator,header):


        i = 0

        with open(str(name), 'w') as classhandle:
            i = 0
            classhandle.write(str(header))
            classhandle.write('\n')
            for listitem in final_list[i]:
                classhandle.write('%s;' % listitem)
                i = i + 1
                if i % iterator == 0:            classhandle.write('\n')


