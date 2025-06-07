import getpass

# from .view_utilites import make_table, get_length_from_subdic, get_key_value_max_length
###################
# class Display:
#   1. display_title()
#   2. display_info()
#   3. display_titlle_and_info()
#   4. display_options()
#   5. display_form()
#   6. display_fiiled_form()
#   7. display_table()
#   8. display_dict()
#   9. 
#  (class utilities function):
#   10. _get_key_value_max_length()
#   11. _make_table()
#   12. _get_length_from_subdic()
#   


class Display:
    line = "-" * 90
    line = f"\t{line}"

    # 1. display_title()
    def display_title(self, title):
        print(self.line)
        print(f"\t{title}")
        print(self.line)

    # 2. display_info()
    def display_info(self, info):
        print(f"\t{info}")
        print(self.line)

    # 3. display_titlle_and_info()
    def display_title_and_infos(self, title, info):
        self.display_title(title)
        self.display_info(info)

    # 4. display_options()
    def display_options(self, options: dict):
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
                    print("\tFehlerhafte Eingabe")
            else:
                print("\tFehlerhafte Eingabe")

    def display_form(self, form_names: dict, to_fill):
        self.form_names = form_names
        self.to_fill = to_fill

        for key, value in form_names.items():
            while True:
                try:
                    if value == "Passwort_Login":
                        user_input = getpass.getpass("\tPasswort eingeben: ").strip()
                    elif value == "Passwort":
                        user_input = getpass.getpass("\tPasswort min. 12 Zeichen und \n"
                                                     "mit A-Z, a-z, 0-9 und Sonderzeichen\n"
                                                     "eingeben: ").strip()
                    else:
                        user_input = input(f"\t{value} eingeben: ").strip()

                    if user_input == "Abbrechen" or user_input == "abbrechen":
                        return False

                    setattr(self.to_fill, key, user_input)
                    break
                except Exception as e:
                    if e == "unter 18":
                        print("\tEs tut uns leid, Mindestalter ist 18 Jahre.")
                        return False
                    else:
                        print(f"\tFehlerhafte Eingabe: {e}")
                        print("\tOder 'Abbrechen' eingeben, um abzubrechen")
        print(self.line)
        return True

    def display_filled_form(self, form_names_input=None):
        if form_names_input is None:
            form_names_input = self.form_names

        length_keys, length_values = self._get_key_value_max_length(form_names_input)

        print(" ")
        print("\tBitte Eingaben überprüfen:")
        print(self.line)
        for key, value in form_names_input.items():
            if key == "password":
                length = len(getattr(self.to_fill, key))
                stars = "*"*length
                print(f"\t{value.ljust(length_values)} : {stars}")
            else:
                print(f"\t{value.ljust(length_values)} : {getattr(self.to_fill, key)}")

        print(self.line)

    def display_table(self, input: dict, column_names: dict):
        transform_input = self._make_table(input, column_names)

        for transform in transform_input:
            print(f"\t{transform}")

        print("")
        print(self.line)

    def display_dict(self, input: dict):
        for v in input.values():
            print(f"\t{v}")
        print(self.line)

    def display_dic(self, input: dict):
        length_key, length_values = self._get_key_value_max_length(input)

        for k, v in input.items():
            print(f"\t{k.ljust(length_key)} : {v.rjust(length_values)}")
        print(" ")

    def display_dic_in_dic(self, input: dict):

        length_keys, length_values = self._get_length_from_subdic(input)

        line = f"\t{"-" * (length_keys + length_values + 1)}"

        for key, dic in input.items():

            print(f"\n\t{key}")
            print(line)
            for k, v in dic.items():
                print(f"\t{k.ljust(length_keys)}:{v.rjust(length_values)}")
        print(self.line)
        print("")

    def _get_key_value_max_length(self, input: dict):
        max_length_keys = 0
        max_length_values = 0

        for k, v in input.items():
            if len(k) > max_length_keys:
                max_length_keys = len(k)

            if len(v) > max_length_values:
                max_length_values = len(v)

        return max_length_keys, max_length_values

    def _make_table(self, input: dict, column_names: dict):

        for dic_in in input.values():

            for k, v in dic_in.items():

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

        tabelle = ["| "]

        for i, v in enumerate(column_names.values()):

            tabelle[0] = f"{tabelle[0]} {v.ljust(column_lengths[i])} |"
            if i == 0:
                tabelle.append("|-")
            tabelle[1] = f"{tabelle[1]}{"-"*(column_lengths[i]+3)}"

        for i, dic_in in enumerate(input.values()):

            tabelle.append("| ")
            for j, k in enumerate(column_names.keys()):

                tabelle[i+2] = f"{tabelle[i+2]} {dic_in[k].ljust(column_lengths[j])} |"

        return tabelle

    def _get_length_from_subdic(self, input: dict):

        length_keys = 0
        length_values = 0
        for dic in input.values():
            for k, v in dic.items():
                if len(k) > length_keys:
                    length_keys = len(k)

                if len(v) > length_values:
                    length_values = len(v)

        return length_keys, length_values
