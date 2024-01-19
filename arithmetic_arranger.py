def validate_input(expressions):
  if len(expressions) > 5:
    raise ValueError('Error: Too many problems.')
  for expression in expressions:
    items = expression.split(' ')
    if len(items) != 3 or items[1] not in ['+', '-']:
      raise ValueError("Error: Operator must be '+' or '-'.")
    try:
      int(items[0])
      int(items[2])
    except ValueError:
      raise ValueError("Error: Numbers must only contain digits.")
    if len(items[0]) > 4 or len(items[2]) > 4:
      raise ValueError("Error: Numbers cannot be more than four digits.")

# To populate the result list by adding operands
def calculate(operand1, operand2, operators):


  op1 = [int(x) for x in operand1]
  op2 = [int(x) for x in operand2]

  operand3 = []
  for y in range(len(operators)):
    if operators[y] == '+':
      operand3.append(op1[y] + op2[y])
    elif operators[y] == '-':
      operand3.append(op1[y] - op2[y])
  operand3 = [str(x) for x in operand3]
  return operand3


# To add space in front of items
def add_space(operand1, operand2, result, dashes):
  space = 0
  for x in range(len(operand1)):
    for y in range(len(operand2)):
      if x == y:
        if len(operand1[x]) > len(operand2[y]):
          space = len(operand1[x]) + 1
          while len(operand1[x]) <= space:
            operand1[x] = " " + operand1[x]
          while len(operand2[y]) < space:
            operand2[y] = " " + operand2[y]
          try:
            while len(result[x]) <= space:
              result[x] = " " + result[x]
          except IndexError:
            pass
          # for z in range(len(dashes)):
          if len(dashes[y]) <= space:
            dashes[y] = '-' * (space+1)
        else:
          space = len(operand2[y]) + 1
          while len(operand1[x]) <= space:
            operand1[x] = " " + operand1[x]
          while len(operand2[y]) < space:
            operand2[y] = " " + operand2[y]
          try:
            while len(result[x]) <= space:
              result[x] = " " + result[x]
          except IndexError:
            pass
          # for z in range(len(dashes)):
          if len(dashes[y]) <= space:
            dashes[y] = '-' * (space+1)

  return operand1, operand2, result, dashes


def arithmetic_arranger(expressions, flag=False):

  try:
    validate_input(expressions)
  except ValueError as ve:
    return str(ve)

  # Seperating operands and operators
  operators = []
  operand1 = []
  operand2 = []
  dashes = []
  result = []
  for expression in expressions:
    items = expression.split(' ')
    operand1.append(items[0])
    operators.append(items[1])
    operand2.append(items[2])
  for x in operand1:
    dashes.append(x)

  if flag:
    result = calculate(operand1, operand2, operators)

  # operators = add_space(operators)
  operand1, operand2, result, dashes = add_space(operand1, operand2, result, dashes)

  # Adding operator and operand 2 together
  operand2 = [x + y for x, y in zip(operators, operand2)]

  operand1 = '    '.join(operand1)
  operand2 = '    '.join(operand2)
  result = '    '.join(result)
  dashes = '    '.join(dashes)

  final_output = operand1 + '\n' + operand2 + '\n' + dashes
  if flag:
    final_output += '\n' + result

  return final_output