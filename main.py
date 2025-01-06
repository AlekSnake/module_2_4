numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:               #перебираем весь список
    if i == 1:                  #пропускаем единицу т.к. оно ни то ни то и продолжаем цикл
        continue
    is_prime = True             #задаем флаговую переменную, значение которой будет меняться внутри цикла
    for j in range(2, i):       #перебираем делители 2-i для всех элементов списка
        if i % j == 0:          #если i делится на j без остатка, то это сооттветственно не простое число
            is_prime = False    #переменная меняет свое значение на False, если мы нашли делитель
            break               #заканчиваем внутренний цикл и переходим к поиску делителя следующего эл-та списка
    if is_prime == True:        #не нашел делитель, то переменная для элемента списка остается True
        primes.append(i)        #включаем этот элемент в список с простыми числами
    else:
        not_primes.append(i)    #иначе включаем его в список с составными числами(т.к. цикл нашел ему делитель кроме 1)

print(primes)
print(not_primes)