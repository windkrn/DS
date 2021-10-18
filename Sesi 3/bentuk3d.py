def balok(p,l,t) :
    #fungsi menghitung segiempat
    volume_blk=p*l*t
    luas_blk = (2*((p*t)+(p*t)+(l*t)))
    print("volume_blk  : ", volume_blk)
    print("luas_blk     : ", luas_blk)

def kubus(s) :
    luas_kbs = 6*(s*s)
    volume_kbs=(s*s*s)
    print("luas kubus    : ",  luas_kbs)
    print("volume kubus: ",  volume_kbs)

def tabung(r,ti) :
    phi=22/7
    volume_tbg = phi*(r*r)*ti
    luas_tbg = 2*phi*r*(r+ti)
    print("luas_tbg   : ", luas_tbg)
    print("keliling lingkarana: ", volume_tbg)
