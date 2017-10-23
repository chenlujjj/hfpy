import os
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')
    
    for each_line in data:
        if each_line.find(':') != -1:        
            (role, line_spoken) = each_line.split(':', 1)
            print(role+' said:'+line_spoken, end='')

    data.close()

else:
    print('The data file is missing!')
