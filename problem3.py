#!/usr/bin/env python
# coding: utf-8

# In[27]:


# reference : https://medium.com/iecse-hashtag/huffman-coding-compression-basics-in-python-6653cdb4c476
import sys
import queue

class Huffman_Node(object):
    def __init__(self, left = None, right = None, frequency = None, element = None):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.element = element
    def __gt__(self, other):
        return self.frequency > other.frequency

def frequency_count(sentence):
    char_count = {}
    if not isinstance(sentence, str):
        return False
    for char in sentence:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    sorted_freq = [(value, key) for key, value in char_count.items()]
    return sorted_freq


def create_huffman_tree(frequencies):
    if not frequencies:
        return False
    priority_queue = queue.PriorityQueue()
    if len(frequencies) == 1:
        node = Huffman_Node(None, None, 0, None)
        priority_queue.put(node)
    for val in frequencies:
        node = Huffman_Node(frequency = val[0], element = val[1])
        priority_queue.put(node)
    while priority_queue.qsize() > 1:
        huff1 = priority_queue.get() # left
        huff2 = priority_queue.get() # right
        parent = Huffman_Node(huff1, huff2,  huff1.frequency + huff2.frequency)
        priority_queue.put(parent)

    tree = priority_queue.get()
    del priority_queue
    return tree


def encode_string(node, encoding_string = None, codes = None):
    if not node:
        return False
    if codes is None:
        codes = {}
    if encoding_string is None:
        encoding_string = ""
    if node.element:
        codes[node.element] = encoding_string
    encode_string(node.left, encoding_string + "0", codes)
    encode_string(node.right, encoding_string + "1", codes)
    return codes


def encode(sentence, codes =None):
    tree = create_huffman_tree(frequency_count(sentence))
    codes = encode_string(tree, "")
    if not codes:
        return False
    output = "".join([codes[letter] for letter in sentence])
    return output


def decode_string(encoded_string, root = None):
    root = create_huffman_tree(frequency_count(sentence))
    if not root or not encoded_string:
        return False
    node = root
    result = ""
    for char in encoded_string:
        if (node.left is None and node.right is None):
            result += node.element
            node = root;
        if char == '0':
            node = node.left
        else:
            node = node.right
    result += node.element
    return result


sentence = "The bird is the word."
print ("\t\t\t\tTest case 1: \nThe size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: {}\n".format(sentence))

encoded_string = encode(sentence)
print("Encoded string:", encoded_string)
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_string, base=2))))
print("Decoded string:", decode_string(encoded_string))


sentence = ""
print ("\n\n\t\t\t\tTest case 2: \nThe size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: {}\n".format(sentence))

encoded_string = encode(sentence)
print("Encoded string:", encoded_string)
print("Decoded string:", decode_string(encoded_string))
if encoded_string:
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_string, base=2))))


sentence = "A"    
print ("\n\n\t\t\t\tTest case 3: \nThe size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: {}\n".format(sentence))

encoded_string = encode(sentence)
print("Encoded string:", encoded_string)
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_string, base=2))))
print("Decoded string:", decode_string(encoded_string))

sentence = "AAA"
print ("\n\n\t\t\t\tTest case 4: \nThe size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: {}\n".format(sentence))

encoded_string = encode(sentence)
print("Encoded string:", encoded_string)
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_string, base=2))))
print("Decoded string:", decode_string(encoded_string))


# In[ ]:





# In[ ]:




