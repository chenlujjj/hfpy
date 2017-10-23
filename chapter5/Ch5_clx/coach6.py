from sanitize import *

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')


print(sorted(set([sanitize(each_t) for each_t in james]))[:3])
print(sorted(set([sanitize(each_t) for each_t in julie]))[:3])
print(sorted(set([sanitize(each_t) for each_t in mikey]))[:3])
print(sorted(set([sanitize(each_t) for each_t in sarah]))[:3])

        
        
