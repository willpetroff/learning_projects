from time import time

def test_1():
    a=[i for i in range (100000000)]
    counter=0
    start_time=time()
    while counter <len(a):
        counter+=1
    end_time=time()-start_time
    print (end_time)

def test_2():
    a=[i for i in range (100000000)]
    counter=0
    a_len=len(a)
    start_time=time()
    while counter <a_len:
        counter+=1
    end_time=time()-start_time
    print (end_time)


def main():
    test_1()
    test_2()


if __name__=='__main__':
    main()
