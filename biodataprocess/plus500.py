import pandas as pd
import numpy as np

def op_txt(f):
 df=pd.read_table(f,"\t",header=0,index_col=1) 
 l1=list(range(1,501));l2=list(range(16570,17070))
 #l1=list(range(1,6));l2=list(range(6,11))
 match_pos=dict(zip(l1,l2))
 print(match_pos[1])
 match_pos2=dict(zip(l2,l1))
 for pos in match_pos.keys():
  #pos1d=dict(df.loc[pos]);pos2d=dict(df.loc[match_pos[pos]])
  if pos in df.index and match_pos[pos] in df.index:
   for col in df.columns:
    if type(df.loc[pos][col])==np.int64:
     df.loc[pos,col]=df.loc[pos][col]+df.loc[match_pos[pos]][col]
    else:
     df.loc[pos,col]=df.loc[pos][col]
   df.drop(labels=match_pos[pos],axis=0,inplace=True)
  elif pos in df.index and match_pos[pos] not in df.index:
   pass
  elif pos not in df.index and match_pos[pos] in df.index:
   df.loc[pos]=df.loc[match_pos[pos]] 
   df.drop(labels=match_pos[pos],axis=0,inplace=True)
  else:
   print(pos,match_pos[pos])
  #elif pos not in df.columns and match_pos[pos] not in df.columns:
   print(str(pos)+"not in TXT")
  #df.drop(labels=match_pos[pos],axis=0,inplace=True)
 df=df.fillna("NA")
 df=df.sort_index(axis=0)#row name sort(default);==sort pos column(pos is index) 
 #print df
 return df  

def sort_dict(d):
 sortedd=sorted(d.items(),key=lambda d:d[1],reverse=True)#not asceding
 max2gene,max2count=sortedd[1][0],sortedd[1][1]
 max1gene,max1count=sortedd[0][0],sortedd[0][1]
 return max1count,max1gene,max2count,max2gene

def value8(df,pos):
 ref=df.loc[pos,"ref"]
 #l=[num_A,num_T,num_C,num_G,num_a,num_t,num_c,num_g]=[df[pos,"A"],df[pos,"T"],df[pos,"C"],df[pos,"G"],df[pos,"a"],df[pos,"t"],df[pos,"c"],df[pos,"g"]]
 lu=[df.loc[pos,"A"],df.loc[pos,"T"],df.loc[pos,"C"],df.loc[pos,"G"]]
 ll=[df.loc[pos,"a"],df.loc[pos,"t"],df.loc[pos,"c"],df.loc[pos,"g"]]
 su=["A","T","C","G"]
 sl=["a","t","c","g"]
 du1,du2=dict(zip(su,lu)),dict(zip(lu,lu))
 dl1,dl2=dict(zip(sl,ll)),dict(zip(ll,sl))
 u1,ug1,u2,ug2=sort_dict(du1)
 l1,lg1,l2,lg2=sort_dict(dl1)
 return u1,ug1,u2,ug2,l1,lg1,l2,lg2,lu,ll,ref
 #sub
def sub_heter(df,rate):
 dsub,dheter={},{}
 for pos in df.index:
  u1,ug1,u2,ug2,l1,lg1,l2,lg2,lu,ll,ref=value8(df,pos)
  urate2=round(float(u2)/float(sum(lu)),4)
  lrate2=round(float(l2)/float(sum(ll)),4)
  if ug2==lg2.upper() and urate2>=rate and lrate2>=rate and u2>=3 and l2>=3:
   print(pos)
  if ug1==lg1.upper()!=ref and u1>=3 and l1>=3:
   dsub[pos]={}
   rate_=round(float(u1+l1)/float(sum(lu+ll)),4)
   dsub[pos]['REF']=ref
   dsub[pos]['UGENE']=ug1
   dsub[pos]['LGENE']=lg1
   dsub[pos]['UCNT']=u1
   dsub[pos]['LCNT']=l1
   dsub[pos]['FRQ']=rate_
 subdf=pd.DataFrame(dsub)
 subdf=subdf.T
 subdf.to_csv("sub.xls",sep="\t",index=True,float_format="%g")
 
def sub_heter_pos(df,rate,pos):
 u1,ug1,u2,ug2,l1,lg1,l2,lg2,lu,ll,ref=value8(df,pos)
 urate2=round(float(u2)/float(sum(lu)),4)
 lrate2=round(float(l2)/float(sum(ll)),4)
 if ug2==lg2.upper() and urate2>=rate and lrate2>=rate and u2>=3 and l2>=3:
  print(pos)
 else:
  print("no")
 
with open("fils.txt",'r') as fils:
 for i in fils:
  print(i)
  i=i.strip()
  name=i.split(".")[0]
  df1=op_txt(i)
  print(df1)
  sub_heter(df1,0.02)
  df1.to_csv(name+"_plus.txt",sep="\t",index=True)
