#!/usr/bin/env python
# encoding: utf-8


tl = [32, 24, 12, 321, 43, 12, 42, 6576]
for index, num in enumerate(range(len(tl) - 1, 0, -1)):
    print 'index ->', index, '|', 'num -> ', num, '|', 'range(num)->', range(num)

alist = [54,26,93,17,77,31,44,55,20]
tl = alist
for i,n in enumerate(range(len(tl) - 1, 0, -1)):
    for i,z in enumerate(range(num)):
        print 'i in range(num)-> ',i
        print 'tl[i]-->', tl[i], ' | ', 'tl[i+1]-->',tl[i+1]
        if tl[i] > tl[i+1]:
            tmp_l = tl[i]
            tl[i] = tl[i+1]
            tl[i + 1] = tmp_l
            print 'tmp_l--> ', tmp_l, ' | ', 'tl[i]--> ', tl[i]
            
