import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}


def deposit():
    while True:
        amount = input('Please enter your deposit (Must be greater than 0 and a whole number ): $')
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print('Please enter a valid number')

    return amount


def get_number_of_lines():
    while True:
        lines = input(f'Number of lines to bet on (1 - {MAX_LINES})? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Please enter valid number of lines')
        else:
            print('Please enter a valid number')

    return lines


def get_bet_amount():
    while True:
        amount = input(f'Please enter your bet on each line ({MIN_BET} - {MAX_BET}): $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print('Please enter a valid bet')
        else:
            print('Please enter a valid number')

    return amount


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            symbol = random.choice(current_symbols)
            column.append(symbol)
            current_symbols.remove(symbol)

        columns.append(column)
            
    return columns


def print_slot_machine(columns):
    for i in range(len(columns[0])):
        row = []
        for j, column in enumerate(columns):
            print(column[i], end='')
            if j < len(columns) - 1:
                print(' | ', end='')
        print()


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) 
    
    return winnings, winning_lines


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is ${balance}.')
        else:
            break
    print(f'You are betting ${bet} on {lines} lines. Total bet is ${bet * lines}.')
    spin_slot_machine = input('Do you want to spin the slot machine ? (Y, N): ').upper()
    if spin_slot_machine == 'Y':
        columns  = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(columns)
        winnings, winning_lines = check_winnings(columns, lines, bet, symbol_count)
        if winnings > 0:
            print(f'You won ${winnings}.')
            print(f'You won on line', *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answer = input('Please enter to spin. (q to quit). ')
        if answer == 'q' or answer == 'Q':
            print('Quiting the game.')
            break
        if balance <= 0:
            print(f"You don't have enough to play. Your balance is ${balance}.")
            break
        balance += spin(balance)

if __name__ == '__main__':
    main()
