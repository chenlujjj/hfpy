def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[:3])

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_of_times):
        self.times.extend(list_of_times)



        
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(',')               
        return(Athlete(data.pop(0), data.pop(0), data))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)

james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))
julie = get_coach_data('julie2.txt')
print(julie.name + "'s fastest times are: " + str(julie.top3()))
mikey = get_coach_data('mikey2.txt')
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
sarah = get_coach_data('sarah2.txt')
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))  
