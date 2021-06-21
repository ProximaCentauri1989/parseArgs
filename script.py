import sys

def isInteger(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False

def isFloat(obj):
    try:
        float(obj)
        return True
    except ValueError:
        return False

def parseArgs(args, out):
    if len(args) < 1:
        raise Exception("No arguments provided")

    ''''
    isinstance(arg, type) does not work because all args are strings be default. Do not use it. Manual checking required
    collecting of arguments can be performed as showed below but manual for loop is a better way:
    out['integers'] = [arg for arg in args if isInteger(arg)]
    out['floats'] = [arg for arg in args if not isInteger(arg) and isFloat(arg)]
    out['strings'] = [arg for arg in args if not isInteger(arg) and not isFloat(arg)]
    '''

    for arg in args:
        if isInteger(arg):
            out['integers'].append(int(arg))
        elif isFloat(arg):
            out['floats'].append(float(arg))
        else:
            out['strings'].append(arg)

    return

def printArgs(args):
    if len(args['integers']) > 0:
        print('Integers: {}'.format(args['integers']))
    if len(args['floats']) > 0:
        print('Floats: {}'.format(args['floats']))
    if len(args['strings']) > 0:
        print('Strings: {}'.format(args['strings']))

def findSubstrings(strToFind, arrOfStrings, out):
    for s in arrOfStrings:
        if strToFind in s and strToFind != s:
            out.append(s)

def main():
    parsedAgs = {
        'integers': [],
        'floats': [],
        'strings': []
    }

    if len(sys.argv) == 1:
        print("No arguments provided")
        return

    args = sys.argv[1:]
    parseArgs(args, parsedAgs)
    printArgs(parsedAgs)

    strs = []
    lastArg = args[len(args)-1:][0]
    if not isInteger(lastArg) and not isFloat(lastArg):
        findSubstrings(lastArg, parsedAgs['strings'], strs)

    if len(strs) > 0:
        print('Found string \'{}\' in following args: {}'.format(lastArg, strs))
    

if (__name__ == '__main__'):
    main()
