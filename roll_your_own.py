def minimum(*args, **kwargs):
  '''
  Replicates the built-in min function
  
  Source: https://therenegadecoder.com/code/roll-your-own-minimum-function-in-python/
  '''
  if len(args) == 1: # must be an iterable
    args = args[0]
    iterator = iter(args)  # will crash if not iterable
    if not args:
      if "default" in kwargs:
        return kwargs.get("default")
      else:
        raise ValueError("min() arg is an empty sequence")
  key = kwargs.get("key", lambda x: x)
  iterator = iter(args)
  smallest = next(iterator)
  while True:
    try:
      test = next(iterator)
      if key(test) < key(smallest):
        smallest = test
    except StopIteration:
      break
  return smallest  

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
