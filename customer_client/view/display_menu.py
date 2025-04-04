from .utility import make_table, get_length_from_subdic, get_key_value_max_length


class DisplayMenu:
    line = "-" * 90

    def display_title(self, title):
        print(self.line)
        print(f"\t{title}")
        print(self.line)

    def display_info(self, info):
        print(f"\t{info}")
        print(self.line)

    def display_title_and_infos(self, title, info):
        self.display_title(title)
        self.display_info(info)

    def display_options(self, options):
        print("")
        count = 1
        for key in options:
            print(f"\t{key}")
            count += 1
        print(self.line)
        while True:
            choice = input(f"\tbitte Menüpunkt auswählen (1-{count-1} eingeben): ")
            if choice.isdigit() is True:
                test = False
                for key in options:
                    if choice in key:
                        print("")
                        return options[key]

                if test is False:
                    print("\tFehlerhafte eingabe")
            else:
                print("\tFehlerhafte eingabe")

    def display_form(self, form_names: dict, to_fill):
        self.form_names = form_names
        self.to_fill = to_fill

        for key, value in form_names.items():
            while True:
                try:
                    user_input = input(f"\t{value} eingeben: ")
                    setattr(self.to_fill, key, user_input)
                    break
                except Exception as e:
                    print(f"\tFehlerhafte eingabe: {e}")
        print(self.line)
        return "form_filled"

    def display_filled_form(self, form_names_input=None):
        if form_names_input is None:
            form_names_input = self.form_names

        length_keys, length_values = get_key_value_max_length(form_names_input)

        print(" ")
        print("\tBitte Eingaben überprüfen:")
        print(self.line)
        for key, value in form_names_input.items():
            print(f"\t{value.ljust(length_values)} : {getattr(self.to_fill, key)}")

        print(self.line)

    def display_table(self, input: dict, column_names: dict):
        transform_input = make_table(input, column_names)

        for transform in transform_input:
            print(f"\t{transform}")

        print("")
        print(self.line)

    def display_dict(self, input: dict):
        for v in input.values():
            print(f"\t{v}")
        print(self.line)

    def display_dic(self, input: dict):
        length_key, length_values = get_key_value_max_length(input)

        for k, v in input.items():
            print(f"\t{k.ljust(length_key)} : {v.rjust(length_values)}")
        print(" ")

    def display_dic_in_dic(self, input: dict):

        length_keys, length_values = get_length_from_subdic(input)

        line = f"\t{"-" * (length_keys + length_values + 1)}"

        for key, dic in input.items():

            print(f"\n\t{key}")
            print(line)
            for k, v in dic.items():
                print(f"\t{k.ljust(length_keys)}:{v.rjust(length_values)}")
        print(self.line)
        print("")
