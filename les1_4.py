# def strcounter(string):
#     for symbol in set(string):
#         counter = 0
#         for sub_symbol in string:
#             if symbol == sub_symbol: 
#                 counter += 1
#         print(symbol, counter)


# strcounter('aaabcdd')


def strcounter(string):
    sym_counter = {}
    for symbol in string:
        sym_counter[symbol] = sym_counter.get(symbol, 0) + 1
    print(sym_counter)

strcounter('aaabcdd')