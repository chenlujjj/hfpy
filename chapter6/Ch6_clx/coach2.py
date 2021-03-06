def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)
        
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(',')
            data_dict = {}
            data_dict['Name'] = data.pop(0)
            data_dict['DOB'] = data.pop(0)
            data_dict['Times'] = str(sorted(set([sanitize(t) for t in data]))[:3])            
        return(data_dict)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)

james = get_coach_data('james2.txt')
print(james['Name'] + "'s fastest times are: " + james['Times'])
julie = get_coach_data('julie2.txt')
print(julie['Name'] + "'s fastest times are: " + julie['Times'])
mikey = get_coach_data('mikey2.txt')
print(mikey['Name'] + "'s fastest times are: " + mikey['Times'])
sarah = get_coach_data('sarah2.txt')
print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])
