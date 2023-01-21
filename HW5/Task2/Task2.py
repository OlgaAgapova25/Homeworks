# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота ""интеллектом""

# Закомментировано решение основной задачи (game_calculation). Задачи под пунктами a и b объединила, оставлены в действующем решении.

# def game_calculation (total_number):
#     import random
#     first_player = random.randint(1,2)
#     print(f"The player {first_player} is starting the game")
#     if first_player == 1: second_player = 2
#     else: second_player = 1
#     count = 1
#     while total_number != 0:
#         if (count == 1): player = first_player
#         elif (count % 2 == 0): player = second_player
#         elif (count % 2 == 1): player = first_player
#         candies_number_to_take = int(input(f"Player {player}, enter the number of candies you are taking: "))
#         total_number -= candies_number_to_take
#         count += 1
#     return player
def game_calculation_bot (total_number):
    import random
    first_player = random.randint(1,2)
    print(f"The player {first_player} is starting the game")
    if first_player == 1: second_player = 2
    else: second_player = 1
    count = 1
    while total_number != 0:
        if (count == 1): player = first_player
        elif (count % 2 == 0): player = second_player
        elif (count % 2 == 1): player = first_player

        if player == 1:
            candies_number_to_take = int(input(f"Player {player}, enter the number of candies you are taking: "))
        else: #bot
            candies_number_to_take = max (total_number % 29, 1)
            print(f"Bot took {candies_number_to_take} candies")
        total_number -= candies_number_to_take
        count += 1
    return player
def main():
    number_of_candies = 78
    #оставила число 78 для теста. Оно попадает под логику игры с 2021 конфетой (20 для первого хода, далее уравнивать до 29)
    # winner = game_calculation(number_of_candies)
    winner = game_calculation_bot (number_of_candies)
    print(f"Player number {winner}'s won")

if __name__ == "__main__":
    main()