import random

logic_gates = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "XOR": lambda x, y: x ^ y,
    "NOT": lambda x: not x
}

print("Welcome to the Logic Gate Identification Game!")
print("You will be shown a truth table, and you have to guess the corresponding logic gate.\n")

while True:
    random_gate = random.choice(list(logic_gates.keys()))

    if random_gate == "NOT":
        truth_table = [(x, logic_gates[random_gate](x)) for x in (0, 1)]
        print("Input | Output")
        print("-" * 13)
        for input_val, output_val in truth_table:
            print(f"  {input_val}   |   {output_val}")
    else:
        truth_table = [(x, y, logic_gates[random_gate](x, y)) for x in (0, 1) for y in (0, 1)]
        print("Input1 | Input2 | Output")
        print("-" * 20)
        for input1_val, input2_val, output_val in truth_table:
            print(f"   {input1_val}   |   {input2_val}    |   {output_val}")

    user_input = input("\nGuess the logic gate (AND, OR, XOR, NOT): ").strip().upper()

    if user_input == random_gate:
        print("Congratulations! You guessed correctly.")
    else:
        print(f"Sorry, the correct answer is {random_gate}.")

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

print("Thank you for playing!")
