#Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов. Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду разработки.
c = int(input())
print('   _~_    '*c)
print('  (o o)   '*c)
print(' /  V  \  '*c)
print('/(  _  )\ '*c)
print('  ^^ ^^   '*c)
