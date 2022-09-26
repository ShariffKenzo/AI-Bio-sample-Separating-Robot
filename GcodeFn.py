from Automatedinput import *
from LogitechCamera import Pixelcount
from Saturationhsvfn import SampleDetector
from PlasmaHeight import PlasmaCount
from ColourTag import ColourTag
import time
from PipetteTipDetection import TipDetection
import math

#step1: go above testtube(X) with inde[i]   where i = 0 initially(testtube 1)
#step2: check if sample is preset using saturationhsv.py(check for white background) if empty go to index i++ else
# step3:go down(Z) using pixelcount() from logitechcamera
# step4:suck(E0) for eppendorf just suck ELSE use for loop n times based on height of testtube
# step5:go up(Z)->
# step6: move(X,Y) behind
# ->Step7: eject(E0)

### note that the testtube/eppendorf racks are of constant distance from each other

### manually calibrate for utmost right testtube

#### whilte True:

#step1: go above testtube(X) with inde[i]   where i = 0 initially(testtube 1)
### right to left

### Note yellow /test tube should come first

###### test tube top =75 test tube bototm  = 665, index 1 , x = 166, index 2, x =149, index3, x = 132, index 4 , x = 115, index 5,x =98  

##### eppendorf index 1 x= 169, index 2 x = 155, index 3 x = 141, index 4 x = 129, index 5 = 115
time.sleep(1)
samples = [0,0,0,0,0]

#if ColourTag(145,510) == 1:
# print("violet and eppendorf")
# samples[0] = SampleDetector(260, 630)
# samples[1] = SampleDetector(340,630)
# samples[2] = SampleDetector(425,630)
# samples[3] = SampleDetector(510,630) ## diff by 90 px for eppendorf
# samples[4] = SampleDetector(600,630)

# print(samples)

if ColourTag(835,160) == 2:
 print("yello and testtube")
 samples[0] = SampleDetector(282,670)
 samples[1] = SampleDetector(389,670)
 samples[2] = SampleDetector(495,670)
 samples[3] = SampleDetector(598,670) ## diff by 100 px for test tube
 samples[4] = SampleDetector(705,650)

 print(samples)

#print(TipDetection(300))


if ColourTag(145,510) == 1:
 print("violet and eppendorf tube")
 index = 0
 origin = int(45)
 for i in samples:
    #print(i)
    x = origin + int(int(index) * 10) ## traverse the testtubes
    if i == 1:
        #coords()  go to above front testtube
        #coords() # step3:go down(Z) using pixelcount() from logitechcamera
        #step4:suck(E0) for eppendorf just suck ELSE use for loop n times based on height of testtube
        #step5:go up(Z)->
        # step6: move(X,Y) behind
        # ->Step7: eject(E0)
        print(x)
    
    index =  index +1
    #print(index)

elif ColourTag(835,160) == 2:
 print("yellow and test tube")
 index = 0
 for i in range(5):
  if(samples[index]==1):
      

      if(index  == 0):
            depth  =  99 -Pixelcount(282,675,1) +6
            times  = math.floor(PlasmaCount(281,1))
            for i in range(times):
                  coords(159,33,120, 0, 0, 3000)
                  coords(159,33,120,18,0,300)
                  coords(159,33,depth,18, 2, 3000)
                  coords(159,33,depth,0, 5, 600) ## suck up
                  coords(159,33,120,0,3,3000)
                  coords(159,4,120,0,3,3000) ### move back
                  coords(159,4,120,18,5,500) ### eject
            #coords(4,110,120,0,0,3000)
            #coords(4,110,15,0,0,3000)
            #coords(4,138,15,0,0,3000)

      if(index  == 1):
            depth  =  99 -Pixelcount(389,675,2) +4
            times  = math.floor(PlasmaCount(389,2))
            for i in range(times):
                  coords(143,32,120, 0, 0, 3000)
                  coords(143,32,120,18,0,300)
                  coords(143,32,depth,18, 2, 3000)
                  coords(143,32,depth,0, 5, 600) ## suck up
                  coords(143,32,120,0,3,3000)
                  coords(143,3,120,0,3,3000) ### move back
                  coords(143,3,120,18,5,500) ### eject

      if(index  == 2):
            depth  =  99 -Pixelcount(495,675,3) +4
            times  = math.floor(PlasmaCount(495,3))
            for i in range(times):
                  coords(126,33,120, 0, 0, 3000)
                  coords(126,33,120,18,0,300)
                  coords(126,33,depth,18, 2, 3000)
                  coords(126,33,depth,0, 5, 600) ## suck up
                  coords(126,33,120,0,3,3000)
                  coords(126,4,120,0,3,3000) ### move back
                  coords(126,4,120,18,5,500) ### eject
      
      if(index  == 3):
            depth  =  99 -Pixelcount(598,675,4) +4
            times  = math.floor(PlasmaCount(598,4))
            for i in range(times):
                  coords(110,33,120, 0, 0, 3000)
                  coords(110,33,120,18,0,300)
                  coords(110,33,depth,18, 2, 3000)
                  coords(110,33,depth,0, 5, 600) ## suck up
                  coords(110,33,120,0,3,3000)
                  coords(110,4,120,0,3,3000) ### move back
                  coords(110,4,120,18,5,500) ### eject
      if(index  == 4):
            depth  =  99 -Pixelcount(705,675,5) +4
            times  = math.floor(PlasmaCount(705,5))
            for i in range(times):
                  coords(87,33,120, 0, 0, 3000)
                  coords(87,33,120,18,0,300)
                  coords(87,33,depth,18, 2, 3000)
                  coords(87,33,depth,0, 5, 600) ## suck up
                  coords(87,33,120,0,3,3000)
                  coords(87,4,120,0,3,3000) ### move back
                  coords(87,4,120,18,5,500) ### eject

 
  index =  index +1

 #   plasmaOrigin = 20
 #   plasmaHeight =  PlasmaCount(plasmaOrigin)%10  ## x coord only needed for plasma height
 #   for x in range(plasmaHeight):
 #    if i == 1:
        #coords()  go to above front testtube
  #          coords(x,y,z,e,0,3500)
        #coords() # step3:go down(Z) using pixelcount() from logitechcamera
  #          coords(x,y,z-Pixelcount(),e,0,3500)
        #step4:suck(E0) for eppendorf just suck ELSE use for loop n times based on height of testtube
  #          coords(x,y,z-Pixelcount(),e,0, 200)
        #step5:go up(Z)->
  #          coords(coords(x,y,z,e,0, 200))
        # step6: move(X,Y) behind
   #         coords(x,y-10,z,e,0, 200)
        # ->Step7: eject(E0)
   #         coords(x,y-10,z,e,0, 200)
 #            print(x)
    
 #   plasmaOrigin = plasmaOrigin + 1
    #print(index)