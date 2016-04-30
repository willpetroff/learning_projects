def farmyard_with_spiders(heads,legs):
    """This method calculates the number of chickens, pigs, and spiders in the farmyard given the number of heads and legs"""
    possible_solutions=[]
    for chickens in range (0,heads+1):
        for spiders in range (0,heads-chickens+1):
            pigs=heads-chickens-spiders
            ##print (chickens, pigs, spiders,((4*pigs)+(2*chickens)+(8*spiders)))
            if (4*pigs)+(2*chickens)+(8*spiders)==legs:
                ans=[pigs,chickens,spiders]
                possible_solutions.append(ans)
    if len(possible_solutions)>0:
        print (possible_solutions)
        #return possible_solutions
    else:
        print ('There are no accpetable answers for the parameters given')
        return None

def main():
    heads=int(input('Please enter the number of heads in the farmyard: '))
    legs=int(input('Please enter the number of legs in the farmyard: '))
    farmyard_with_spiders(heads,legs)

main()
