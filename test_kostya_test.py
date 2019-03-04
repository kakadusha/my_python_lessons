
'''
    Эй, задание к следующей субботе: Написать функцию, которая генерирует список списков, где каждый 
    i-ый внутренний список это последоватльнось от 1 до i. Например, для длины n=5 список будет такой 
    [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]. 
    Выйграет тот код, в котором будет меньше строчек кода. Проигравший оплачивает счет ))) Му-ха-ха-ха)))
'''


def l1(n):
    return [ [ y for y in range(1,x) ] for x in range(2,2+n) ]

def l2(now_lst, step_list, step):
    #print(step,'/',step_list,'/',now_lst)
    if step<5 :  
        return l2(now_lst+[step_list], step_list+[step] ,step+1)
    return now_lst+[step_list]




print( l1( 5 )) #int(input("Введите число i: ")) ) )
#print( [ [ range(1,x) ] for x in range(2,5) ] )
#print( [y for y in range(1,2)] )


#print( l2([],[1],2) ) 


def l3(i):
    return [y for y in range(1,i+1)]

#print(l3(5))

#print("lambda range ",(lambda i: [range(1,i+1)])(5))


def make_adder(n):
    return lambda x: n + x
li = []
add_li = make_adder(li)
#print("Add_li ",add_li([1]))
#print("Add_li ",add_li([1,2]))

add_li2 = lambda n: lambda x: n + x
#print(add_li2([1])(li))
#print("li:",[add_li2([li.append(y)])(li) for y in range(1,6)])

def l4(n,L):
    return [L+[L.append(y)] for y in range(1,n)]

print("lo:", l4(5,[]))
la = []
#print("la:", [la+[la+[y]] for y in range(1,6)])
