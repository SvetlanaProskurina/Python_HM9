# Создайте программу для игры в ""Крестики-нолики"".
# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
import emoji 

print('Поиграем в крестики нолики?')

field_for_game = list(range(1,10))

# рисуем поле для игры
def game_field(field_for_game):
    print('-'*13)
    for i in range(3):
        print('|', field_for_game[0+i*3],'|', field_for_game[1+i*3], '|', field_for_game[2+i*3], '|')
        print('-'*13)
        
# очередность хода и проверка чтобы не нажали буквы или еще что
def motion(x_o):
    flag = False
    while not flag:
        player_index = input('Ваш ход, выберите ячейку, введите ее номер для  ' + x_o + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Введите цифру от 1 до 9')
            continue
# проверка на занятость клетки в которую хотят нарисовать ХО и на введенное число, которое должно быть от 0 до 9
        if player_index >= 1 and player_index < 10:
            if emoji.emoji_count(str(field_for_game[player_index-1])) != 1: #not in 'XO' :
                field_for_game[player_index-1] = x_o # Х или О
                flag = True
            else:
                print('эта клетка занята')
        else:
            print('Попробуйте еще раз')

def check(field_for_game):
    check_win = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in check_win:
        if field_for_game[i[0]] == field_for_game[i[1]] == field_for_game[i[2]]:
            return field_for_game[i[0]]
    return False

def game(field_for_game):
    counter =0
    winer = False
    while not winer:
        game_field(field_for_game)
        if counter % 2 == 0:
            motion(emoji.emojize(":crossed_swords:"))
        else:
            motion(emoji.emojize(":red_heart:"))
        counter +=1
        if counter > 4:
            win_check = check(field_for_game)
            if win_check:
                print(win_check,'Выиграл игру',emoji.emojize(":sports_medal:"))
                winer = True
                break
            if counter == 9:
                print('Ничья!',emoji.emojize(":handshake:"))
                break
game(field_for_game)