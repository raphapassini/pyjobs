import re


def where_from_request(request):
    """ Return a dictionary to be used in a mongodb.collections.find()

    Args:
        request (flask.request): A Flask request object
    """
    where = {}
    for (field, value) in request.args.items():
        if not value:
            continue

        if field.find('___'):
            where.update(process_operator_filter(field, value))
        else:
            where.update({field: value})

    return where


def process_operator_filter(field, value):
    """ Process a mongo operador attached to a field like name__in, pay__gte

    Args:
        field (str): The field name
        value (str): The value
    """
    params = field.split('__')
    if len(params) is not 2:
        return {}

    field, operator = params

    operator_func = globals().get(operator + '_operator')
    if not callable(operator_func):
        return {}

    return operator_func(field, value)


def in_operator(field, values):
    """ Process the $in mongodb operator

    Args:
        field (str): The field name
        values (str): The value
    """
    regex_in = []

    for value in values.split(','):
        regex_in.append(re.compile("^{}$".format(value), re.IGNORECASE))

    return {
        field: {'$in': regex_in}
    }
