import robot
r = robot.rmap()
r.lm('task5')
r.sleep = 0.05
def task():
    def f():
        a = 0
        while a <= 1:     
            r.pt()
            r.dn(1)
            r.rt(1)
            r.pt()
            r.rt(1)
            r.up(1)
            r.pt()
            r.rt(2)
            a +=1
    def g():
        r.dn(2)
        while r.fl():
            r.lt()
        r.dn(1)
    f()
    g()
    f()
    g() 
    f()
r.start(task)



