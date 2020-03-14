

import understand
import re
db = understand.open("fastgrep2.udb")
print(db.ents())
#for ent in sorted(db.ents(), key=lambda ent: ent.name()):
#    print(ent.name(), "  [", ent.kindname(), "]", sep="", end="\n")

# Create a regular expression that is case insensitive
searchstr = re.compile("r*.h", re.I)
for file in db.lookup(searchstr, "File"):
    print(file)

print("********************************")
metrics = db.metric(db.metrics())
for k, v in sorted(metrics.items()):
    print(k, "=", v)

print("**********************************")
for func in db.ents("function,method,procedure"):
  metric = func.metric(("Cyclomatic",))
  if metric["Cyclomatic"] is not None:
    print (func," = ",metric["Cyclomatic"],sep="")

print("*************************************")
for func in db.ents("function,method,procedure"):
  file = "callby_" + func.name() + ".png"
  print (func.longname(),"->",file)
  func.draw("Called By",file)

print("*********************************")
for func in db.ents("function,method,procedure"):
  for line in func.ib():
    print(line, end="")



file = db.lookup("r*.h")[0]
for lexeme in file.lexer():
  print (lexeme.text(),end="")
  if lexeme.ent():
    print ("@",end="")


