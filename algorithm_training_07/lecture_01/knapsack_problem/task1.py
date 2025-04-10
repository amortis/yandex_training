# Есть рюкзак грузоподъёмностью S и набор неделимых предметов с весами W.
# Можно ли заполнить рюкзак ими полностью?

# Например, S=9, и есть четыре предмета с весами 2,3,5,2.

weights = [2, 3, 5, 2]
s = 9


def can_fill(s:int, weights:list) -> bool:
    can_take = [False for _ in range(s + 1)]
    can_take[0] = True
    for weight in weights:
        for i in range(s - weight, -1, -1):
            if can_take[i]:
                can_take[i + weight] = True
    return can_take[-1]


print(can_fill(s, weights))
