words = {
    'Буллинг' : 'травля' ,
    'Вайб' : 'атмосфера' ,
    'Изи' : 'легко' ,
    'Пранк' : 'розыгрыш' ,
    'Тильт' : 'напряжённое состояние' ,
    'Треш' : 'что-то плохое' ,
    'Хейтить' : 'открыто ненавидеть кого-то или что-то' ,
    'Лол' : 'что-то очень смешное' ,
}
word = input("Введите непонятное слово: ").capitalize()
if word in words.keys():
    print('Ваш перевод:')
    print(words.get(word))
else:
    print('такого слова не нашлось')
    
