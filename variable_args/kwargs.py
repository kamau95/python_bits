def member_of_staff(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, values in kwargs.items():
        print(f"key is: {key} and its value is: {values}")

member_of_staff("monday", "tuesday", "wednesday", title = 'Dr', name = 'kinyua')
