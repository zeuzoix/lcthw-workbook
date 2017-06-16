# Reference: https://developers.google.com/edu/python/dict-files

## Can build up a dict by starting with the empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value-for-the-key

dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print dict          ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print dict['a']     ## alpha
dict['a'] = 6
print dict['a']     ## 6

key = raw_input('Enter key:')
if key in dict:
        print key, "is in dict"
else:
        print key, "is not in dict value is ", dict.get(key)


## By default, iterating over a dict iterates over its keys
## The keys are in random order
for key in dict:
        print key
# a
# o
# g

for key in dict.keys():
        print key
# a
# o
# g

print dict.keys()
#['a', 'o', 'g']

print dict.values()
#[6, 'omega', 'gamma']

## Common case loop over the keys in sorted order
## accessing each key/value

for key in sorted(dict.keys()):
        print key, dict[key]
#a 6
#g gamma
#o omega


## .items is the dict expressed as (key, value) tuples
print dict.items()
#[('a', 6), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping
## over the .items() tuples list, accessing one (key, value)
## pair on each iteration
for k, v in dict.items(): print k, '>', v
#a > 6
#o > omega
#g > gamma
