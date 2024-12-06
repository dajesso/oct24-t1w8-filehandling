# Open a for writing - destructive - overwrites

file = open('new_file.txt', 'a') # write w and append a

file.write("Felicis was here\n")
file.write('See ya!\n')

file.close()

