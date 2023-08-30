'''


'''
import csv

verb_present = []
verb_past = []
verb_list = {}

with open('english_vocabulary_list.csv','r') as file:
    csv_reader = csv.reader(file)
    data = dict(csv_reader)#这里其实已经变成了字典，后面没必要再重新合成了，但是为了功能还是重新做了一遍。
# print(data.values)

def vocabulary_present():
    verb_present = list(data.keys())
    # print(verb_present)
    return verb_present

def vocabulary_past():
    verb_past = list(data.values())
    # print(verb_past)
    return verb_past

def vocabulary_list():
    presetent_list = vocabulary_present()
    past_list = vocabulary_past()
    vocabulary_list = dict(zip(presetent_list,past_list))
    # print(vocabulary_list)
    return vocabulary_list


# vocabulary_present()
# vocabulary_past()
# a = vocabulary_list()
# print(a['meet'])