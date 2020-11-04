tete = lambda l : l[0]
reste = lambda l: l[1:]


def nombreElements(list):
    if list ==[]:
        return 0
    else:
        return 1+nombreElements(reste(list))

def somme(list):
    if list == []:
        return 0
    else:
        return tete(list)+somme(reste(list))

def moyenne(list):
    return somme(list) / nombreElements(list)


def inserer(list, element):
    if nombreElements(list) == 1:
        if tete(list) < element:
            return list + [element]
        else:
            return [element] + list
    else:
        if tete(list) < element:
            return [tete(list)]+inserer(reste(list), element)
        else:
            return [element]+[tete(list)]+reste(list)


def tri(list):
    if len(list) <= 1:
        return list
    else:
        return tri([x for x in reste(list) if x <= tete(list)]) + [tete(list)] +\
            tri([x for x in reste(list) if x > tete(list)])



