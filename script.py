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
    if not args:
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
    if args['integers']:
        print('Integers: {}'.format(args['integers']))
    if args['floats']:
        print('Floats: {}'.format(args['floats']))
    if args['strings']:
        print('Strings: {}'.format(args['strings']))

def findSubstrings(strToFind, arrOfStrings):
    return [s for s in arrOfStrings if strToFind in s and strToFind != s]

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
    lastArg = args[-1]
    if not isInteger(lastArg) and not isFloat(lastArg):
        strs = findSubstrings(lastArg, parsedAgs['strings'])

    if strs:
        print("Found string '{}' in following args: {}".format(lastArg, strs))
    

if (__name__ == '__main__'):
    main()
