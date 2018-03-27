lol=[  0, 1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10, 11, 12, 13, 14, 15]
lst =[  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10, 11, 12, 13, 14, 15, 16]
string=[ 1  , 2  , 3  , 4  , 5  , 6  , 7  , 8  , 9  ,10,11,12,13,14,15,16]
print (*lst[0:4])
print (*lst[4:8])
print (*lst[8:12])
print (*lst[12:16])
while True:
        s=(input("Player 1 (pick first square):" ))
        R=True
        while R:
            if s.isdigit()==True:
                R=False
            else:
                print("Enter the number of the fisrt square")
                s=(input("Player 1 (pick first square):" ))
        k=int(s)
        
        while lst[k-1]==100:
            s=(input("Player 1 (pick first square):" ))
            R=True
            while R:
                if s.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the fisrt square")
                    s=(input("Player 1 (pick first square):" ))
            k=int(s)
        while k<1 or k >16 :  
            s=(input("Player 1 (pick first square):" ))
            R=True
            while R:
                if s.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the fisrt square")
                    s=(input("Player 1 (pick first square):" ))
            k=int(s)
    
             
        u=(input("Player 1 (pick second square):" ))
        R=True
        while R:
            if u.isdigit()==True:
                R=False
            else:
                print("Enter the number of the second sqaure")
                u=(input("Player 1 (pick second square):" ))
        y=int(u)
        
        while lst[y-1]==100:
            u=(input("Player 1 (pick second square):" ))
            R=True
            while R:
                if u.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the second sqaure")
                    u=(input("Player 1 (pick second square):" ))
            y=int(u)
        while y<1 or y>16 :
            u=(input("Player 1 (pick second square):" ))
            R=True
            while R:
                if u.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the second sqaure")
                    u=(input("Player 1 (pick second square):" ))
            y=int(u)
        while abs(k-y) !=1 and  abs(k-y) !=4 :
            u=(input("Player 1 (pick second square):" ))
            R=True
            while R:
                if u.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the second sqaure")
                    u=(input("Player 1 (pick second square):" ))
            y=int(u)
        while (k==4 and y==5) or (k==8 and y==9) or (k==12 and y==13):
            s=(input("Player 1 (pick first square):" ))
            R=True
            while R:
                if s.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the fisrt square")
                    s=(input("Player 1 (pick first square):" ))
            k=int(s)

            
            u=(input("Player 1 (pick second square):" ))
            R=True
            while R:
                if u.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the second sqaure")
                    u=(input("Player 1 (pick second square):" ))
            y=int(u)
    
        lst.remove(k)
        lst.insert(k-1,100)
        lst.remove(y)
        lst.insert(y-1,100)

        string.remove(k)
        string.insert(k-1,"X")
        string.remove(y)
        string.insert(y-1,"X")
        print (*string[0:4])
        print (*string[4:8])
        print (*string[8:12])
        print (*string[12:16])
        l=True
        for j in (lol):  
                for i in (lol):
                        if i==15:
                                break
                        
                        elif (i!=3) and (i!=7) and (i!=11) and (i!=15)and (lst[i]!=100) and (lst[i+1]!= 100):
                                l=False
                                break
                       
                        elif (lst[i]!=100)and (lst[i+4]!=100):
                                        l=False
                                        break
                if 1== False :
                        break                    
        if l ==True :
                print("Player 1 wins")
                break
        
        tw=(input("Player 2 (pick first square):" ))
        R=True
        while R:
            if tw.isdigit()==True:
                R=False
            else:
                print("Enter the number of the fisrt square")
                tw=(input("Player 2 (pick first square):" ))
        t=int(tw)


        
        while lst[t-1]==100:
            tw=(input("Player 2 (pick first square):" ))
            R=True
            while R:
                if tw.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the fisrt square")
                    tw=(input("Player 2 (pick first square):" ))
            t=int(tw)


        while t<1 or t >16 :
            tw=(input("Player 2 (pick first square):" ))
            R=True
            while R:
                if tw.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the fisrt square")
                    tw=(input("Player 2 (pick first square):" ))
            t=int(tw)


            
        gj=(input("Player 2 (pick second square):" ))
        R=True
        while R:
            if gj.isdigit()==True:
                R=False
            else:
                print("Enter the number of the second square")
                gj=(input("Player 2 (pick second square):" ))
        g=int(gj)


       
        while g<1 or g>16 :
            gj=(input("Player 2 (pick second square):" ))
            R=True
            while R:
                if gj.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the second square")
                    gj=(input("Player 2 (pick second square):" ))
            g=int(gj)

        while lst[g-1]==100:
            gj=(input("Player 2 (pick second square):" ))
            R=True
            while R:
                if gj.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the second square")
                    gj=(input("Player 2 (pick second square):" ))
            g=int(gj)

        while abs(t-g) !=1 and  abs(t-g) !=4 :
            gj=(input("Player 2 (pick second square):" ))
            R=True
            while R:
                if gj.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the second square")
                    gj=(input("Player 2 (pick second square):" ))
            g=int(gj)

        while (t==4 and g==5) or (t==8 and g==9) or (t==12 and g==13):
            tw=(input("Player 2 (pick first square):" ))
            R=True
            while R:
                if tw.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the fisrt square")
                    tw=(input("Player 2 (pick first square):" ))
            t=int(tw)
            
            gj=(input("Player 2 (pick second square):" ))
            R=True
            while R:
                if gj.isdigit()==True:
                    R=False
                else:
                    print("Enter the number of the second square")
                    gj=(input("Player 2 (pick second square):" ))
            g=int(gj)
 
        lst.remove(t)
        lst.insert(t-1,100)
        lst.remove(g)
        lst.insert(g-1,100)

        string.remove(t)
        string.insert(t-1,"X")
        string.remove(g)
        string.insert(g-1,"X")
        print (*string[0:4])
        print (*string[4:8])
        print (*string[8:12])
        print (*string[12:16])
        l=True
        for j in (lol):  
                for i in (lol):
                        if i==15:
                                break
                        
                        elif (i!=3) and (i!=7) and (i!=11) and (i!=15)and (lst[i]!=100) and (lst[i+1]!= 100):
                                l=False
                                break
                        elif (i>11):
                                break
                        else: 
                                if (lst[i]!=100)and (lst[i+4]!=100):
                                        l=False
                                        break        
                if 1== False:
                        break                        
        if l==True :
                print("Player 2 wins")
                break
print("Game Over")
