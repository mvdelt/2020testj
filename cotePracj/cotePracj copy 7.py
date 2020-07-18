d = {}
for i in range( 4 ):
    for j in range( 3 ):
        d.setdefault( i, [] ).append( j )
print(d)