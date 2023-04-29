import random

user_wins_print = "Felicidades le ganaste a la máquina"
computer_wins_print = "Perdiste"


def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input("Elija piedra, papel o tijera = > ").lower()
  if not user_option in options:
    print("Opción no válida")
    return None, None

  computer_option = random.choice(options)
  print("User option =>", user_option)
  print("Computer option = >", computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
  if (user_option == computer_option):
    print("Empate")
  elif (user_option == "piedra" and computer_option == "tijera") or (
      user_option == "tijera"
      and computer_option == "papel") or (user_option == "papel"
                                          and computer_option == "piedra"):
    user_wins += 1
    print("Gana usuario")

  else:
    computer_wins += 1
    print("Gana máquina")
  return user_wins, computer_wins


def check_winner(user_wins, computer_wins):

  if user_wins == 2:
    print(user_wins_print)
    exit()

  if computer_wins == 2:
    print(computer_wins_print)
    exit()


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while True:

    print('*' * 10)
    print('Round', rounds)
    print('*' * 10)
    rounds += 1
    print("Computador = >", computer_wins)
    print("User = >", user_wins)

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    check_winner(user_wins, computer_wins)


run_game()