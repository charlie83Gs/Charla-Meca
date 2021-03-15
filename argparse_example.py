import argparse

parser = argparse.ArgumentParser(description='Multiply two numbers')
parser.add_argument('num1', type=int, help='The first number to multiply')
parser.add_argument('num2',type=int,help='The second number to multiply')

def calculate(num1, num2):
  return num1 * num2

if __name__ == "__main__":
  args = parser.parse_args()
  num1 = args.num1
  num2 = args.num2
  print(f"The result is: {calculate(num1, num2)}")