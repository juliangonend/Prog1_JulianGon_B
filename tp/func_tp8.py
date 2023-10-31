
def total_digit(num):
    
    if num==0:
        return 0
    if num>0:
        num=abs(num)
        amount_digit=total_digit(num//10)+1
        return amount_digit
            # //5,25//
def is_power_of(n,b):
    if b<1:
        return False
    if b==1:
        return True
    if b%n==0:
        return is_power_of(n,b//n)
    else: 
        return False
    

def find_position(str1, str2, start, arr):
    len_str1 = len(str1)
    len_str2 = len(str2) + start

    if len_str2 <= len_str1:
        sub_string = str1[start:len_str2]

        if sub_string == str2:
            arr.append(start)  # Agregar la posición de la subcadena encontrada a la lista
        return find_position(str1, str2, start + 1, arr)
    else:
        return arr  # Devolver la lista al final
    
def is_number_even(num):
    if num==0:
        return "es par"
    elif num==1 :
        return"no es par"
    else:
        return is_number_even(num-2)
    
def is_number_odd(num):
    if num==0:
        return "no es impar"
    elif num==1 :
        return"impar"
    else:
        return is_number_odd(num-2)
    

def find_biggest_num(list,index,biggest):
    len_list=len(list)
    if len_list==index:
        return biggest
    else:
        if list[index]>biggest:
            biggest=list[index]
        return find_biggest_num(list,index+1,biggest)
    
def replicate_list(arr,new_arr,i):
    len_arr=len(arr)
    if len_arr==0:
     return new_arr
    else:
        number=arr.pop(0)
        new_arr.extend([number]*i)
        
        return replicate_list(arr,new_arr,i)

def K(n, p):
    if n == 1:
        return p
    else:
        return n * p + K(n - 1, p)
    
def pascal_triang(n,k,sum=0):

    if k == 0 or k == n:
        return 1
    else:
        return pascal_triang(n - 1, k - 1) + pascal_triang(n - 1, k)
    

def combinations(list, k, current_string='', res=[]):
    if k == 0:
        res.append(current_string)
    else:
        for char in list:
            combinations(list, k - 1, current_string + char, res)

    return res

def measurements_sheet_A(N):
    if N == 0:
        return (841, 1189) 
    broad, long = measurements_sheet_A(N - 1)

    new_width = long /2
    new_long= broad
    return (int(new_width), int(new_long))