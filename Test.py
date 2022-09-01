import  googletrans
import  json
import ast
from googletrans import Translator

translate =Translator()
list =["Vijya","Vinay","Ajay"]
list = str(list)
result = translate.translate(list,dest='hi')
print(result.text)
print(type(result.text))
print(ast.literal_eval(result.text))


