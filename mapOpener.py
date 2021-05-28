
#mapOpener.py  to open google maps from a specified address

import webbrowser

print('Please enter address')
address = input()      
#print('Address is ' + address + ' ')
webbrowser.open('www.google.com/maps/dir/'+ address)



#TODO: create user interface
