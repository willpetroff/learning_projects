def large_pal_rev(upper,lower):
    upper_limit=upper**2
    lower_limit=lower**2
    pal_test_ret=False
    while upper_limit>=lower_limit and pal_test_ret==False:
        x=int(str(upper_limit)[-1])
        y=int(str(upper_limit)[0])
        if pal_test_recur(str(upper_limit))==True:
            for i in range (100,1000):
                if upper_limit%i==0 and int(upper_limit/i)<=999:
                    return upper_limit, i, upper_limit/i
            else:
                upper_limit=upper_limit-10
        else:
            if x!=y:
                while x!=y:
                    upper_limit-=1
                    x=int(str(upper_limit)[-1])
                    y=int(str(upper_limit)[0])
                upper_limit-=10            
            else:
                upper_limit-=10

def pal_test_recur(string):
    if len(string)<=1:
        return True
    else:
        if string[0]==string[-1]:
            return pal_test_recur(string[1:len(string)-1])
        else:
            return False


def main():
    user_input_one=int(input('please enter a first int: '))
    user_input_two=int(input('please enter a second int: '))
    a=large_pal_rev(user_input_one,user_input_two)
    print (a)

main()
