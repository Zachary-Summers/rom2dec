#Roman Numerals Two Decimal Converter

'''
lowercase is the same as letter with dash on top
uppercase is normal with no dash
'''

def rom2dec(string):
    numb=0
    string=string[::-1]
    curnum=1
    for i in string:
        if i=='I':
            if curnum<=1:
                numb+=1
            else:
                numb-=1
        elif i=='V':
            if curnum<=5:
                curnum=5
                numb+=5
            else:
                numb-=5
        elif i=='X':
            if curnum<=10:
                curnum=10
                numb+=10
            else:
                numb-=10
        elif i=='L':
            if curnum<=50:
                curnum=50
                numb+=50
            else:
                numb-=50
        elif i=='C':
            if curnum<=100:
                curnum=100
                numb+=100
            else:
                numb-=100
        elif i=='D':
            if curnum<=500:
                curnum=500
                numb+=500
            else:
                numb-=500
        elif i=='M':
            if curnum<=1000:
                curnum=1000
                numb+=1000
            else:
                numb-=1000
        elif i=='v':
            if curnum<=5000:
                curnum=5000
                numb+=5000
            else:
                numb-=5000
        elif i=='x':
            if curnum<=10000:
                curnum=10000
                numb+=10000
            else:
                numb-=10000
        elif i=='l':
            if curnum<=50000:
                curnum=50000
                numb+=50000
            else:
                numb-=50000
        elif i=='c':
            if curnum<=100000:
                curnum=100000
                numb+=100000
            else:
                numb-=100000
        elif i=='d':
            if curnum<=500000:
                curnum=500000
                numb+=500000
            else:
                numb-=500000
        elif i=='m':
            if curnum<=1000000:
                curnum=1000000
                numb+=1000000
            else:
                numb-=1000000
        else:
            print('that number is not roman!')
    return numb