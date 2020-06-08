"""
Flatten Dictionary

This problem was recently asked by Google:

Given a nested dictionary, flatten the dictionary, where nested dictionary
keys can be represented through dot notation.

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

def flatten_dictionary(data):
    flatten_dict = {}
    helper(data, "", flatten_dict)
    return flatten_dict


def helper(data, append_key, flatten_dict):
    for key, value in data.items():
        if isinstance(value, dict):
            helper(value, append_key + key + ".", flatten_dict)
        else:
            flatten_dict[append_key + key] = value


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