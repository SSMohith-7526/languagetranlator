from translate import Translator

translator = Translator(to_lang="hi")
translation = translator.translate("hello")
print(translation)


//pip install translate