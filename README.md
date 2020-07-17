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
