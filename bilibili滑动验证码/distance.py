import random
v0=0
t=0.2
s=0
move_list=[]
mid=30/5*3
v_list=[1,2,3,4]
while s<30:
        if s<mid:
                a=v_list[random.randint(0,3)]
        else:
                a=-v_list[random.randint(0,3)]
        v=v0
        s1=v*t+0.5*a*t*t
        s1=round(s1)
        m_v=v+a*t
        v0=m_v
        print(a)
        move_list.append(s1)
        s+=s1

print(move_list)
