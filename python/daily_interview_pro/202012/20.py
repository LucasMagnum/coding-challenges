"""
Flatten Dictionary

This problem was recently asked by Google:

Given a nested dictionary, flatten the dictionary, where nested dictionary keys can be represented through dot notation.

Example:
Input: {
  'a': 1,
  'b': {
    'c': 2,
    'd': {
      'e': 3
    }
  }
}
Output: {
  'a': 1,
  'b.c': 2,
  'b.d.e': 3
}
You can assume there will be no arrays, and all keys will be strings.
"""

def flatten_dictionary(d):
    result = {}

    def flatten(dikt, append_key):
        for k, v in dikt.items():
            if isinstance(v, dict):
                flatten(v, append_key + k + ".")
            else:
                result[append_key + k] = v

    flatten(d, "")
    return result


if __name__ == "__main__":
    d = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3
            }
        }
    }
    print(flatten_dictionary(d))
    # {'a': 1, 'b.c': 2, 'b.d.e': 3}