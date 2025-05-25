def make_dictionary(datas, names):

    search_result = {}
    i = 0
    for data in datas:
        row_data = {}
        for j in range(len(data)):
            row_data[names[j]] = data[j]

        search_result[f"row_result{i}"] = row_data
        i += 1

    return search_result


def make_dictionary_one_result(datas, names):
    row_data = {}
    for j in range(len(datas)):
        row_data[names[j]] = datas[j]

    return row_data
