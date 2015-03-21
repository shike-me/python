#!/usr/bin/python
# Filename : seq.py

# 'ab' is short for 'a'ddress 'b'ook

ab = {'Swaroop' : 'wwd@qq.com',
	   'Larry' : 'larry@qq.com',
	   'Matsumoto' : 'matz@163.com',
	   'Spammer' : 'Spammer@gamil.com'
	   }

print "Swaroop's address is %s" % ab['Swaroop']

# adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)
for name, address in ab.items():
	print 'Contact %s at %s' % (name, address)

if 'Guido' in ab: # or  ab.has_key('Guido')
	print "\nGuido's address is %s" % ab['Guido']
