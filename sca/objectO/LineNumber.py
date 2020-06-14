import MainMetrics


db = MainMetrics.Metrics.DBlodb("/home/nazanin/cephDB.udb")

class Linenumber(MainMetrics.Metrics):
    def line(self, item):
        lin =''
        self.item = item
        def_str = ''
        end_str = ''

        lineString =''
        defineAref = self.item.ref("definein")
        if defineAref is not None:
            lineString = self.item.longname() + ","
            lineString += defineAref.file().longname()
        for ref in item.refs("define"):
            def_str = str(ref.line())

        for ref in item.refs("End"):
            end_str = str(ref.line())
        lin += str(item.longname())+', '
        lin += lineString + ', '
        lin += str(def_str) + ', '

        lin += str(end_str)
        return (lin)

    def main(self, db):
        self.db = db
        file_line = []
        class_line = []
        function_line = []
        for file in sorted(db.ents("function")):
            function_line.append(Linenumber.line(self, file))

        for file in sorted(db.ents("File")):

            if file.library() != "Standard":
                file_line.append(Linenumber.line(self,file))
        print(file_line)
        for item in sorted(db.ents("Class")):

            class_line.append(Linenumber.line(self, item))

    print("")






    def __init__(self):

        MainMetrics.Metrics.__init__(self)
        self.db = db
        Linenumber.main(self, db)

P1 = Linenumber()