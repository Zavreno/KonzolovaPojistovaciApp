class ValidateInput:
    # Třída, která řeší validaci jednotlivých uživatelských vstupů

    # Metoda kontrolující jednotlivé uživatelské vstupy na základě input_type
    def validate_user_input(self, input_type):
        end = 0
        while end != 1:
            user_input = input(f"Zadejte {input_type} pojištěného: ").strip().lower()  # Získání vstupu s odstraněním mezer a zmenšením textu

            # Na základě daného input_type vybere validaci uživatelského vstupu
            match input_type:

                # Kontroluje, uživatelský vstup abecedou. Vrací uživatelský vstup s velkým prvním písmenem
                case "jméno" | "příjmení":
                    if user_input.isalpha():
                        end = 1
                        return user_input.capitalize()
                    else:
                        print(f"Špatně zadané {input_type}!")

                # Kontroluje, zdali je uživatelský vstup číslicí a je v rozmezí 0-110. Následně vrací uživatelský vstup
                case "věk":
                    if user_input.isdigit():
                        if 0 <= int(user_input) <= 110:
                            end = 1
                            return user_input
                        else:
                            print(f"Zadávejte {input_type} v rozmezí 0-110!")
                    else:
                        print("Zadávejte pouze čísla!")

                # Kontroluje, zdali je uživatelský vstup číslici s délkou stringu 9
                case "telefonní číslo":
                    if user_input.isdigit() and len(user_input) == 9:
                        end = 1
                        return user_input
                    else:
                        print(f"Špatně zadané {input_type}!")

    # Metoda přijme uživatelem zadanou operaci, kterou pak ověří, zdali je číslicí v rozmezí 1-4
    def validate_option_input(self):
        end = 0
        while end != 1:
            try:
                user_input = input("Vyberte možnost 1-4: ")
                if user_input.isdigit():
                    user_input = int(user_input)
                    if 1 <= user_input <= 4:
                        end = 1
                    else:
                        raise ValueError("Zadávejte čísla v rozmezí 1-4!")
                else:
                    raise ValueError("Zadávejte pouze čísla!")
            except ValueError as e:
                print(e)
            else:
                return user_input
