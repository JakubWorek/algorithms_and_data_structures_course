'''
    5. Pojemniki z wodą
    Pojemniki z wodą na różnej wysokości, wlewamy wodę, który się 
    napełni pierwszy objętością A wody.
    Pytanie: ile pojemników zalanych zostanie w całości
    pojemnik (x1,y1,x2,y2)
    dana jest sekwencja pojemników w formie krotek oraz objętość A

'''

def fill_containers(A, total_water):
    # wyliczamy maksymalną wysokość
    max_y = 0
    for pojemnik in A:
        max_y = max(max_y,pojemnik[1])

    #wyliczamy ile na danej wysokości potrzeba wody
    cnt_x = [0]*(max_y+1)
    for pojemnik in A:
        for j in range(pojemnik[3]+1, pojemnik[1]+1):
            cnt_x[j] += (pojemnik[2]-pojemnik[0])

    #wlewamy wode
    height = 0
    while total_water >0:
        #todo: if cnt[h]-tw<0: odejmij else nie i break
        total_water -= cnt_x[height]
        height += 1
    if total_water != 0:
        height -= 1

    #zliczamy zapełnione pojemniki
    filled = []
    for pojemnik in A:
        if pojemnik[1]<=height: filled.append(pojemnik)

    return filled


def main():
    zbiorniki = [   (1, 5, 2, 3), (2, 4, 3, 1),
                    (5, 6, 10, 4), (9, 7, 11, 0), 
                    (2, 8, 3, 3), (1, 2, 2, 1), 
                    (1, 3, 2, 1)
                ]

    print(fill_containers(zbiorniki, 15))

if __name__ == '__main__': main()