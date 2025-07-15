from utils import add_numbers, multiply_number

def validate_float(data):
    if not isinstance(data, list):
        return False
    for item in data:
        if not isinstance(item, float):
            return False
    return True

float_list = [1.3, 1.45, 8.12, 3.142, 6.4, 7.24]
print(validate_float(float_list))

bad_float_list = [1.3, 'haha', 7.56]
print(validate_float(bad_float_list))

x = 0
y = 1
for item in float_list:
    x = add_numbers(x, item)
    y = multiply_number(y, item)
print(x)
print(y)