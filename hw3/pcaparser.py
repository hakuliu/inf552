
def parsedatafile(filepath):
    result = []
    for line in open(filepath, 'r'):
        result.append(parseline(line))
    return result

def parseline(line):
    line = line.replace(' ','')
    split = line.split('\t')
    return [float(split[0]), float(split[1]), float(split[2])]