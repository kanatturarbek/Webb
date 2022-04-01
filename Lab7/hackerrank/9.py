def split_and_join(line):
    list=line.split()
    res="-"
    res=res.join(list)
    return res
if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result