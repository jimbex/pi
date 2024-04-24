
cnt = 0
dist = 0
sp = 0

def pulse(channel):
    global cnt, dist, sp
    cnt+=1
    dist += (3.142 * 0.026)/22
    sp = (cnt*60)/20
    sp = (sp *3.142 * 0.026)/60
    
def speed():
    global cnt
    cnt =0
    return sp

def distance():
    global dist
    return dist