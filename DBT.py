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
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Zhangqi')
    material_splite(5,2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
