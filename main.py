# import random module
import random

# constant vairables
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# dictionary for count symbols
symbol_count = {
    'A': 2,
    'B': 4,
    'C':6,
    'D':8
}

# dictionary for grade values
symbol_value = {
    'A': 5,
    'B': 4,
    'C':3,
    'D':2
}

# check user win function
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
            winning_lines.append(line +1)

    return winnings, winning_lines

# spin machine function in rows and columns
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count, in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

# print multidimensional value function
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

# deposit amount check function
def deposit():
    while True:
        amount = input("How much amount you want to deposist? $")
        if amount.lstrip("-").isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
        
    return amount

# get line number function
def get_number_of_lines():
    while True:
        line = input("Enter a line number? (1-" + str(MAX_LINES) + ") ")
        if line.lstrip("-").isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
                print("line must between 1 and 3.")
        else:
            print("Please enter a number.")
        
    return line

# get bet amount function
def get_bet():
    while True:
        bet_amount = input("How much amount you want to bet on each line? $")
        if bet_amount.lstrip("-").isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Bet Amount must between #{MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
        
    return bet_amount

# spin the machine function
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet_amount = get_bet()
        total_bet = bet_amount * lines
        if total_bet > balance:
            print(f"You have not enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"Your betting amount ${bet_amount} on {lines} lines.Total betting amount is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet_amount, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet

# main function 
def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("press enter to play or (q to quit).").lower()
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

# call main function
main()
