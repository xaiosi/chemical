# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from chemicals import CAS_from_any, MW, Tb
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def Tran(mass,material):
    b = CAS_from_any(material)
    temp = MW(b)
    res = mass / temp
    return res
def material_splite(num, wher):
    li = np.arange(num)
    contain = []
    for i in range(num):
        material = input()
        temp = CAS_from_any(material)
        li[i] = Tb(temp)
        contain.append(material)
    np.sort(li)
    res = np.arange(2)
    res[0] = li[wher-1]
    res[1] = li[wher]
    print('*'*20)
    for j in range(num):
        temp2 = contain[j]
        temp = CAS_from_any(temp2)
        temp3 = Tb(temp)
        if int(temp3) == res[0]:
            print(contain[j])
        elif int(temp3) == res[1]:
            print(contain[j])

def Flow(num):
    material = np.array([0.0005,0.0121,0.0287,0.5582,0.3372,0.0349,0.0203,0.0081])
    contain = ['a1','a2','a3','a4','a5','a6','a7','a8']
    QnF_list = []
    QnF = num
    QnD = 0
    QnW = 0
    for k in range(8):
        m = material[k] * QnF
        QnF_list.append(m)
    for i in range(3):
        temp = QnF_list[i]
        temp1 = QnF_list[7-i]
        QnD = QnD + temp
        QnW = QnW + temp1
    QnD = QnD + QnF_list[3]*0.83 + QnF_list[4]*0.27
    QnW = QnW + QnF_list[3]*0.17 + QnF_list[4]*0.73
    for j in range(8):
        print('QnF(a %d ):%f' % (j+1,QnF_list[j]))
    print('*'*30)
    print('QnD:%f' % (QnD))
    print('Qnw:%f' % (QnW))
    print('-'*30)
    for i in range(8):
        if i <= 2:
            print('X(a%d-D):%f' % (i+1, QnF_list[i] / QnD))
        elif i == 3:
            print('X(a4-D):%f' % (QnF_list[i]*0.83 / QnD))
            print('X(a4-W):%f' % (QnF_list[i] * 0.17 / QnW))
        elif i == 4:
            print('X(a5-D):%f' % (QnF_list[i]*0.27 / QnD))
            print('X(a5-W):%f' % (QnF_list[i] * 0.73 / QnW))
        else:
            print('X(a%d-W):%f' % (i+1,QnF_list[i] / QnW))




