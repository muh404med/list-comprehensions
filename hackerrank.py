if __name__ == '__main__':
    x = 3
    y = 2
    z = 5
    n = 1
    il2 = []
    if ( z > y ) and (z > x):
        first_num = z
        if y > x :
            second_num = y
            third_num = x
        else:
            second_num = x
            third_num = y

    elif ( y > z ) and (y > x):
        first_num = y
        if z > x :
            second_num = z
            third_num = x
        else:
            second_num = x
            third_num = z
    elif y > x  :
        first_num = y
        if x > y :
            second_num = x
            third_num = y
        else:
            second_num = y
            third_num = x
    else:
        first_num = x
        second_num = z
        third_num = y
       


    num = int(str(first_num)+str(second_num)+str(third_num))
    for i in range(0,1000 ):
        try:
            if i < 10:
                il = [0 , 0 ]
                il.append(int(str(i)[0]))
                if ((il[0] == y ) or (il[0] == x) or (il[0] == z) or (il[0] == 0 ) or (il[0] < first_num )   ) and ((il[1] == y ) or (il[1] == x) or (il[1] == z) or (il[1] == 0 )  or (il[1] < first_num ))  and ((il[2] == y ) or (il[2] == x) or (il[2] == z) or (il[2] == 0 ) or (il[2] < first_num ) ) and (0<=il[0]<=x) and (0<=il[1]<=y) and (0<=il[2]<=z)  :
                            if sum(il) == n :
                                pass 
                            else:
                                
                                il2.append(il)
                                
            elif i < 100:
                il = [0]
                il.append(int(str(i)[0]))
                il.append(int(str(i)[1]))
                if ((il[0] == y ) or (il[0] == x) or (il[0] == z) or (il[0] == 0 ) or (il[0] < first_num )   ) and ((il[1] == y ) or (il[1] == x) or (il[1] == z) or (il[1] == 0 )  or (il[1] < first_num ))  and ((il[2] == y ) or (il[2] == x) or (il[2] == z) or (il[2] == 0 ) or (il[2] < first_num ) ) and (0<=il[0]<=x) and (0<=il[1]<=y) and (0<=il[2]<=z)  :
                            if sum(il) == n :
                                pass 
                            else:
                                
                                il2.append(il)
                                

            
                else:
                    pass

                        
            else:

                il =[]
                il.append(int(str(i)[0]))
                il.append(int(str(i)[1]))
                il.append(int(str(i)[2]))
                if ((il[0] == y ) or (il[0] == x) or (il[0] == z) or (il[0] == 0 ) or (il[0] < first_num )   ) and ((il[1] == y ) or (il[1] == x) or (il[1] == z) or (il[1] == 0 )  or (il[1] < first_num ))  and ((il[2] == y ) or (il[2] == x) or (il[2] == z) or (il[2] == 0 ) or (il[2] < first_num ) ) and (0<=il[0]<=x) and (0<=il[1]<=y) and (0<=il[2]<=z)  :
                            if sum(il) == n :
                                pass 
                            else:
                                
                                il2.append(il)
                                
        except IndexError:
            pass

    print(il2)
