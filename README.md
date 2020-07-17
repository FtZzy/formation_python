# Formation python
Prises de note de la formation python suivie en 2016. Il s'adresse à des personnes ayant des notions en développement ou en programmation. Bien entendu il s'adresse à des novices de Python. Cependant, nous n'aborderons pas son installation, l'environnement d'édition de texte. De plus, de nombreuses notions plus 'basiques' ne sont vues  qu'à l'oral.



## Séance 1: les notions générales
Fichier associé: `src/1st_course.py`

**Python**, qu'est-ce que c'est? Tout d'abord il s'agit d'un langage informatique comme *C/C++*, *Java*, *JavaScript*, *Scala*, ...


### Python en quelques mots
1. **Interprété**: la traduction se fait en temps réel, lors de l'exécution (contrairement à un langage compilé). Un même script peut ainsi être exécuté sur des plateformes différents mais cela a un impact sur les performances.
1. **Fortement typé**: les variables sont donc typées, les différences entre les chiffres et les lettres par exemple sont marquées. De plus, elles le sont *fortement* car Python différencie également les entiers et les réels, les caractères et les chaînes de caractères, ...
1. **Typage dynamique**: son typage est également dynamique, les variables peuvent changer de type et ne sont pas déterminées dès leur création (comme en *C++*, par exemple). Ainsi un int pourra devenir un float, puis un string, ... Nous devrons alors faire attention à nos types lors de notre développement.
1. **CPython**: l'implémentation de référence est écrite en C et se nomme CPython. Il existe aussi *Jython* en Java, *IronPython* en C#, *PyPy* en Python et d'autres encore.
1. **Introsectif**: tout est objet, même les types de base. Pour cette raison nous retrouverons par la suite des fonctions 'spéciale' sous la forme `__functionname__`. Nous pouvons avoir accès à toute les méthodes d'un objet via la fonctions `dir(my_var)` et savoir son fonctionnement avec `help(my_var.function)` qui nous donne la documentation.
1. **Tout est vrai**: en Python toutes les valeurs sont 'vraies' (*i.e. bool(18) >>> True*) sauf 0, False, None et ce qui est vide ([], {}, (,), ...)


### Quelques confrontations
1. **Muable Vs. Immuable**: un objet immuable ne sera pas modifiée en appelant une fonction tandis que ce sera le cas si elle est mutable (in place).
1. **== Vs. is**: l'égalité compare les valeurs tandis que `is` regarde l'id, c'est à dire s'il s'agit exactement du même objet. Nous l'utilisons également pour savoir si un objet est None.
1. **Listes Vs. Tuples**: les listes sont *mutables* alors que les tuples sont immuables. Nous utilisons donc ces dernières quand on veut être sûr de ne pas modifier les valeurs. Nous pouvons pour les deux utiliser les listes/tuples en compréhension (i.e. `[i for i in liste if (cond)]`)


### Les structures
1. Pour les structures **for** et **while** il existe un '`else`' qui est utilisé quand la boucle est menée à terme.
1. Pour ces mêmes structures, il existe **break** et **continue** permettant de casser la boucle ou passer à la valeur suivante.



## Séance 2: structures de données, collections et fonctions géniales

### Les dictionnaires
1. Les dictionnaires ne sont **pas ordonnées** et leurs clés sont uniques.
1. **Déclaration**: pour déclarer un dictionnaire nous utilisons `my_dict = {key1: val1, key2: val2}`. Nous pouvons également utiliser `vars(args)` qui va appeler `args.__dict__()`.
1. **Mutable**: un dictionnaire est mutable. En revanche, les *clés* doit impérativement être **immuable** (*i.e. la fonction `hash` ne renvoie pas d'erreur*)
1. **Obtention** d'une valeur. Pour obtenir une valeur du dictionnaire on préféra utiliser `my_dict.get(key, [default_value])` que `my_dict[key]` car cette deuxième solution renvoie une erreur si la clé n'est pas dans le dictionnaire tandis que la fonction *get* renverra `None` ou une valeur choisie.
1. On peut définir une **clé sans valeur** avec `my_dict.setdefault(key)`. La clé aura alors `None` comme valeur.
1. Nous pouvons les utiliser pour implémenter un *switch-case*, absent en Python.


### Les ensembles
1. Les ensembles sont des collections **non ordonnées** et **sans doublons**. Ils peuvent être utilisés pour la gestion des intersections et des unions.
1. Les ensembles sont **mutables**.
1. La **définition** se fait avec `set(my_values)`.
1. De nombreuses fonctions permettent de faire la 'différence' des éléments présents dans deux ensembles: `issubset`, `issuperset`, ...


### Les collections
Il existe bien entendu de nombreuses collections, certaines par défaut comme nous venons de voir. Mais nous pouvons trouver **toutes des collections disponibles** avec `import collections`.
Par exemple, il y les objets `Counter` ressemblants aux dictionnaires plus ou moins quelques fonctions. Nous pouvons trouver ainsi des collections très intéressantes!


### Quelques fonctions géniales
1. **any() Vs. all()**: ces fonctions permettent de savoir si l'un des items est vrai (*respectivement tous les items*) ou non. Par exemple, `any([False, True])` donnera `True` tandis que `all([False, True])` renverra `False`
1. **map()** permet d'appliquer une fonction à chaque item d'un itérable `map(my_func, my_iter)`. Il existe dans le même type **filter()** qui filtrent les items.
1. **zip()** permet de zip deux itérateurs de même taille, `list(zip((0,1,2), ['a', 'b', 'c'])) >>> [(0, 'a'), (1, 'b'), (2, 'c')]`
1. **Créer des itérateurs** afin de boucler efficacement avec `import itertools`. Ce module offre en effet de nombreux itérateurs: `count()`, `dropwhile()`, `combinations()`, ...
