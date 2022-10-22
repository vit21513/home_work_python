
from tictactoe.egtb import Generator
import functools, operator
from tictactoe import Board

def creaty_table_win():

    dimensions = (3, 3)
    total_squares = functools.reduce(operator.mul, dimensions)
    for index in reversed(range(total_squares + 1)):
        Generator(dimensions, 3, index)



def game(board):

    i=0
    print(board)
    print(f'Первый ходит крестик\n')
    while i<=9:
        try:
            a =int(input('Введите куда хотите поставить (х,у)     х=:'))
            b =int(input('Введите куда хотите поставить (х,у)     y=:'))

            if board.is_empty((a,b)):
                board.push((a, b))
                if board.result() == 1:
                    print(f"\nПоздравляю!! Выиграл  крестик")
                    print(board)
                    break
                elif board.result() == 2:
                    print(f"\nПоздравляю!! Выиграл  нолик")
                    print(board)
                    break  
            else:
                print("ячейка занята")
                i-=1
            i+=1
            if i==9:
                print(f"\nНичья")
                print(board)
                break
            print(board)
        except:
            print("Некоректное значение позиции")
            
                

#creaty_table_win()      # для создания  файлов проверки на выигрыш
desk = Board((3, 3), 3)
game(desk)