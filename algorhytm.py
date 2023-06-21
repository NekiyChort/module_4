def palindrom(string):
    list_from_beg = []
    list_from_end = []
    for symbol in string:
        list_from_beg.append(symbol)
    #print(list_from_beg)
    list_from_end = list_from_beg[::-1]
    #print(list_from_end)

    true_detector = 0
    for symbol in string:
        index = 0
        if list_from_beg[index] == list_from_end[index]:
            true_detector += 1
            index += 1
        else:
            None
    #print(true_detector)

    if true_detector == len(list_from_beg):
        print(True)
    else:
        print(False)


palindrom('saippuakivikauppias')  #saippuakivikauppias с финского продавец мыльного камня; торговец стеатитом))