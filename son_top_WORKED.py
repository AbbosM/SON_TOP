from random import randint, sample
print("Keling SON TOP o'yini o'ynaymiz!")
while True:
    def son_pc(x, y)->int: # x->random son, y -> user number
        global t
        t=1
        while x != y:
            if y > x:
                print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:\n")
                y = eval(input(":"))
                t+=1
            elif y < x:
                print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:\n")
                y = eval(input(":"))
                t+=1
        print(f"TOPDINGIZ! {x} sonini o'ylagan edim. {t} ta taxmin bilan topdingiz. Tabriklayman!")
    son = randint(1,10)
    user_num=eval(input("1 dan 10 gacha son o'yladim. Topa olasizmi?: \n"))
    son_pc(son, user_num)
    any_key = input(print("1 dan 10 gacha son o'ylang. Men topishga harakat qilaman: \nSon o'ylagan bo'lsangiz istalgan tugmani bosing."))
    def son_user(m, n):#m-> user's number in mind, n-> PC's assumption
        t1=1
        l = [1,2,3,4,5,6,7,8,9,10]
        n = sample(l,1)
        #print(n)
        pc_num = n[0]
        user_check = input(print(f"Siz, {pc_num} sonini o'yladingiz: to'g'ri(T), bundan kattaroq (+), yoki kichikroq (-)?\n"))
        while user_check.title() != "T":
            if user_check =="+":
                del l[:l.index(pc_num+1)]
                #print(l)
                n = sample(l,1)
                print(n)
                pc_num = n[0]
                user_check = input(print(f"Siz, {pc_num} sonini o'yladingiz: to'g'ri(T), bundan kattaroq (+), yoki kichikroq (-)?\n"))
                t1+=1
            elif user_check =="-":
                del l[l.index(pc_num):]
                t1+=1
                #print(l)
                n = sample(l,1)
                print(n)
                pc_num = n[0]
                user_check = input(print(f"Siz, {pc_num} sonini o'yladingiz: to'g'ri(T), bundan kattaroq (+), yoki kichikroq (-)?\n"))
        print(f"Soningizni {t1} ta taxmin bilan topdim!")
        if t == t1:
            print(f"Durrang! Ikkimiz ham {t} ta taxmin bilan topdik" )
        elif t>t1:
            print(f"Men yutdim. Men {t1} ta taxmin bilan topdim, siz esa {t} ta taxmin bilan topdingiz!")
        else:
            print(f"Tabriklayman, siz yutdingiz. Men {t1} ta taxmin bilan topdim, siz esa {t} ta taxmin bilan topdingiz!")
    in_mind = []
    pc_assumption = []
    for i in range(1,11):
        in_mind.append(i)
    for i in range(1,11):
        pc_assumption.append(i)
    son_user(in_mind, pc_assumption)

    yana = eval(input(print("Keling yana bir marta o'ynaylik! ha(1), yo'q(0): ")))
    if yana == 0:
        break
    elif yana == 1:
        continue
