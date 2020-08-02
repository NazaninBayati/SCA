#from pydriller import RepositoryMining,GitRepository
#import subprocess
#import time
#subprocess.call([r'C:\Users\nazanin\Documents\api.bat'])
#subprocess.run([r'C:\Users\Lion\PycharmProjects\SCA-master (1)\SCA-master\analysis\FileLevel\Auto\metrics.bat'])
#time.sleep(1)
#https://stackoverflow.com/questions/7832770/how-to-get-certain-commit-from-github-project
#git checkout 00251f4355c8806215a9534a974097e371cc71f6
#0x7f4f0b5f3f60
"""B = GitRepository(path = '/home/nazanin/ceph',from_commit = 0x7f4f0b5f3f60)

#with open('/home/nazanin/git.bat','w')as handler:
    handler.write('git checkout 7f4f0b5f3f60')

for commit in RepositoryMining('/home/nazanin/ceph').traverse_commits():
    print('Hash {}, author {}'.format(commit, commit.author.name))

subprocess.call([r'/home/nazanin/git.bat'])
print("")
"""
#text = open("/home/nazanin/ceph",'r')


#with open(filename) as txt:

import os
from function_secondscenario.Main import *

path = '/home/nazanin/ceph'
db_path=[]
for root, directories, files in os.walk(path, topdown=False):
  for name in files:

    if name.split(".").__len__()>1 and name.split(".")[1]=='cc':
      db_path.append(os.path.join(root, name))



  #for name in directories:
    #print(os.path.join(root, name))


import re

class functionlevel:

  def clean_data(self,file_dict):
    self.file_dict = file_dict
    arr = file_dict.keys()
    for i in arr:
      cleaner = str(file_dict[str(i)]).split('(')[0].replace('[','').replace("]",'').replace('\\','')
      file_dict[str(i)] = [cleaner]
    #print(cleaner)

  def find_match_func(self, txt, dictio_func, file_dict,filename):

    self.txt = txt
    self.dictio_func = dictio_func
    self.file_dict = file_dict
    self.filename = filename

    i = dictio_func.__len__()-1
    while i >=0:
        res = functionlevel.match_items(self,dictio_func[str(i)])

        if res:
          if str(filename) not in file_dict:
            file_dict[str(filename)] = []

          file_dict[str(filename)].append(dictio_func[str(i)])
          functionlevel.clean_data(self,file_dict)
          i = i - 1
          break
        else:
              i = i - 1



  def match_items(self,item):

    self.item = item
    a = str(item[0])
    x = re.match("([\n\r\s]*)([a-zA-Z]*[a-zA-Z0-9]*)([\n\r\s]*)(int|void|float|char|double)([a-zA-Z0-9]*)([\n\r\s]*)([a-zA-Z][a-zA-Z0-9]*)([::]*)*([\(.*\)]*).*\{", str(item[0]))
    y = re.match("([\n\r\s]*)([a-zA-Z][a-zA-Z0-9]*)([::]+)([a-zA-Z][a-zA-Z0-9]*)([\(.*\)]*).*\{*",str(item[0]))
    #print(x)  # ([\n\r\s]*)([a-zA-Z][a-zA-Z0-9]*)([\n\r\s]*)([a-zA-Z][a-zA-Z0-9]*)([::]*)*([\(.*\)]*).*\{

    if x or y:
      print("YES! We have a match!")
      return True

    else:
      print("No match")
      return False



  def find_stmt(self,lookup,txt,dictio_func, file_dict, filename):

    self.lookup = lookup
    self.txt = txt
    self.dictio_func = dictio_func
    self.file_dict=file_dict
    self.filename = filename
    text = txt.split('\n')
    for num, line in enumerate(text):

      if str(num) not in dictio_func:
        dictio_func[str(num)] = []
      dictio_func[str(num)].append(str(line))
      if lookup in line:
        #print('found at line:', num)
        functionlevel.find_match_func(self, txt, dictio_func, file_dict, filename)
        break

  def lookup_stmt(self,lookup_dict):
    self.lookup_dict = lookup_dict

    db = open("/home/nazanin/PycharmProjects/pydriller/diff_parsed.txt",'r')
    db = db.read()
    db  = db.split("\n")
    for i in db:
      return_arr=[]
      string = i.split(":")
      j=1
      while j < string.__len__():
        if string[j]!='':
          str_temp = string[j].split(',')
          k = 0
          while k <str_temp.__len__():
            if re.findall("[a-zA-Z]",str_temp[k]):
              if re.findall("([\r\s]*)(added|deleted)",str_temp[k]):
                k = k + 1
                continue
              else :
                return_arr.append(str_temp[k])
            k = k + 1

        j = j + 1
      if return_arr != []:
        filename =  return_arr[return_arr.__len__()-1]

        if str(filename) not in lookup_dict:
          lookup_dict[str(filename)] = []
        lookup_dict[str(filename)].append(return_arr)

  def main(self,lookup_dict):

    self.lookup_dict = lookup_dict


    for i in db_path:
      txt = Main.load_db_functionlevel(str(i))




  def __init__(self):

    dictio_func={}
    file_dict = {}
    lookup_dict={}
    plain_txt = ''


    functionlevel.lookup_stmt(self,lookup_dict)
    functionlevel.main(self,lookup_dict)


    lookup = "void *_realloc"    #done
    filename = 'test'            #done
    txt = """int A::safe_cat(char **pstr, int *plen, int pos, const char *str2){
      int len2 = strlen(str2);

      //printf("safe_cat '%s' max %d pos %d '%s' len %d\n", *pstr, *plen, pos, str2, len2);
      while (*plen < pos + len2 + 1) {
        *plen += BUF_SIZE;
        if(a<b){
        }
        OpRequest::OpRequest(Message* req, OpTracker* tracker)
    : TrackedOp(tracker, req->get_throttle_stamp()),
      request(req),
      hit_flag_points(0),
      latest_flag_point(0),
      hitset_inserted(false) {
      ..
      }
        static void C(int pos, const char *str2):D{

        void *_realloc = realloc(*pstr, (size_t)*plen);

        if (!_realloc) {
       """

    #functionlevel.find_match_func(self, txt, dictio_func, file_dict, filename)
    functionlevel.find_stmt(self, lookup, txt, dictio_func, file_dict, filename)


p = functionlevel()