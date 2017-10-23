data = open('sketch.txt')

for each_line in data:
    try:        
        (role, line_spoken) = each_line.split(':', 1)
        print(role+' said:'+line_spoken, end='')

    except:
        pass

data.close()
