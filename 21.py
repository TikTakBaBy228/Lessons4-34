'''
Дан список words. Составьте из него список слов-палиндромов.
Попробуйте это сделать двумя способами: произвольное решение
и решение в одну строку кода.

Дан список my_str со строками, часть из которых являются палиндромами.
Составьте новый список строк-палиндромов.
'''
# words = ['мадам', 'топот', 'test', 'madam', 'word']
# my_str = ['Око за око', 'А роза упала на лапу азора', 'Около Миши молоко']

# words = ['мадам', 'топот', 'test', 'madam', 'word']
# p = []
# for pal in words:
#     if pal == pal[::-1]:
#         p.append(pal)
# p = [pal for pal in p if pal == pal[::-1]]
# print(p)

# my_str = ['Око за око', 'А роза упала на лапу азора', 'Около Миши молоко']
# p = []
# for pal in my_str:
#     pal_r = pal.replace(' ', '').lower()
#     if pal_r == pal_r[::-1]:
#         p.append(pal)
# print(p)