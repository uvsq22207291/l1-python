def all_squares():
    for a1 in range(1,16):
        for a2 in range(1,16):
            for a3 in range(1,16):
                for a4 in range(1,16):
                    for b1 in range(1,16):
                        somme = a1 + a2 + a3 + a4
                        c1 = somme - a1 - b1
                        b2 = somme - a3 - c1
                        b3 = somme - b1 - b2
                        c2 = somme - a2 - b2
                        c3 = somme - c1 - c2
                        M = MagicSquare( [a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4] )
                        if MisMagic() and 0 < b2 < 16 and 0 < b3 < 16 and 0 < c1 < 16 and 0 < c2 < 16 and 0 < c3 < 16 :
                            print(M)
                            print("---------------")
                        
all_squares()