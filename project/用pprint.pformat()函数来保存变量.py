import pprint
import mycats

cats = [{'name': 'pttt', 'desc': 'cubby'}, {'desc': 'pooka', 'name': 'kmll'}]
fileobj = open('mycats.py', 'w')
fileobj.write('cats =' + pprint.pformat(cats) + '\n')
fileobj.close()

print(mycats.cats[0])