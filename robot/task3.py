import robot
r = robot.rmap()
r.lm('task4')

def task():
    def f():
        a = 0
        while a < 5:
            r.pt()
            r.dn(1)
            r.lt(1)
    def g():
        while r.fu():
            r.up()
        while r. fd():
            r.rt()
    g()
    f()
    g()
    r.dn(2)
    f()
    g()
    r.dn(4)
r.start(task)



