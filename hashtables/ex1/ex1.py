#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    # ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    ht = HashTable(length)
    count = 0

    for i in weights:
        print("current [i] [count] [retrieve]: ", i, count, hash_table_retrieve(ht, i))

        if (hash_table_retrieve(ht, i) != None):
            print("indices addition [i + i] and [limit]: ", i + i, limit)
            
            if (i + i == limit):
                if (hash_table_retrieve(ht, i) > count):
                    return (hash_table_retrieve(ht, i), count)
                return (count,hash_table_retrieve(ht, i), count)

        hash_table_insert(ht, i, count) 

        if (hash_table_retrieve(ht, limit - i)):
            print("[retrieve] and [count]", hash_table_retrieve(ht, limit - i), count)  
            
            if (hash_table_retrieve(ht, limit - i) > count):
                print("[retrieve] > [count]", hash_table_retrieve(ht, limit - i), count)
                return (hash_table_retrieve(ht, limit - i), count)

            print("[retrieve] <= [count]", hash_table_retrieve(ht, limit - i), count)
            return (count, hash_table_retrieve(ht, limit - i), count)

        print("COUNT", count)
        count += 1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
