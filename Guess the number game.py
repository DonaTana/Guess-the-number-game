import random
print('Добро пожаловать в числовую угадайку')

def is_valid(n):
  if 1 <= n.isdigit() <= 100:
    return True
  else:
    print("Пожалуйста, ведите целое число ")

def main():
  rb = int(input('Выберите правую границу для определния случайного числа '))
  num = random.randint(1, rb)
  count = 0
  flag = False
  while flag == False:
    print('Введите число от 1 до', rb)
    n = input()
    count += 1
    if is_valid(n):
      n = int(n)
      if n > num:
        print('Слишком много, попробуйте еще раз')
      elif n < num:
        print('Слишком мало, попробуйте еще раз')
      elif n == num:
        print(f'Вы угадали, поздравляем! Вы угадали c {count} попытки\nСпасибо, что играли в числовую угадайку')
        flag == True
        break
  print('Хотите сыграть еще раз? Пожалуйста, напишите: да или нет')
  ans()
  
def ans():
  answer = input()
  if answer == 'нет':
    print('До скорых встреч!')
  elif answer != 'да' and answer != 'нет':
    print('Моя твоя не понимать))) Сыграем?')
    ans()
  else:
    print('Отлично! Давайте сыграем еще раз')
    main()
    
main()