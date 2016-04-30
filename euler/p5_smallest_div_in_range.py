def div_within_range(upper_limit):
    even_divis=False
    counter=1
    while even_divis==False:
        check_test=0
        for i in range (1,upper_limit+1):
            if counter%i==0:
                check_test+=1
        if check_test==upper_limit:
            even_divis=True
        else:
            counter+=1
    return counter

"""def div_faster(upper_limit):
    value=1
    value_2=0
    value_3=0
    for i in range (3,upper_limit):
        if i%2==0:
            value_2+=1
        elif i%3==0:
            value_3+=1
        else:
            value*=i
    value*=((2**value_2)*(3**value_3))
    return value"""

def main():
    user_input=int(input('Please enter a positive int: '))
    #print (div_within_range(user_input))
    print (div_faster(user_input))
