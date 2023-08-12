#tute num 35
g=0
v=0
def shout(x):
    global v
    print("x in procedure is ",x)
    print("accessing global v again",v)
    v=v+1
    print("v again",v)
shout(5)    