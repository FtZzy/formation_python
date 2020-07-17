import copy


def typing_concept():
    my_var = 1  # It is an int
    print("The value of my var is %s and is a %s" % (my_var, type(my_var)))
    my_var += 1.0  # It is a float
    print("The value of my var is %s and is a %s" % (my_var, type(my_var)))


def using_is():
    a = 18
    b = 18
    c = 18.0

    if a == b:  # True
        print("a == b")
    if a == c:  # True
        print("a == c")

    if a is b:  # True
        print("a is b")
    if a is c:  # False
        print("a is c")


def structure_while():
    begin = 1
    end = 10
    # Example with continue
    while begin < end:
        begin += 1
        if begin % 2 == 0:
            continue
        print(begin)
    else:
        print("The final value is %s." % begin)

    # Exemple with break
    while True:
        print('Hey !')
        break
    else:
        print("It will never be display.")


def shallow_vs_deep_copy():
    """
    Quelle est la différence entre =, copy.deepcopy et copy.copy?
    = crée une référence au même objet. Si l'un est modifié, l'autre aussi.
    copy.deepcopy crée un objet différent.
    copy.copy, la shallow copie, fait une copie sur le premier id donc copie la
    liste mais pas ce qu'il y a à l'intérieur (contrairement à deepcopy). Ainsi
    si la liste contient une variable mutable elle peut être modifiée.
    """
    l0 = [0, 1, 2, 3, [4, 5], 6]
    l1 = l0  # l1 is l0 >>> True
    l2 = copy.copy(l1)  # l2 is l0 >>> False
    l3 = copy.deepcopy(l1)  # l3 is l0 >>> False
    print('Initial:\nl0 = l1 = l2 = l3 = %s' % l0)

    l0[0] = "Change l0"  # Change l0 and l1
    l1[1] = "Change l1"  # Change l0 and l1
    l2[2] = "Change l2"  # Change l2
    l3[3] = "Change l3"  # Change l3
    print('Change 1:\nl0 = %s\n l1 = %s\n l2 = %s\n l3 = %s' % (l0, l1, l2, l3))

    l0[4].append('Add l0')  # Change l0, l1 AND l2
    l1[4].append('Add l1')  # Change l0, l1 AND l2
    l2[4].append('Add l2')  # Change l0, l1 AND l2
    l3[4].append('Add l3')  # Change l3
    print('Change 2:\nl0 = %s\n l1 = %s\n l2 = %s\n l3 = %s' % (l0, l1, l2, l3))


if __name__ == "__main__":
    typing_concept()
    print('==========')
    using_is()
    print('==========')
    structure_while()
    print('==========')
    shallow_vs_deep_copy()
