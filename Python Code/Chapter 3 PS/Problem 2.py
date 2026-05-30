# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''

letter = print(letter.replace("<|Name|>","Yogish").replace("<|Date|>","10 th December 2027"))