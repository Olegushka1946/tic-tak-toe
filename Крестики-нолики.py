maps = list(range(1,10))
winner_combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
max_move = 9
counter = 0 
#desk for game
def map_board():
    print ("-----------")
    for i in range (3):
        print ('|', str(maps[0+i*3]) + '|',str( maps[1+i*3]) + '|', str(maps[2+i*3]), '|')
    print ("-----------")

# Ходы игроков
def player_move(move,symbol): 
    ind = maps.index (move)
    maps[ind] = symbol
    
def Wins(maps):
    for i in winner_combination: 
        if maps[i[0]] == maps [i[1]] == maps[i[2]]:
            return maps[i[0]]
        else:
            return False

# игра
def game():
    print ("Игра начинается, если захотите прекратить игру нажми на цифру 0 ")
    First_player = input("Первый игрок, представьтесь:  ")
    Second_player = input("Второй игрок, представьтесь: ")
    map_board()
    global counter
    while counter < max_move: 
        if counter % 2 == 0:
            try: 
                move = int((input(f"{First_player}, Ваш ход ___ ")))
                player_move (move, "X")
                if move == 0:
                    break
            except ValueError:
                print("Поле уже занято или Вы выбрали не цифру от 1 до 9 \n Выберите другое поле или цифру от 1 до 9")
                map_board()
                continue
        else:
            try: 
                move = int((input(f"{Second_player}, Ваш ход ___ ")))
                player_move (move, "O")
                if move == 0:
                    break 
                
            except ValueError:
                print("Поле уже занято или Вы выбрали не цифру от 1 до 9 \n Выберите другое поле или цифру от 1 до 9")
                map_board()
                continue
            
        map_board()
        counter += 1
        check_win = Wins
        if counter > 4: 
            if check_win: 
                if counter % 2 == 0: 
                    print (f"Выиграл {Second_player}")
                    break
                else: 
                    print(f"Выиграл {First_player}")
                    break
            
        if counter == max_move:
            print ("Ничья попробуйте снова")
            break
        

game()

