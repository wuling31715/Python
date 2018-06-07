import requests
import numpy
import matplotlib


r = requests.get(url='https://www.facebook.com/')

input = raw_input('Name? ')
print 'Hello! %s' % (input)
