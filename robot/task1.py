import robot
r = robot.rmap()
r.lm('task2')

def task():
    r.up(1)
    a = 0
    while a < 5:
        r.pt()
        r.up(1)
        r.rt(1)
        r.pt()
        r.dn(2)
        r.pt()
        r.rt(1)
        r.up(1)
        r.pt()
        r.rt(1)
        a +=1
r.start(task)



