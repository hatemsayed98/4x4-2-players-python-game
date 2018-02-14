lol=[  0, 1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10, 11, 12, 13, 14, 15]
lst =[  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10, 11, 12, 13, 14, 15, 16]
string=[ 1  , 2  , 3  , 4  , 5  , 6  , 7  , 8  , 9  ,10,11,12,13,14,15,16]
print (*lst[0:4])
print (*lst[4:8])
print (*lst[8:12])
print (*lst[12:16])
while True:
        k=int(input("Player 1 (pick first square):" ))
        while lst[k-1]==100:
            k=int(input(" 'Error ' Player 1 (first rectangle): " )) 
        while k<1 or k >16 :  
            k=int(input(" 'Error ' Player 1 (first rectangle): " ))
    
             
        y=int(input("Player 1 (pick second square):" ))
        while lst[y-1]==100:
            y=int(input(" 'Error ' Player 1 (second rectangle): " ))
        while y<1 or y>16 :
            y=int(input(" 'Error ' Player 1 (second rectangle): " ))
        while abs(k-y) !=1 and  abs(k-y) !=4 :
            y=int(input(" 'Error ' Player 1 (second rectangle): " ))
        while (k==4 and y==5) or (k==8 and y==9) or (k==12 and y==13):
            k=int(input(" 'Error ' Player 1 (first rectangle): " ))
            y=int(input(" 'Error ' Player 1 (second rectangle): " ))
    
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
                        
                        elif (i!=3) and (i!=7) and (i!=11) and (i!=15)and (lst[i] !=100) and(lst[i]!=100) and (lst[i+1]!= 100):
                                l=False
                                break
                        elif (i>11):
                                break
                        else: 
                                if (lst[i]!=100)and (lst[i+4]!=100):
                                        l=False
                                        break
                if 1== False :
                        break                    
        if l ==True :
                print("Player 1 wins")
                break
        
        t=int(input("Player 2 (pick first square):" ))
        while lst[t-1]==100:
            t=int(input(" 'Error ' Player 2 (first rectangle): " ))
        while t<1 or t >16 :
            t=int(input(" 'Error ' Player 2 (first rectangle): " ))
            
        g=int(input("Player 2 (pick second square):" ))
       
        while g<1 or g>16 :
            g=int(input(" 'Error ' Player 2 (second rectangle): " ))
        while lst[g-1]==100:
            g=int(input(" 'Error ' Player 2 (first rectangle): " ))
        while abs(t-g) !=1 and  abs(t-g) !=4 :
            g=int(input(" 'Error ' Player 2 (second rectangle): " ))
        while (t==4 and g==5) or (t==8 and g==9) or (t==12 and g==13):
            t=int(input(" 'Error ' Player 2 (first rectangle): " ))
            g=int(input(" 'Error ' Player 2 (second rectangle): " )) 
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
                        
                        elif (i!=3) and (i!=7) and (i!=11) and (i!=15)and (lst[i] !=100) and(lst[i]!=100) and (lst[i+1]!= 100):
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
