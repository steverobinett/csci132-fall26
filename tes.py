tag = '</body>'
try:
    ndx = tag.index('u')
    print(ndx)
except ValueError:
    print('not found')