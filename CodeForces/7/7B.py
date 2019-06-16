"""
There is little time left before the release of the first national operating system BerlOS. Some of its components are not finished yet — the memory manager is among them. According to the developers' plan, in the first release the memory manager will be very simple and rectilinear. It will support three operations:

alloc n — to allocate n bytes of the memory and return the allocated block's identifier x;
erase x — to erase the block with the identifier x;
defragment — to defragment the free memory, bringing all the blocks as close to the beginning of the memory as possible and preserving their respective order;
The memory model in this case is very simple. It is a sequence of m bytes, numbered for convenience from the first to the m-th.

The first operation alloc n takes as the only parameter the size of the memory block that is to be allocated. While processing this operation, a free block of n successive bytes is being allocated in the memory. If the amount of such blocks is more than one, the block closest to the beginning of the memory (i.e. to the first byte) is prefered. All these bytes are marked as not free, and the memory manager returns a 32-bit integer numerical token that is the identifier of this block. If it is impossible to allocate a free block of this size, the function returns NULL.

The second operation erase x takes as its parameter the identifier of some block. This operation frees the system memory, marking the bytes of this block as free for further use. In the case when this identifier does not point to the previously allocated block, which has not been erased yet, the function returns ILLEGAL_ERASE_ARGUMENT.

The last operation defragment does not have any arguments and simply brings the occupied memory sections closer to the beginning of the memory without changing their respective order.

In the current implementation you are to use successive integers, starting with 1, as identifiers. Each successful alloc operation procession should return following number. Unsuccessful alloc operations do not affect numeration.

You are to write the implementation of the memory manager. You should output the returned value for each alloc command. You should also output ILLEGAL_ERASE_ARGUMENT for all the failed erase commands.

Input
The first line of the input data contains two positive integers t and m (1 ≤ t ≤ 100;1 ≤ m ≤ 100), where t — the amount of operations given to the memory manager for processing, and m — the available memory size in bytes. Then there follow t lines where the operations themselves are given. The first operation is alloc n (1 ≤ n ≤ 100), where n is an integer. The second one is erase x, where x is an arbitrary 32-bit integer numerical token. The third operation is defragment.

Output
Output the sequence of lines. Each line should contain either the result of alloc operation procession , or ILLEGAL_ERASE_ARGUMENT as a result of failed erase operation procession. Output lines should go in the same order in which the operations are processed. Successful procession of alloc operation should return integers, starting with 1, as the identifiers of the allocated blocks.
"""

def alloc(identifier, size):
    for key, i in enumerate(memory):
        if (not i['identifier']) and (i['size'] >= size):
            if i['size'] > size: # still zeros?
                memory.insert(key, {'identifier': identifier, 'size': size})
                i['size'] -= size
            else:
                i['identifier'] = identifier
            return True

    return False

def erase(identifier, m):
    erase_counter = 0

    for key, j in enumerate(memory):
        if j['identifier'] == identifier:
            j['identifier'] = 0
            erase_counter = j['size']

            if (key > 0) and (memory[key - 1]['identifier'] == 0):
                memory[key - 1]['size'] += j['size']
                erase_counter = memory[key - 1]['size']
                memory.pop(key)

            if (key < len(memory) - 1) and (memory[key + 1]['identifier'] == 0):
                memory[key + 1]['size'] += j['size']
                erase_counter = memory[key + 1]['size']
                memory.pop(key)

            break

    return erase_counter

def defragment(memory):
    zero_counter = 0
    for key, k in enumerate(memory):
        if not k['identifier']:#zeros
            memory.pop(key)
            zero_counter += k['size']

    if zero_counter:
        memory.append({'identifier': 0, 'size': zero_counter})

    return memory

t, m = map(int, input().split())
memory = [{'identifier': 0, 'size': m}]

identifier_count = 1
identifiers = set()
empty_elm_counter = m

for i in range(t):
    command = input().split()
    op = command[0]
    if len(command) > 1:
        arg = int(command[1])

    if op == 'alloc':
        if arg <= empty_elm_counter:
            test1 = alloc(identifier_count, arg)
            if test1:
                print(identifier_count)
                identifiers.add(identifier_count)
                identifier_count += 1
            else:
                print('NULL')
        else:
            print('NULL')

    elif op == 'erase':
        if arg in identifiers:
            empty_elm_counter = max(empty_elm_counter, erase(arg, m))
            identifiers.remove(arg)
        else:
            print('ILLEGAL_ERASE_ARGUMENT')

    elif op == 'defragment':
        memory = list(defragment(memory))
