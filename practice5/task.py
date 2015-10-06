import robot
r = robot.rmap()
r.lm('task4')
r.sleep = 0.05
def task():
    def f():
        while r.fu():
            r.up()
        while r.fr():
            r.rt()
    def g(a):
        a = 0
        while a < 5:
            r.dn(1)
            r.lt(1)
            r.pt()
            a += 1
    f()
    g(5)
    f()
    r.dn(2)
    g(5)
    f()
    r.dn(4)
    g(5)
r.start(task)



