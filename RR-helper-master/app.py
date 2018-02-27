from math import*
from cmath import*

def main():

    op = input('''
Type C4
Type RR
Type SC

or type E to exit
''')

    if op.upper() == 'C4':
        TimedEXP()

    elif op.upper() == 'RR':
        RRocket()

    elif op.upper() == 'SC':
        Satchel()

    elif op.upper() == 'E':
        iexit()

    else:
        main()

    main()
    TimedEXP()
    RRocket()
    Satchel()


def TimedEXP():
    in1 = 0
    n1i = in1
    while True:
        try:
            n1 = int(input('''
Enter the amount of C4 you want
'''))
        except ValueError:
            print('''
Invalid Response, please enter a integer.
''')
        else:
            break
        in1 = n1i
#C4------------------
    ie = n1*20
    ic = n1*5
    it = n1*2
#Explosives------------------
    ig = n1*1000
    il = n1*60
    i_s = n1*200
    im = n1*200

#Gun-Powder------------------
    a = 30*5
    r = 20*5
    sl = r*20*n1+i_s
    ch = a*20*n1


    print('''
Explosives:{}
Cloth:{}
Tec Trash:{}
Gun Powder:{}
Low Grade:{}
Metal Frags:{}
Total Sulfur:{}
Charcoal:{}

'''.format(ie, ic, it, ig, il, im, sl, ch))


def RRocket():
    in1 = 0
    n1i = in1
    while True:
        try:
            n1 = int(input('''
Enter the amount of Regular Rockets you want
'''))
        except ValueError:
            print('''
Invalid Response, please enter a integer.
''')
        else:
            break
        in1 = n1i
#RRocket------------------
    mp = n1*2
    gp = n1*150
    ie = n1*10
#Explosives------------------
    ig = n1*500+gp
    il = n1*30
    i_s = n1*100
    im = n1*100

#Gun-Powder------------------
#30*5 = 150
#20*5 = 100
#This means 150 sulfur and 100 charcoal is needed to make 1 explosive
    a = 30*5
    r = 20*5
    sl = r*20*n1+i_s
    ch = a*20*n1


    print('''
Metal Pipes:{}
Gun Powder:{}
Explosives:{}
Low Grade:{}
Metal Frags:{}
Total Sulfur:{}
Charcoal:{}

'''.format(mp, ig, ie, il, im, sl, ch))


def Satchel():
    in1 = 0
    n1i = in1
    while True:
        try:
            n1 = int(input('''
Enter the amount of Satchels you want:
'''))
        except ValueError:
            print('''
Invalid Response, please enter a integer.
''')
        else:
            break
        in1 = n1i
#Satchel------------------
    ib = n1*4
    hs = n1*1
    ic = n1*10
    ir = n1*1
#Beancan------------------
    gp = 60*4*n1
    mt = 20*4*n1
#Gun-Powder------------------
    s = 30*6
    r = 20*6
    sl = r*4*n1
    ch = s*4*n1


    print('''
Beancans:{}
Stashes:{}
Cloth:{}
Rope:{}
Gun Powder:{}
Metal Frags:{}
Total Sulfur:{}
Charcoal:{}

'''.format(ib, hs, ic, ir, gp, mt, sl, ch))


def iexit():
    ex = input('If you are sure you want to exit press "enter", if you would like to go back type B')

    if ex.upper() == '':
        exit()

    elif ex.upper() == 'B':
        main()

    else:
        iexit()

    main()


main()
