
# digit 1: z=w+2
# digit 2: z=z*26 + (4+w)
# digit 3: z=z*26+(w+8)
# digit 4: z=z*26+(w+7)
# digit 5: z=z*26+(w+12)
# digit 6: z=z/26, x=z%26 - 14. If x == w, z doesn't change after that
# digit 7: z=z/26, x=z%26 - 0     if x == w, z doesn't change after that
# digit 8: z=z*26, x=z%26 +(14+w)
# digit 9: z=z/26, x=z%26 -10  if x == w, z doesn't change
# digit 10: z=z*26 +(w+6)
# digit 11: z=z/26, x=z%26-12 if x==w, z doesn't change after that
# digit 12: z=z/26, x=z%26-3 if x==w, z doesn't change
# digit 13: z=z/26, x=z%26-11 if x==w, z doesn't change
# digit 14: z=z/26, x=z%26-2 if x==w, z doesn't change

# part 1
for i in range(9,0,-1):
    for j in range(9,0,-1):
        print(f"{i} {j}")
        for k in range(9,0,-1):
            for l in range(9,0,-1):
                for m in range(9,0,-1):
                    for n in range(9,0,-1):
                        for o in range(9,0,-1):
                            """
# part 2
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            for l in range(1,10):
                for m in range(1,10):
                    for n in range(1,10):
                        for o in range(1,10):
                            """
                            res = [0]*14
                            
                            z=i+2
                            z=z*26+(4+j)
                            z=z*26+(8+k)
                            z=z*26+(7+l)
                            z=z*26+(12+m)

                            res[0]=i
                            res[1]=j
                            res[2]=k
                            res[3]=l
                            res[4]=m

                            # digit 6
                            x=z%26 -14
                            z=int(z/26)
                            if x <1 or x > 9:
                                continue
                            res[5]=x
                            
                            #digit 7
                            x=z%26 -0
                            z=int(z/26)
                            if x <1 or x > 9:
                                continue
                            res[6]=x
                            #print(f"z {z} x {x}")

                            #digit 8
                            z=z*26+(14+n)
                            res[7]=n

                            #digit 9
                            x=z%26 -10
                            z=int(z/26)
                            if x <1 or x > 9:
                                continue
                            res[8]=x

                            #digit 10
                            z=z*26+(6+o)
                            res[9]=o

                            #11
                            x=z%26 -12
                            z=int(z/26)
                            if x <1 or x > 9:
                                continue
                            res[10]=x


                            #12
                            x=z%26 -3
                            z=int(z/26)
                            if x <1 or x > 9:
                                continue
                            res[11]=x

                            #13
                            x=z%26 -11
                            z=int(z/26)
                            if x <1 or x > 9:
                                continue
                            res[12]=x

                            #14
                            x=z%26 -2
                            z=int(z/26)
                            if x <1 or x > 9:
                                continue
                            res[13]=x

                            print(f"Found {res}")
                            exit()
                            
                            
