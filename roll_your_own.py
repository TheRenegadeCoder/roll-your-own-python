def power(base, exp, mod=None):
  '''
  Replicates the built-in power function.
  
  Source: https://therenegadecoder.com/code/roll-your-own-power-function-in-python/
  '''
  if mod == 0:
    raise ValueError("power() 3rd argument cannot be 0")
  result = 1
  for i in range(abs(exp)):
    result *= base
  if exp < 0:
    result = 1 / result
  if mod:
    result %= mod
  return result

def upper(string):
  '''
  Replicates the upper method of strings.
  
  Source: https://therenegadecoder.com/code/roll-your-own-uppercase-function-in-python/
  '''
  characters = list(string)
  for index, character in enumerate(characters):
    ordinal = ord(character) - 32
    if 65 <= ordinal <= 90:
      characters[index] = chr(ordinal)
  return ''.join(characters)
