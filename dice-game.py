import random

COLOR_CODES = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m', 
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}

def colorize(text, color_code):
    return f"{COLOR_CODES[color_code]}{text}{COLOR_CODES['ENDC']}"

def get_chosen_numbers(num_players, player_names):

    chosen_numbers = {}
    chosen_set = set() 

    for name in player_names:

        while True:

            try:

                remaining_numbers = [num for num in range(num_players) if num not in chosen_set]
                chosen_number = int(input(f"{colorize(name, 'OKGREEN')}、好きな数字を選んでください（{remaining_numbers}から選択してください）: "))
                if chosen_number not in remaining_numbers:
                    raise ValueError("無効な数字です。")
                chosen_set.add(chosen_number) 
                chosen_numbers[name] = chosen_number
                break

            except ValueError as ve:
                print(colorize(f"{ve} 正しい数字を選択してください。", 'FAIL'))

    return chosen_numbers


def play_game(num_players, player_names, chosen_numbers):

    target_number = random.randint(0, num_players - 1)
    print(f"{colorize('ランダム数字:', 'WARNING')} {colorize(target_number, 'OKBLUE')}")

    for name, chosen_number in chosen_numbers.items():
        if chosen_number == target_number:
            print(f"{colorize(chosen_number, 'OKBLUE')}を選択した{colorize(name + 'の勝ち', 'OKGREEN')}")
        else:
            print(f"{colorize(chosen_number, 'OKBLUE')}を選択した{colorize(name + 'の負け', 'FAIL')}")

def main():

    while True:

        while True:
            try:
                num_players = int(input(f"{colorize('何人で遊びますか？', 'HEADER')}: "))
                if num_players <= 0:
                    raise ValueError
                break

            except ValueError:
                print(colorize("無効な入力です。正の整数を入力してください。", 'FAIL'))
    
        player_names = []

        for i in range(num_players):

            name = input(f"{colorize(i+1, 'OKBLUE')}人目の名前を入力してください: ")
            player_names.append(name)

        chosen_numbers = get_chosen_numbers(num_players, player_names)

        play_game(num_players, player_names, chosen_numbers)

        while True:

            choice = int(input(f"{colorize('ゲームを続けますか？（はい/いいえ）: ', 'HEADER')}: "))
            
            if choice.lower() == "はい":
                main()
            
            elif choice.lower() == "いいえ":
                print(colorize("ゲームを終了します。", 'WARNING'))
                return
            
            else:
                print(colorize("無効な選択です。はいまたはいいえを入力してください。", 'FAIL'))

if __name__ == "__main__":
    
    print(colorize(f"賭けゲーム スタート！！", 'HEADER'))
    main()
