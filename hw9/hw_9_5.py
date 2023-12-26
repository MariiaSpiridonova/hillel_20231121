source_string = 'Python is good language to learn and in same time we like to tell that it is cool expereance for us'
reworked_string = source_string.lower().replace(' ', '')

dict_from_string = {i: reworked_string.count(i) for i in reworked_string}
print(dict_from_string)
