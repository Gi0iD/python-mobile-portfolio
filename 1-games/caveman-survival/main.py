#Caveman
#Noriel G. Cezar
ver=180

#added game modes

import random

def prcd():
 prc=input("\n...")
 if prc==1:
  pass
 else:
  pass

mode=1

print(f"  Welcome to Caveman ver:{ver}\nI'm Noriel G. Cezar creator of this\nmini winter survival game.\n\n")
mode=int(input("1. Normal mode\n2. Hard mode\n"))

if mode==2:
 print("\nRemember that in hardmode your save will auto delete after loading!\nplease be mindfull when existing without saving!")
 mode=0
 prcd()
elif mode==1:
 mode=1
else:
 mode=1
	
sav=int(input("\n1.Load\n2.New Game\n3.Exit\n"))

if sav==1:
 from cmsave import cmsave1 as cs1
 player=cs1.player
 hp=cs1.hp
 mhp=cs1.mhp
 en=cs1.en
 men=cs1.men
 hg=cs1.hg
 mhg=cs1.mhg
 day=cs1.day
 wea=cs1.wea
 fr=cs1.fr
 w=cs1.w
 x=cs1.x
 c=cs1.c
 po=cs1.po
 pp=cs1.pp
 fruit=cs1.fruit 
 wood=cs1.wood
 sap=cs1.sap
 flint=cs1.flint
 stick=cs1.stick
 glue=cs1.glue
 spear=cs1.spear
 inv=cs1.inv
 print("\nSaved Game Loaded!")
 
 if mode==0:
  print("\n Saved Data Deleted!\n")
  f=open("cmsave.py","w")
  f.write("class cmsave:\n")
  f.write(" def __init__(self,player,hp,mhp,en,men,hg,mhg,day,wea,fr,w,x,c,po,pp,fruit,wood,sap,flint,stick,glue,spear,inv):\n")
  f.write("  self.player=player\n")
  f.write("  self.hp=hp\n") 
  f.write("  self.mhp=mhp\n")
  f.write("  self.en=en\n")
  f.write("  self.men=men\n")
  f.write("  self.hg=hg\n")
  f.write("  self.mhg=mhg\n")
  f.write("  self.day=day\n")
  f.write("  self.wea=wea\n")
  f.write("  self.fr=fr\n")
  f.write("  self.w=w\n")
  f.write("  self.x=x\n")
  f.write("  self.c=c\n")
  f.write("  self.po=po\n")
  f.write("  self.pp=pp\n")
  f.write("  self.fruit=fruit\n") 
  f.write("  self.wood=wood\n")
  f.write("  self.sap=sap\n")
  f.write("  self.flint=flint\n")
  f.write("  self.stick=stick\n")
  f.write("  self.glue=glue\n")
  f.write("  self.spear=spear\n") 
  f.write("  self.inv=inv\n") 
  f.write(f"cmsave1=cmsave(\"???\",4,4,3,3,1,2,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,[])\n")
  f.close()
  
 prcd()

elif sav==2:
 player="???"
 hp=4
 mhp=4
 en=3
 men=3
 hg=1
 mhg=2
 day=1
 wea=0
 fr=0
 w=0
 x=1
 c=0
 po=0
 pp=0
 fruit=0 
 wood=0
 sap=0
 flint=0
 stick=0
 glue=0
 spear=0
 inv=[]

def weather():
 global wea
 global w
 if w==0:
  wea=random.randint(1,6)
  if wea >0 and wea <4:
   print("[ Sunny! ]")
   wea=0
  elif wea >3 and wea <6:
   print("[ Cloudy! ]")
   wea=1
  else:
   print("[ Raining! ]")
   wea=2
 else:
  if wea==0:
   print("[ Sunny! ]")
  elif wea==1:
   print("[ Cloudy! ]")
  else:
   print("[ Raining! ]")
 w=1

def make_fire():
 global wood
 global fr
 global hp
 global c
 if fr==0:
  mf=int(input("Make fire? 1 yes, 0 no "))
  if mf==1:
   if wood>0:
    wood=wood-1
    inv.remove("wood")
    fr=1
    c=0
    print("Cave man lit a campfire!")
   else:
    rim()
    c=c+1
    hp=hp-c
    print(f"Cold hurts! -{c} health!")
  else:
   c=c+1
   hp=hp-c
   print(f"Cold hurts! -{c} health!")
 else:
  print("Campfire keeps the Caveman warm...")
 
def forage():
 global wood
 global flint
 global fruit
 global sap
 global en
 frg=random.randint(1,6)
 if frg>1 and frg<4:
  inv.append("wood")
  wood=wood+1
  print("Got wood!")
 elif frg>3 and frg<6:
  print("Got flint!")
  flint=flint+1
  inv.append("flint")
 else:
  print("Got Fruit!")
  sap=sap+1
  inv.append("sap")
  fruit=fruit+1
  inv.append("fruit")
 en=en-1

def hunt():
 global hg
 global hp
 global en
 global fruit
 global spear
 hnt=random.randint(1,6)
 if hnt>1 and hnt<4:
  print("Got 2 fruits")
  inv.append("fruit")
  fruit=fruit+1
  inv.append("fruit")
  fruit=fruit+1
 elif hnt>3 and hnt<6:
  print("Got 4 fruits")
  i=0
  while i<4:
   inv.append("fruit")
   fruit=fruit+1
   i=i+1
 else:
  print("Got 8 fruits")
  i=0
  while i<8:
   inv.append("fruit")
   fruit=fruit+1
   i=i+1
 inv.remove("spear")
 spear=spear-1

def ws():
 print("Wrong selection!")

def nem():
 print("Not enough materials!")

def wi():
 print("Wrong input!")

def nee():
 print("Not enough energy!")

def rim():
 print("Required item missing!")

def ip():
 global po
 global pp
 po=int(input("position: "))
 pp=po-1
  

def sleep():
 global day
 global hg
 global mhg
 global men
 global en
 global mhp
 global hp
 global fr
 global w
 global x
 print("\nCave man slept!")
 day=day+1
 if hg<0:
  print("Starving...")
  print("Weakened!")
  print("Max health and energy -1!")
  men=men-1
  en=men
  mhp=mhp-1
  hp=mhp
  x=x-1
 elif hg>1 and hg<mhg:
  print("Satisfied...")
  print("Health and energy restored!")
  en=men
  hp=mhp
 elif hg>mhg+x-1 and en==men:
  if hp==mhp:
   print("Growth!")
   print("Max health and energy +1!")
   men=men+1
   mhp=mhp+1
   hg=hg-(mhg+x-1)
   x=x+1
 else:
  print("Satisfied...")
  print("Health and energy restored!")
  hp=mhp
  en=men
 hg=hg-1
 fr=0
 w=0
 

g=1 
  
while g!=0:
 print(f"\n[ Cave Man ver:{ver} ]")
#weather
 if day<4 and day>0:
  print("[ Sunny! ]")
  wea=0
 elif day>3 and day<16:
  weather()
 elif day>15 and day<40:
#Winter
  print("[ Winter! ]")
  wea=3
  make_fire()
 elif day>39:
  print("[ Sunny! ]")
  wea=0
   
 print(f"Caveman {player}\nHealth:{hp}/{mhp} Energy:{en}/{men} Belly:{hg}/{mhg+x}\n\nBag\nFruit:{fruit} Wood:{wood} Sap:{sap} Flint:{flint} Stick:{stick} Glue:{glue} Spear:{spear}\n\nDay:{day}")
 opt=int(input("Actions\n1.Craft 2.Forage 3.Eat 4.Sleep 5.Hunt 6.exit\n"))
 #actions
 if opt==1:
#Craft
  print(f"Bag\n{inv}")
  act=int(input("\nCraft\n1.stick\n2.glue\n3.spear\n"))
  if act==1:
#stick
   if wood>0:
    print(f"Bag\n{inv}")
    print("\nwood")
    ip()
    if inv[pp]=="wood":
     print("\nCrafted 2 sticks!")
     inv.remove("wood")
     wood=wood-1
     inv.append("stick")
     inv.append("stick")
     stick=stick+2
     en=en-1
    else:
     ws()
     continue;
   else:
    nem()
  elif act==2:
#glue
   if sap >0:
    print(f"Bag\n{inv}")
    print("\nsap")
    ip()
    if inv[pp]=="sap":
     print("Crafted glue!")
     inv.remove("sap")
     sap=sap-1
     inv.append("glue")
     glue=glue+1
     en=en-1
    else:
     ws()
     continue;
   else:
    nem()
  elif act==3:
#spear
   if en>1:
    if stick>0 and glue>0:
     if flint>0:
      print(f"Bag\n{inv}")
      print("\nstick")
      ip()
     if inv[pp]=="stick":
      print("\nglue")
      ip()
     else:
      ws()
      continue;
     if inv[pp]=="glue":
      print("\nflint")
      ip()
     else:
      ws()
      continue;
     if inv[pp]=="flint":
      print()
     else:
      ws()
      continue;
     print("Crafted Spear!")
     stick=stick-1
     inv.remove("stick")
     glue=glue-1
     inv.remove("glue")
     flint=flint-1
     inv.remove("flint")
     en=en-2
     inv.append("spear")
     spear=spear+1
    else:
     nem() 
   else:
    nee()
    continue;
  else:
   wi()
   continue;
 elif opt==2:
#Forage
  if wea==0 or wea==1:
   print("\nCave man foraged...")
   forage()
  elif wea==2:
   print("\nCave man foraged...\neven raining...\ncold hurts -1 health!")
   forage()
   hp=hp-1
  elif wea==3:
   print("The snow is thick!\nthere's nothing to forage...")
 elif opt==3:
#eating
  if fruit>0:
   print("\nCave man ate Fruit\n")
   fruit=fruit-1
   inv.remove("fruit")
   if en==men:
    print("Cave man is full of energy!")
    if hg==mhg+x:
     print("Cave man is full!")
    else:
     hg=hg+1
   else:
    en=en+1
    if hg==mhg+x:
     print("Cave man is full!")
    else:
     hg=hg+1
  else:
   rim()
   continue;  
 elif opt==4:
#Sleep
  sleep()
 elif opt==5:
#Hunt
  if spear>0:
   if wea==0 or wea==1:
    print("\nCave man hunt using spear!")
    hunt()
    en=en-1
   elif wea==2:
    print("\nCave man hunt using spear!\neven raining...\ncold hurts -1 health!")
    hunt()
    hp=hp-1
    en=en-1
   elif wea==3:
    if en>1:
     hp=hp-2+c
     print(f"\nCave man hunt using spear!\neven the snow is thick...\nextreme cold hurts -{2+c} health!")
     hunt()
     hg=hg-1
     en=en-2
    else:
     nee()
  else:
   rim()
   continue;
#save 
 elif opt==6:
  sav2=int(input("Save? 1 yes, 0 no\n"))
  if sav2==1:
   if player=="???":
    player=input("Enter Player name: ")
   print("\nsaving...")
   f=open("cmsave.py","w")
   f.write("class cmsave:\n")
   f.write(" def __init__(self,player,hp,mhp,en,men,hg,mhg,day,wea,fr,w,x,c,po,pp,fruit,wood,sap,flint,stick,glue,spear,inv):\n")
   f.write("  self.player=player\n")
   f.write("  self.hp=hp\n") 
   f.write("  self.mhp=mhp\n")
   f.write("  self.en=en\n")
   f.write("  self.men=men\n")
   f.write("  self.hg=hg\n")
   f.write("  self.mhg=mhg\n")
   f.write("  self.day=day\n")
   f.write("  self.wea=wea\n")
   f.write("  self.fr=fr\n")
   f.write("  self.w=w\n")
   f.write("  self.x=x\n")
   f.write("  self.c=c\n")
   f.write("  self.po=po\n")
   f.write("  self.pp=pp\n")
   f.write("  self.fruit=fruit\n") 
   f.write("  self.wood=wood\n")
   f.write("  self.sap=sap\n")
   f.write("  self.flint=flint\n")
   f.write("  self.stick=stick\n")
   f.write("  self.glue=glue\n")
   f.write("  self.spear=spear\n") 
   f.write("  self.inv=inv\n") 
   f.write(f"cmsave1=cmsave(\"{player}\",{hp},{mhp},{en},{men},{hg},{mhg},{day},{wea},{fr},{w},{x},{c},{po},{pp},{fruit},{wood},{sap},{flint},{stick},{glue},{spear},{inv})\n")
   f.close()
   print("\nGame Saved!")
   print("\nExiting program...\n")
   break;
  elif sav2==0:
   print("\nExiting program...\n")
   break;
  else:
   wi()
   continue;
 else:
   wi()
   continue;
   
#procced function  
 prcd()

#final ifs
 if en<1:
  sleep()
  prcd()

 if hg<-2+-x:
  mhp=0
  print("\nCave man died!\n")
  print(f"You only lasted {day} days!\n")
  if day<10:
   print("Your a Noob Cave man!")
  elif day<25 and day>9:
   print("Not Bad Cave man!")
  elif day<35 and day>24:
   print("Almost there Cave man!")
  
  break;

 if hp<1:
  print("\nCave man died!\n")
  print(f"You only lasted {day} days!\n")
  if day<10:
   print("Your a Noob Cave man!")
  elif day<25 and day>9:
   print("Not Bad Cave man!")
  elif day<35 and day>24:
   print("Almost there Cave man!")
  
  break;

 if day>39:
  print("\n\n[ Cave man Survived! ]")
  print(f"\nYou Survived {day} days!\n")
  print("You are ready for the Ice Age!")
  break;


    
