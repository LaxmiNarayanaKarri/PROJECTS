import math
def check(x,y,m,l):
    for i in l:
        x1,y1=i
        #point 
        s=((y-y1)-(m*(x-x1)))
        #line through center
        if s==0:
            x2=(float)((2*x)-x1)
            y2=(float)((2*y)-y1)
            #fouth point
            X=(x2,y2)
            if X in l:
               X2=(x1,y1)
               fin=[X,X2]
               return fin
    return 0    
    
r=int(input("Enter the number of coordinates you are going to enter\n"))
#r is number of coordinates
l=[]
final=[]
for i in range(1,r+1):
    p=input("enter the coordinates x,y of point {}:\n".format(i)).split(",")
    p=tuple(map(float,p))
    t=p
    if t not in l:
        l.append(t)
if len(l)<=3:
    print("insufficient points")
else:
    for p1 in l:
        for p2 in l:
            if(p2!=p1):
                x1,y1=p1
                #x1,y1 is point1
                x2,y2=p2
                #x2,y2 is point2
                if x1!=x2:
                    m=(float)(y1-y2)/(x1-x2)
                    #slope of line
                    M=(-m)
                    #perendicular slope
                else:
                    M=0
                X=(float)(x1+x2)/2
                Y=(float)(y1+y2)/2
                res=check(X,Y,M,l)
                if res==0:
                    continue
                else:
                   p3,p4=res
                   ent=set((p1,p2,p3,p4))
                   d1=math.dist(p1,p3)
                   d2=math.dist(p1,p4)
                   if len(ent)==4 and d1!=d2:
                        if ent not in final:
                            final.append(ent)
    if(len(final)>0):
        print("total no of rectangle can be formed is {0}".format(len(final)))
        print("co-ordinates of rectangle are")      
        for i in final:
            print(i)
       
    else:
        print("rectangle cannot be formed with given points")
