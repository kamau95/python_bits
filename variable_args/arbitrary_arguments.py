def print_address(*args, **kwargs):
    print(kwargs.get('city'))
    for key, values in kwargs.items():
        print(f"key: {key} value: {values}")
    for value in args:
        print(value)


print_address(
        'ruiru',
        'kiambu',
        'kilimani',
        street = 'alphine',
        city = 'kamakis',
        poBox = '400 ruiru'
        )
