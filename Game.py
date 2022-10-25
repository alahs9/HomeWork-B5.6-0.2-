table = list(range (1, 10))

def draw_table(table):
   for i in range(3):
      print("[", table[0+i*3],"][", table[1+i*3],"][", table[2+i*3],']')

def your_input(token):
   real = False
   while not real:
      ppl_answer = input(" Введите цифру куда хотите поставить " + token + "?")
      try:
         ppl_answer = int(ppl_answer)
      except:
         print("Некорректный ввод. Введите число?")
         continue
      if ppl_answer >=1 and ppl_answer <=9:
         if(str(table[ppl_answer-1]) not in "XØ"):
            table[ppl_answer-1] = token
            real= True
         else:
            print('Клетка занята')

      else:
         print('Введите число от 1-9')

def test_win_game(table):
   win_game = ((0 , 1 , 2), (3 , 4 , 5), (6 , 7 , 8), (0 , 3 , 6) , (1 , 4 , 7), (2 , 5 , 8), (0 , 4 , 8), (2 , 4 , 6))
   for every in win_game:
      if table[every[0]]==table[every[1]]==table[every[2]]:
         return table[every[0]]
   return False

def main(table):
   counter = 0
   win = False
   while not win:
      draw_table(table)
      if counter % 2 == 0:
         your_input('X')
      else:
         your_input("Ø")
      counter +=1

      if counter > 4:
         game_end = test_win_game(table)
         if game_end:
            print('*'*25, game_end, 'победил!')
            win = True
            break
      if counter == 9:
            print('Ничья')
            break
   draw_table(table)
main(table)

