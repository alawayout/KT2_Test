


def averageValue(list):
    sum = 0
    iter = 0
    for i in list:
        sum += i
        iter += 1;
    avg = sum/iter;
    print(avg)


averageValue([1,2,3,4,5])