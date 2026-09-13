class Solution(object):

  def getHappyString(self, n, k):
    total_strings = 3 * (1 << (n - 1))
    if k > total_strings:
      return ''

    # Determine first character
    k -= 1  # Convert to 0-indexed
    group_size = 1 << (n - 1)
    first_char_idx = k // group_size
    res = [chr(ord('a') + first_char_idx)]

    k %= group_size

    # Build the rest of the string
    for i in range(1, n):
      group_size >>= 1
      next_char_idx = k // group_size
      k %= group_size

      # Available characters excluding the last inserted character
      choices = [c for c in ['a', 'b', 'c'] if c != res[-1]]
      res.append(choices[next_char_idx])

    return ''.join(res)