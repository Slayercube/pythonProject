#dictonery = a changable, unordered collectoion of unique
# key:value pairs fast because they use hashing , allow us to acess a value quickly

capitals = {'usa' : 'dc',
            'india' : 'delhi',
            "russia" : 'moscow'
            }

capitals.update({'german' : 'berlin'})
capitals.update({'usa' : 'new-york'})
# capitals.pop('russia')
# capitals.clear()

# print(capitals.get('usa'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key , value in capitals.items():
    print(key , value)