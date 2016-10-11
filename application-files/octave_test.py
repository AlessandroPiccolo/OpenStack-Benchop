from oct2py import octave

octave.run('Table.m')

#vars = octave.who(); print vars
print 'How many files i found'
print octave.filepathsBSeuCallUI()

print 'The times'
print octave.timeBSeuCallUI()

print 'The relative errors'
print octave.relerrBSeuCallUI()

#print octave.a()
#print octave.b()
