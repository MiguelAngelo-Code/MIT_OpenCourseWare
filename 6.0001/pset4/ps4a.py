# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # List of permutations
    permutations = []

    # Base case
    if len(sequence) == 1:
        return sequence

    # Recursive case 
    else:
        # Store first chare to insert acros sub-sequnece of permutations
        first_char = sequence[0]
        new_seq = (get_permutations(sequence[1:]))

        # Loops over list of sub-sequences 
        for sub_seq in new_seq:
            # Loops over sub-sequence
            for i in range(len(sub_seq)+1):

                # Create temp list of string & insert first_char into evry index
                temp = list(sub_seq).copy()
                temp.insert(i, first_char)
                new_perm = "".join(temp)

                # Append new permuation to list of permutations
                permutations.append(new_perm)

        return permutations
    
    
    

    '''
    seq_lst = list(sequence)

    permutations = []

    if len(seq_lst) > 1:
        for lst in get_permutations(seq_lst.pop(0)):
            for i in range(len(lst)): 
                permutation = lst.insert(i, seq_lst[0])
                permutations += "".join(permutation)

    else:
        return [sequence]

    return permutations
    '''
if __name__ == '__main__':
    print('----- Test 1 -----')
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    print('----- Test 2 -----')
    example_input = 'cat'
    print('Input:', example_input)
    print('Expected Output:', ['cat', 'cta', 'tca', 'tac', 'act', 'atc'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

