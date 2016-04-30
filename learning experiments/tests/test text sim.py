# def punc_strip(text_string):
#     word_list =text_string.lower().split()
#     punc_mark=""".!?,'";:[]{}$%()#@"""
#     for index in range(len(word_list)):
#         for num in range(len(word_list[index])):
#             if word_list[index][num] in punc_mark:
#                 word_list[index][num] = word_list[index][:num]+word_list[index][num+1:]

test_text_1='The dog jumped over the moon'
test_text_2='THE dog jUmped over the moon, over the moon, over the moon.'
dict_1=[word for word in test_text_1.lower().split() if word.isalpha()==True]
dict_2=[word for word in test_text_2.lower().split() if word.isalpha()==True]
similar_word_count=0
print (dict_1,dict_2)
for word in dict_1:
    if word in dict_2:
        similar_word_count+=1
sim_score=similar_word_count/(len(dict_1)+len(dict_2)-similar_word_count)
print (sim_score)
