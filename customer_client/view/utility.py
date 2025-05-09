def get_key_value_max_length(input: dict):
    max_length_keys = 0
    max_length_values = 0

    for k, v in input.items():
        if len(k) > max_length_keys:
            max_length_keys = len(k)

        if len(v) > max_length_values:
            max_length_values = len(v)

    return max_length_keys, max_length_values


def make_table(input: dict, column_names: dict):

    print("\n\n")
    print("input:", input)
    print("")
    print("column_names", column_names)
    print("\n\n")

    for dic_in in input.values():

        for k, v in dic_in.items():

            # if isinstance(v, decimal.Decimal):
              #  dic_in[k] = str(v.quantize(decimal.Decimal(1.00)))
              #  dic_in[k] = f"{dic_in} EUR"

            if isinstance(v, int):
                dic_in[k] = str(v)
            elif isinstance(v, float):
                dic_in[k] = str(round(v, 2))

    column_lengths = []

    for v in column_names.values():

        vol = len(v)
        column_lengths.append(len(v))

    for dic_in in input.values():

        for i, v in enumerate(dic_in.values()):

            vol = len(v)

            if vol > column_lengths[i]:
                column_lengths[i] = vol

    tabelle = [""]

    for i, v in enumerate(column_names.values()):

        tabelle[0] = f"{tabelle[0]} {v.ljust(column_lengths[i])} |"
        if i == 0:
            tabelle.append("")
        tabelle[1] = f"{tabelle[1]}{"-"*(column_lengths[i]+3)}"

    
    for i, dic_in in enumerate(input.values()):

        tabelle.append("")
        for j, k in enumerate(column_names.keys()):

            tabelle[i+2] = f"{tabelle[i+2]} {dic_in[k].ljust(column_lengths[j])} |" 

    return tabelle


def get_length_from_subdic(input: dict):

    length_keys = 0
    length_values = 0
    for dic in input.values():
        for k, v in dic.items():
            if len(k) > length_keys:
                length_keys = len(k)

            if len(v) > length_values:
                length_values = len(v)

    return length_keys, length_values


if __name__ == "__main__":
    result = {'row_result0': {'isin': 'DE0005140008',
                            'company_name': 'Deutsche Bank',
                            'amount': 68,
                            'price_per_stock': 21.270000457763672,
                            'actual_price': 21.270000457763672,
                            'performance': 1.0},
              'row_result1': {'isin': 'DE0005190003',
                              'company_name': 'BMW St',
                              'amount': 79,
                              'price_per_stock': 86.44000244140625,
                              'actual_price': 86.44000244140625,
                              'performance': 1.0},
              'row_result2': {'isin': 'DE000DTR0CK8',
                              'company_name': 'Daimler Truck',
                              'amount': 34,
                              'price_per_stock': 41.91999816894531,
                              'actual_price': 41.91999816894531,
                              'performance': 1.0},
              'row_result3': {'isin': 'DE000ZAL1111',
                              'company_name': 'Zalando',
                              'amount': 54,
                              'price_per_stock': 31.229999542236328,
                              'actual_price': 31.229999542236328,
                              'performance': 1.0}}

    tabelle = make_table(result)

    for tab in tabelle:
        print(tab)
