import time
import datetime

def bubble_sort(f_lst):
    t1 = time.perf_counter_ns()
    lst = f_lst[0:]
    ln = len(lst)
    j = ln
    while j > 0:
        i = 0
        while i < j - 1:
            if lst[i] > lst[i+1]:
                lst[i+1], lst[i] = lst[i], lst[i+1]
            i+=1
        j -= 1
    t2 = time.perf_counter_ns()
    print(f'time == {t2 - t1}')    
    return lst                

def selection_sort(f_lst):
    t1 = time.perf_counter_ns()
    lst = f_lst[0:]
    ln = len(lst)
    i = 0
    j = 0
    while i < ln:
        min = lst[i]
        min_j = i 
        while j < ln:
            if lst[j] < min:
                min = lst[j]
                min_j = j
            j += 1
        lst[i], lst[min_j] = min, lst[i]
        i += 1
        j = i
    t2 = time.perf_counter_ns()
    print(t1, t2)
    print(f'time == {t2 - t1}')    
    return lst            

def insertion_sort(f_lst):
    t1 = time.perf_counter_ns()
    lst = f_lst[0:]
    ln = len(lst)
    i = 0
    while i < ln - 1:
        j = i
        if lst[i+1] < lst[i]:
            lst[i+1], lst[i] = lst[i], lst[i+1]
            while j-1 >=0:
                if lst[j] < lst[j-1]:
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                    j -= 1
                else:
                    break
        i += 1                
    t2 = time.perf_counter_ns() 
    print(f'time == {t2 - t1}')
    return lst

def quick_sort(f_lst):
    def sort(f_lst):
        lst = f_lst[0:]
        ln = len(lst)
        if ln <= 1:
            return lst
        else:
            sup_el = lst[ln-1]
            i = 0
            bef_sup_list = []
            after_sup_list = []
            while i < ln:
                if lst[i] <= sup_el:
                    bef_sup_list.append(lst[i])
                else:
                    after_sup_list.append(lst[i])
                i += 1            
            bef_sup_list = sort(bef_sup_list) if bef_sup_list != lst else sort(bef_sup_list[0:ln-1]) + [lst[ln-1]]
            after_sup_list = sort(after_sup_list)   
            lst = bef_sup_list + after_sup_list 
            return lst
    t1 = time.perf_counter_ns()
    lst = sort(f_lst)
    t2 = time.perf_counter_ns()
    print(f'time == {t2 - t1}')
    return lst    
    

def merge_sort(f_lst):
    def sort(f_lst):
        lst = f_lst[:]
        ln = len(lst)
        if ln <= 1:
            return lst
        else:
            i = 0
            mid = ln//2
            lst1, lst2 = sort(lst[0:mid]), sort(lst[mid:])
            nlst = []
            while i < ln:
                j, k = 0, 0
                ln1, ln2 = len(lst1), len(lst2)
                while ln1 > 0 and j < ln1:
                    min1 = lst1[0]
                    if lst1[j] < min1:
                        min1 = lst1[j]
                    j += 1

                while ln2 > 0 and k < ln2:
                    min2 = lst2[0]
                    if lst2[k] < min2:
                        min2 = lst2[k]
                    k += 1

                if ln1 == 0:
                    nlst.append(min2)
                    lst2.remove(min2)
                elif ln2 == 0:
                    nlst.append(min1)
                    lst1.remove(min1)   
                elif min1 < min2:
                    nlst.append(min1)
                    lst1.remove(min1)
                else:
                    nlst.append(min2)
                    lst2.remove(min2)
                i += 1                           
        return nlst
    
    t1 = time.perf_counter_ns()
    lst = sort(f_lst)
    t2 = time.perf_counter_ns()
    print(f'time == {t2 - t1}')
    return lst

def shell_sort(f_lst):
    t1 = time.perf_counter_ns()
    lst = f_lst[0:]
    ln = len(lst)
    n = 2
    while ln//n >= 1:
        i = 0
        j = i + ln//n
        while j <= ln - 1:
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
                a, b = i, j
                a -= ln//n
                b -= ln//n
                while a >=0:
                    if lst[b] < lst[a]:
                        lst[a], lst[b] = lst[b], lst[a]
                    a -= ln//n
                    b -= ln//n    
            i += 1
            j += 1    
        n *= 2 
    t2 = time.perf_counter_ns() 
    print(f'time == {t2 - t1}')    
    return lst               


