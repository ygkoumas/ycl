def parse(source):
    ps = source.replace('\\n', ' ')
    ps = ps.split('\n')
    ps = filter(lambda x: x!='', ps) # get rid of empty lines of source code
    ps = filter(lambda x: x[0]!='#', ps) # get rid of the comments
    ps = map(lambda x: x.split(), ps)
    return ps
