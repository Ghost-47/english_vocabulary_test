'''
this program is test my english vocabulary.


'''
import english_vocabulary_list
import random

vocabulary_list = english_vocabulary_list.vocabulary_list()
vocabulary_present = english_vocabulary_list.vocabulary_present()
vocabulary_past = english_vocabulary_list.vocabulary_past()
# print(vocabulary_present[0])
# print(vocabulary_list['run'])
# print(vocabulary_list[vocabulary_present[0]])


for i in range(0,5):
    x = random.randint(0,20)
    print(vocabulary_present[x])
    input_vaculary = input('please imput vocabulary\n')
    # print(input_vaculary)
    if vocabulary_list[vocabulary_present[x]] == input_vaculary:
        print('you are right')
    else:
        print('you need more effort')
        print('the right word is:' + vocabulary_list[vocabulary_present[x]])
    i += 1
