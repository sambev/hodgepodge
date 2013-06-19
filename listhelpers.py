def getNumDupes(list):
    """
    Get the count of duplicates in a list
    """
    dup_count = 0
    while list:
        index = list.pop(0)
        if index in list:
            dup_count += 1
            list = [x for x in list if x != index]
    return dup_count


def getDupes(list):
    """
    Get the duplicates from a list
    """
    dupes = []
    while list:
        index = list.pop(0)
        if index in list:
            dupes.append(index)
            list = [x for x in list if x != index]

    return dupes

