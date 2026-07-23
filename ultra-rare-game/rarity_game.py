#Ultra rare practice
#fix rar,sra,ura selling!

ver=85
# fixing and adding stuff
# ver 78 layout and basic content and mechanics
#previous version has not been documented
import random

mon=0
nrm=0
unc=0
rar=0
sra=0
ura=0
qnt=0
day=0
mult=0
err=0



mon=1000

def prcd():
 prc=input("...")
 if prc=="1":
  pass
 else:
  pass
 

def nem():
 print("\nNot enough material!")
 
def wi():
 print("\nWrong Input!")
 
def slp():
 print("\nYou have eaten and slept in a decent room...")
 
def buy():
 global nrm
 global unc
 global rar
 global sra
 global ura
 rnd1=random.randint(1,2)
 if rnd1==1:
  print("\nEmpty pack!")
  prcd()
 else:
  rnd2=random.randint(1,6)
  if rnd2>0 and rnd2<4:
   print("\nGot 1 normal!")
   nrm=nrm+1
   prcd()
  elif rnd2>3 and rnd2<6:
   print("\nGot 1 Uncommon!")
   unc=unc+1
   prcd()
  else:
   rnd3=random.randint(1,6)
   if rnd3>0 and rnd3<4:
    print("\nGot 1 rare!")
    rar=rar+1
    prcd()
   elif rnd3>3 and rnd3<6:
    print("\nGot 1 Super rare!")
    sra=sra+1
    prcd()
   else:
    print("\nGot 1 Ultra rare!")
    ura=ura+1
    prcd()
 
def sell():
 global qnt
 global mon
 global s
 if x>0:
  qnt=input("How many?\n")
  qnt=int(qnt)
  if qnt>x:
   nem()
  else:
   pay=qnt*s
   mon=mon+pay
   print(f"\nEarned {pay:,}z")
 else:
  nem()
  
def eco():
 global mult
 eco=random.randint(1,2)
 if eco==1:
  eco2=random.randint(1,6)
  if eco2>0 and eco2<4:
   mult=0
  elif eco2>3 and eco2<6:
   mult=-1
  else:
   mult=-2
 else:
  eco2=random.randint(1,6)
  if eco2>0 and eco2<4:
   mult=0
  elif eco2>3 and eco2<6:
   mult=1
  else:
   mult=2
 


###########################
#Main Loop
###########################
g=1
while g!=0:
 z=0
 s=0
 
 #####################
 #Main UI
 #####################
 print(f"\n[ Ultra rare ver:{ver} ]\n")
 print(f"Money: {mon:,}z\nUR:{ura} SR:{sra} RA:{rar} UC:{unc} CO:{nrm}\n\nDay:{day} Economy:{mult}\n")
 act=input("Actions\n\n1.Work\n2.Vending Machine\n3.Sleep\n4.Craft\n5.Exit\n")
 
 ################
 #Work
 ################
 if act=="1":
  print("\nWorked! +1000z\n")
  mon=mon+1000
  mon=mon-500
  print("\nDaily expenses -500z!")
  slp()
  day=day+1
  eco()
 elif act=="2":
  act2=input("\nVending Machine\n1.Buy\n2.Sell\n")
  if act2=="1":
   qnt=input("\nHow many?\n")
   qnt=int(qnt)
   if mult==0:
    z=100
   elif mult==-1:
    z=(100/4)*3
   elif mult==-2:
    z=(100/2)
   elif mult==1:
    z=z+(100/2)
   elif mult==2:
    z=z+(100/4)*3
   bill=z*qnt
   if mon>=bill:
    mon=mon-bill
    i=0
    while i<qnt:
     buy()
     i=i+1
     if i==qnt:
      print(f"\nBill: {bill:,}z")
   else:
    print("\nNot enough money!")
  else:
   act2=input("\nSell what?\n1.Normal\n2.Uncommon\n3.Rare\n4.Super rare\n5.Ultra rare\n")
   if mult==0 and act2=="1":
    x=nrm
    s=500
    sell()
    if nrm>=qnt:
     nrm=nrm-qnt
    else:
     continue;
   elif mult==1 and act2=="1":
    x=nrm
    s=750
    sell()
    if nrm>=qnt:
     nrm=nrm-qnt
    else:
     continue;
   elif mult==2 and act2=="1":
    x=nrm
    s=1000
    sell()
    if nrm>=qnt:
     nrm=nrm-qnt
    else:
     continue;
   elif mult==-1 and act2=="1":
    x=nrm
    s=375
    sell()
    if nrm>=qnt:
     nrm=nrm-qnt
    else:
     continue;
   elif mult==-2 and act2=="1":
    x=nrm
    s=250
    sell()
    if nrm>=qnt:
     nrm=nrm-qnt
    else:
     continue;
   elif mult==0 and act2=="2":
    x=unc
    s=1000
    sell()
    if unc>=qnt:
     unc=unc-qnt
    else:
     continue;
   elif mult==1 and act2=="2":
    x=unc
    s=1500
    sell()
    if unc>=qnt:
     unc=unc-qnt
    else:
     continue;
   elif mult==2 and act2=="2":
    x=unc
    s=3000
    sell()
    if unc>=qnt:
     unc=unc-qnt
    else:
     continue;
   elif mult==-1 and act2=="2":
    x=unc
    s=750
    sell()
    if unc>=qnt:
     unc=unc-qnt
    else:
     continue;
   elif mult==-2 and act2=="2":
    x=unc
    s=500
    sell()
    if unc>=qnt:
     unc=unc-qnt
    else:
     continue;
   elif mult==0 and act2=="3":
    x=rar
    s=2000
    sell()
    if rar>=qnt:
     rar=rar-qnt
    else:
     continue;
   elif mult==1 and act2=="3":
    x=rar
    s=3000
    sell()
    if rar>=qnt:
     rar=rar-qnt
    else:
     continue;
   elif mult==2 and act2=="3":
    x=rar
    s=4000
    sell()
    if rar>=qnt:
     rar=rar-qnt
    else:
     continue;
   elif mult==-1 and act2=="3":
    x=rar
    s=1500
    sell()
    if rar>=qnt:
     rar=rar-qnt
    else:
     continue;
   elif mult==-2 and act2=="3":
    x=rar
    s=1000
    sell()
    if rar>=qnt:
     rar=rar-qnt
    else:
     continue;
   elif mult==0 and act2=="4":
    x=sra
    s=5000
    sell()
    if sra>=qnt:
     sra=sra-qnt
    else:
     continue;
   elif mult==1 and act2=="4":
    x=sra
    s=7500
    sell()
    if sra>=qnt:
     sra=sra-qnt
    else:
     continue;
   elif mult==2 and act2=="4":
    x=sra
    s=10000
    sell()
    if sra>=qnt:
     sra=sra-qnt
    else:
     continue;
   elif mult==0 and act2=="5":
    x=ura
    s=10000
    sell()
    if ura>=qnt:
     ura=ura-qnt
    else:
     continue;
   elif mult==1 and act2=="5":
    x=ura
    s=15000
    sell()
    if ura>=qnt:
     ura=ura-qnt
    else:
     continue;
   elif mult==2 and act2=="5":
    x=ura
    s=20000
    sell()
    if ura>=qnt:
     ura=ura-qnt
    else:
     continue;
   elif mult==-1 and act2=="5":
    x=ura
    s=7500
    sell()
    if ura>=qnt:
     ura=ura-qnt
    else:
     continue;
   elif mult==-2 and act2=="5":
    x=ura
    s=5000
    sell()
    if ura>=qnt:
     ura=ura-qnt
    else:
     continue;
  
    
 
 elif act=="3":
  if mon<500:
   print("\nNot enough money!")
   continue;
  else:
   slp()
   mon=mon-500
   day=day+1
   eco()
 
 elif act=="4":
  act2=input("\nCraft what?\n\n1.Uncommon\n2.Rare\n3.Super rare\n4.Ultra rare\n")
  if act2=="1":
   if nrm>=10:
    print("\nCrafted 1 Uncommon!")
    nrm=nrm-10
    unc=unc+1
   else:
    nem()
    continue;
  elif act2=="2":
   if unc>=10:
    print("\nCrafted 1 Rare!")
    unc=unc-10
    rar=rar+1
   else:
    nem()
    continue;
  elif act2=="3":
   if rar>=10:
    print("\nCrafted 1 Super rare!")
    rar=rar-10
    sra=sra+1
   else:
    nem()
    continue;
  elif act2=="4":
   if sra>=10:
    print("\nCrafted 1 Ultra rare!")
    sra=sra-10
    ura=ura+1
   else:
    nem()
    continue;
  else:
   wi()
   
  prcd()
  continue;

 elif act=="5":
  act2=input("\nExiting...") 
  g=0
     
 else:
  wi()
  
 prcd()
 
  
