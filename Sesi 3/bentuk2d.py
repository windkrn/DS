def segiempat(p,l) :
    #fungsi menghitung segiempat
    keliling_segiempat = 2*int(p) + 2*int(l)
    luas_segiempat = int(p)* int(l)
    print("keliling_segiempat   : ",keliling_segiempat)
    print("luas segi empat      : ", luas_segiempat)

def segitiga(a,t) :
    keliling_segitiga= 3*int(a)
    luas_segitiga = (int(a)*int(t))/2
    print("luas segitiga    : ", luas_segitiga)
    print("keliling segitiga: ", keliling_segitiga)

def persegi(s) :
    keliling_persegi = 4 * int(s)
    luas_persegi = int(s) * int(s)
    print("luas segitiga    : ", luas_persegi)
    print("keliling segitiga: ", keliling_persegi)

def lingkaran(r) :
    keliling_lingkaran = 2* 22/7 * float(r)
    luas_lingkaran = 22/7* float(r) * float(r)
    print("luas lingkaran   : ", luas_lingkaran)
    print("keliling lingkarana: ", keliling_lingkaran)
