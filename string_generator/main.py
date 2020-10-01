import string,random

def string_generator(size, chars):
        return ''.join(random.choice(chars) for _ in range(size))
    
    
def get_option(option):    
    if option == 'alphabet':
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    elif option == 'numeric':
        characters = string.digits
    else:
        print('option out of context!')

    return characters

# choose want alphabet generic or numeric generic
option = 'alphabet'
# choose length of size string
size = 10

characters = get_option(option)

new_number = string_generator(size,characters)
print(new_number)