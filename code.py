# _*_coding: utf-8 _*_
import random
import csv


def random_choice(max_value, num, k):
    data_list = random.choices(range(0, max_value), k=num - 1)
    data_list.insert(0, 0)
    data_list.append(max_value)
    data_list.sort()
    length = len(data_list)
    for i in range(length - 1):
        if (data_list[i + 1] - data_list[i]) > k:
            if data_list[i + 1] == length - 1:
                return False
            data_list[i + 1] = data_list[i] + k
    return data_list


def random_num_with_fit_total(max_value, num, k):
    while True:
        data_list = random_choice(max_value, num, k)
        if data_list:  # 直到满足和才结束
            break
    n = [data_list[i + 1] - data_list[i] for i in range(len(data_list) - 1)]

    print(n)
    print(len(n))
    print(sum(n))
    write_to_csv(n)


def write_to_csv(data, name='save.csv'):
    with open(name, mode='w', newline='') as fp:
        writer = csv.writer(fp)
        for t in data:
            writer.writerow([t])


def read_csv(name='save.csv'):
    with open(name, 'r') as fp:
        reader = csv.reader(fp)
        for line in reader:
            yield line


def size(data):
    x = len(data)
    if x:
        y = len(data[0])
    else:
        y = 0
    return x, y


def loop(k_value: int = 10, name='save.csv'):
    A = []
    for t in read_csv(name):
        t = int(t[0])
        Z = []
        for i in range(1, k_value + 1):
            if k_value < t:
                t = 0
            alpha = t/k_value
            L = (k_value * ((1 - alpha) ** k_value)) - 1
            Z.append(L)
        A.append(Z)
    with open("t_save.csv", 'w', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerows(A)


if __name__ == '__main__':
    K = 3
    T = 100
    P = 80
    random_num_with_fit_total(T, num=P, k=K)
    loop()