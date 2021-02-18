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
