

def populate_object(obj, ignored=[], **kwargs):

    data = kwargs
    for element in data.keys():
        if element in ignored:
            data.pop(element)

    for name, value in data.items():
        if hasattr(obj, name):
            setattr(obj, name, value)

    return obj