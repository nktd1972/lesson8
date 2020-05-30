def oops(_index=3, _dict={'a': 1, 'b': 2, 'c': 'mem'}, _key='d'):
    _list = [1, 2, 3]
    print(_list[_index])
    print(_dict[_key])


try:
    _index = int(input(f'Enter index of list: '))
    oops(_index)
except IndexError:
    print("Oops!  That was no valid index.  Try again...")
