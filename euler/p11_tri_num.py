def tri_form_test(num):
    for i in range (num,1000):
        tri_n=int((i*(i+1))/2)
        counter=0
        for b in range (1,tri_n):
            while counter<=500:
                if tri_n%b==0:
                    counter+=1
                else:
                    pass
    return tri_n


def main():
    num=1
    print (tri_form_test(num))
