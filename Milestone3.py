import math
class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense

def getDataset(): # this is the table in doucmention
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]#24
    data.append(item(0, 0, 0, 0, labels[0]))
    data.append(item(0, 0, 0, 1, labels[1]))#
    data.append(item(0, 0, 1, 0, labels[2]))
    data.append(item(0, 0, 1, 1, labels[3]))#
    data.append(item(0, 1, 0, 0, labels[4]))
    data.append(item(0, 1, 0, 1, labels[5]))#
    data.append(item(0, 1, 1, 0, labels[6]))
    data.append(item(0, 1, 1, 1, labels[7]))#
    data.append(item(1, 0, 0, 0, labels[8]))
    data.append(item(1, 0, 0, 1, labels[9]))#
    data.append(item(1, 0, 1, 0, labels[10]))
    data.append(item(1, 0, 1, 1, labels[11]))#
    data.append(item(1, 1, 0, 0, labels[12]))
    data.append(item(1, 1, 0, 1, labels[13]))#
    data.append(item(1, 1, 1, 0, labels[14]))
    data.append(item(1, 1, 1, 1, labels[15]))#
    data.append(item(1, 0, 0, 0, labels[16]))
    data.append(item(1, 0, 0, 1, labels[17]))#
    data.append(item(1, 0, 1, 0, labels[18]))
    data.append(item(1, 0, 1, 1, labels[19]))#
    data.append(item(1, 1, 0, 0, labels[20]))
    return data
#######################################################
age=[]
pre=[]
ast=[]
rate=[]
label=[]
p=getDataset()
for i in range(len(p)):
    age.append(p[i].age)#list
    pre.append(p[i].prescription)
    ast.append(p[i].astigmatic)
    rate.append(p[i].tearRate)
    label.append(p[i].needLense)
#################################################################
def clearss(dataset=getDataset()):
    age.clear()
    pre.clear()
    ast.clear()
    label.clear()
    rate.clear()
    for i in range(len(dataset)):
        age.append(p[i].age)  # list
        pre.append(p[i].prescription)
        ast.append(p[i].astigmatic)
        rate.append(p[i].tearRate)
        label.append(p[i].needLense)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
def safe_div(x,y):
    if y == 0 or x==0:
        return 0
    return x / y
#######################
def Total_Entropy(list=[]): #only on label
    count_0_label=0
    count_1_label=0
    for i in range(len(list)):
        if list[i] == 0:
            count_0_label = count_0_label + 1
        if list[i] == 1:
            count_1_label = count_1_label + 1
    if count_0_label==0 or len(list)==0 :
        q=0
    else:
        q=math.log((count_0_label/len(list)),2)
        ##################################################
    if count_1_label == 0 or len(list) == 0:
        w = 0
    else:
        w = math.log((count_1_label / len(list)), 2)
    Total_Entropy = -1 * (safe_div(count_0_label , len(list)) * q) + -1 * (safe_div(count_1_label , len(list)) * w)  ##total entorpy
    #print(Total_Entropy)
    return  Total_Entropy
        ################################################################################
def check_0(fet=[]): #clear zero's
    for i in range(len(fet)):
        if fet[i] == 1:
            fet[i] = -1
            age[i] = -1
            pre[i] = -1
            ast[i] = -1
            label[i] = -1
            rate[i] = -1
    while age.count(-1) > 0:
        age.remove(-1)
        ##############
    while ast.count(-1) > 0:
        ast.remove(-1)
        ##################
    while label.count(-1) > 0:
        label.remove(-1)
        ###########################
    while rate.count(-1) > 0:
        rate.remove(-1)
    while fet.count(-1) > 0:
        fet.remove(-1)
    while pre.count(-1) > 0:
        pre.remove(-1)
    #print (len(ast))
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def check(fet=[]): #clear zero's
    for i in range(len(fet)):
        if fet[i] == 0:
            fet[i] = -1
            age[i] = -1
            pre[i] = -1
            ast[i] = -1
            label[i] = -1
            rate[i] = -1
    while age.count(-1) > 0:
        age.remove(-1)
        ##############
    while ast.count(-1) > 0:
        ast.remove(-1)
        ##################
    while label.count(-1) > 0:
        label.remove(-1)
        ###########################
    while rate.count(-1) > 0:
        rate.remove(-1)
    while fet.count(-1) > 0:
        fet.remove(-1)
    while pre.count(-1) > 0:
        pre.remove(-1)
    #print (len(ast))

#################################################################
def information_Gain(l=[]):
  c00=0
  c01=0
  c11=0
  c10=0
  pro_0=0
  pro_1=0

  for i in range(len(l)):
      #print(len(l))
      if l[i] == 0:
          pro_0 = pro_0 + 1

          if label[i] == 0:
              c00=c00+1
          if label[i] == 1:
              c01=c01+1
              #########################
      if l[i] == 1:
          pro_1 = pro_1 + 1
          if label[i] == 0:
              c10 = c10 + 1
          if label[i] == 1:
              c11 = c11 + 1
        ###########################
  if (c00 == 0 or pro_0 == 0):
        h_ = 0
  else:
    h_ = math.log((c00 / pro_0), 2)
  if (c01 == 0 or pro_0 == 0):
        h__ = 0
  else:
     h__ = math.log(c01 / pro_0, 2)
  if (c10 == 0 or pro_1 == 0):
        h___ = 0
  else:
          h___ = math.log(c10 / pro_1, 2)
  if (c11 == 0 or pro_1 == 0):
          h____ = 0
  else:
          h____ = math.log(c11 / pro_1, 2)
     ###################################3
  #print(Total_Entropy(label))
  information = Total_Entropy(label) - (safe_div(pro_0 , len(l)) * (-1 * (safe_div(c00 , pro_0) * h_ + safe_div(c01 , pro_0) * h__)) +safe_div(pro_1 , len(l)) * (-1 * (safe_div(c10 , pro_1) * h___ + safe_div(c11 , pro_1) * h____)))
  return information
#################################################
#################################################
class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1

class ID3:
    def __init__(self, features):
        self.features = features
    def classify(self, input):
        c1 = 1
        c2 = 1
        c3 = 1
        c4 = 1
        age_vale=input[0]
        pres_value=input[1]
        ast_value=input[2]
        rate_value=input[3]
        ###############Spilts inputs#################3
        for i in range(1, 5):
         lists=[]
         #global c1
         if c1 == 1 :
          lists.append(information_Gain(rate))
          #global c2
         if c2 == 1 :
          lists.append(information_Gain(age))
          #global c3
         if c3 == 1 :
          lists.append(information_Gain(pre))
          #global c4
         if c4 == 1 :
          lists.append(information_Gain(ast))
        #print(lists)
         lists.sort(reverse=True)
       # print(lists[0])
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
         #features[0].infoGain=
         #print(lists[0])
         if lists[0]==information_Gain(rate) and c1 == 1:
             out = 0
             counnters = 3
             counnters1 = 1
             counnters2 = 0
             for n in range(len(rate)):
                 if rate_value==rate[n]:
                     counnters2 =counnters2+1
                     if counnters==3:
                         counnters=label[n]
                         out = label[n]
                     elif counnters==label[n]:
                         counnters1=counnters1+1

             if counnters1==counnters2:
                 return out
             if rate_value==1:
              check(rate)
              c1 = 0
              #print("rate1")
             if rate_value==0:
                check_0(rate)
                c1=0
                print("rate0")
             if i==4:
                 return label[0]
           # rate = []
        #########################################
          # ######################
         elif lists[0] == information_Gain(age) and c2 == 1:
             out = 0
             counnters = 3
             counnters1 = 1
             counnters2 = 0
             for n in range(len(rate)):
                 if rate_value == rate[n]:
                     counnters2 = counnters2 + 1
                     if counnters == 3:
                         counnters = label[n]
                         out = label[n]
                     elif counnters == label[n]:
                         counnters1 = counnters1 + 1

             if counnters1 == counnters2:
                 return out
             if age_vale==1:
              check(age)
              c2 = 0
              #print("age1")
             if age_vale==0:
                 check_0(age)
                 c2=0
                 #print("age0")
             if i == 4:
                 return label[0]
          #  age = []
            ###################################################
         elif lists[0] == information_Gain(pre) and c3 == 1:
            out = 0
            counnters = 3
            counnters1 = 1
            counnters2 = 0
            for n in range(len(rate)):
                if rate_value == rate[n]:
                    counnters2 = counnters2 + 1
                    if counnters == 3:
                        counnters = label[n]
                        out = label[n]
                    elif counnters == label[n]:
                        counnters1 = counnters1 + 1

            if counnters1 == counnters2:
                return out
            if pres_value==1:
              check(pre)
              c3 = 0
              #print("pre1")
            if pres_value==0:
               check_0(pre)
               #print("pre0")
               c3=0
            if i == 4:
                return label[0]
          #  pre = []
           ####################################################
         elif lists[0] == information_Gain(ast) and c4 == 1:
            out = 0
            counnters = 3
            counnters1 = 1
            counnters2 = 0
            for n in range(len(rate)):
                if rate_value == rate[n]:
                    counnters2 = counnters2 + 1
                    if counnters == 3:
                        counnters = label[n]
                        out = label[n]
                    elif counnters == label[n]:
                        counnters1 = counnters1 + 1

            if counnters1 == counnters2:
                return out
            if ast_value==1:
             check(ast)
             c4 = 0
             #print("ast1")
            if ast_value==0:
               check_0(ast)
               c4=0
               #print("ast0")
            if i == 4:
                return label[0]
          #  ast = []



dataset = getDataset()
features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)

cls = id3.classify([1, 0, 1, 1])  # should print 1
print('testcase 1: ', cls)
'''
clearss(dataset)
cls = id3.classify([1, 1, 0, 0])  # should print 0
print('testcase 2: ', cls)
clearss(dataset)
cls = id3.classify([1, 1, 1, 0])  # should print 0
print('testcase 3: ', cls)
clearss(dataset)
cls = id3.classify([1, 1, 0, 1])  # should print 1
print('testcase 4: ', cls)
clearss(dataset)
'''

