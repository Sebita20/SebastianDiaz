def by_name(item):
    return item['nombre']

def by_hegiht(item):
    return item['altura']

def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

def show_list(title, list_values):
    print()
    print(f"{title}")
    for index, element in enumerate(list_values):
        print(index, element)
    print()

def show_list_list(title, subtitle, list_values):
    print()
    print(f"{title}")
    for index, element in enumerate(list_values):
        print(index, element['nombre'])
        print(f"    {subtitle}")
        for second_index, second_element in enumerate(element['sublist']):
            print('    ', second_index, second_element)
    print()