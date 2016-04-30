def sieve_Erat(limit,desired_prime):
    limit_plus=limit+1
    list_one=[i for i in range(limit_plus)]
    list_one[1]=0
    for i in range (2,int(limit**.5)+1):
        if list_one[i]:
            list_one[i*i:limit_plus:i]=[0]*len(range(i*i,limit_plus,i))
    return list(filter(None,list_one))

def main():
    prime_limit=int(input('please enter an integer: '))
    desired_prime=0
    a=sieve_Erat(prime_limit,desired_prime)
    sum_total=0
    print (len(a))
    for i in a:
        sum_total+=i
    print (sum_total)
    print (a)
           

    
main()
