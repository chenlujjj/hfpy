man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)

        except ValueError:
            pass

    data.close()
        
except IOError:
    print('The datafile is missing!')

import nester
try:
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        nester.print_lol(man, indent=True, level=0, fh=man_file)
        nester.print_lol(other, indent=True, level=0, fh=other_file)   
    
   
except IOError:
    print('File error.')


        

