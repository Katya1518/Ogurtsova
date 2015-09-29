import robot
r = robot.rmap()
r.lm('task3')

def task():
    r.rt(1)
    a = 0
    while a < 3:
        r.rt(1)
        r.dn(1)
        r.up(1)
        r.rt(1)
        a +=1
    r.rt(1)
r.start(task)



