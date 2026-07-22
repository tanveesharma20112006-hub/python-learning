"""lll                                                                   hh                    kk                   
lll   eee    aa aa pp pp      yy   yy   eee    aa aa rr rr       cccc hh        eee    cccc kk  kk   eee  rr rr  
lll ee   e  aa aaa ppp  pp    yy   yy ee   e  aa aaa rrr  r    cc     hhhhhh  ee   e cc     kkkkk  ee   e rrr  r 
lll eeeee  aa  aaa pppppp      yyyyyy eeeee  aa  aaa rr        cc     hh   hh eeeee  cc     kk kk  eeeee  rr     
lll  eeeee  aaa aa pp              yy  eeeee  aaa aa rr         ccccc hh   hh  eeeee  ccccc kk  kk  eeeee rr     
                   pp          yyyyy        """

year = int(input("Enter year:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print(" Not leap Year")
    else:
        print("Leap year")
else:
    print("Not a leap year")    