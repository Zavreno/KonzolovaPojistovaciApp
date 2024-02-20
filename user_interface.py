from validate_input import ValidateInput
from insured_person import ManageInsuredPerson


class UserInterface:

    def __init__(self):
        self.insured_person = ManageInsuredPerson()  # Instance třídy InsuredPerson, ve které pracujeme se získanými daty
        self.validate = ValidateInput()  # Instance třídy ValidateInput, která ověřuje uživatelské vstupy

# Metoda, jenž nám vypisuje 4 možnosti, které může uživatel zvolit
    def choose_option(self):
        end = 0
        while end != 1:
            print(
                "Vyberte si akci:\n"
                "1 - Přidat nového pojišteného\n"
                "2 - Vypsat všechny pojištěné\n"
                "3 - Vyhledat pojištěného\n"
                "4 - Konec\n"
            )

            # Získání a kontrola vstupu od uživatele, dle nehož se uplatní akce v match
            option_input = self.validate.validate_option_input()

            match option_input:

                # První možnost umožnuje uživateli přidávat nové pojištěnce do kolekce
                case 1:
                    print()
                    # Získání jednotlivých vstupů společne s jejich validací
                    first_name = self.validate.validate_user_input("jméno")
                    last_name = self.validate.validate_user_input("příjmení")
                    age = self.validate.validate_user_input("věk")
                    phone = self.validate.validate_user_input("telefonní číslo")
                    # Zavolání metody, která ukládá jednotlivá data do kolekce
                    self.insured_person.add_person(first_name, last_name, phone, age)
                    input("\nData byla uložena. Pro pokračování stiskněte ENTER...")
                    return self.choose_option()  # Vrací uživatele zpět na výběr možností

                # Druhá možnost vypisuje všechny pojištěnce, kteří jsou uloženi v kolekci
                case 2:
                    # Výpis všech pojištěnců
                    print(self.insured_person)
                    input("\nPro pokračování stiskněte ENTER...")
                    return self.choose_option()  # Vrací uživatele zpět na výběr možností

                # Třetí možnost vyhledá dle zadaných hodnot daného pojištěnce a následně ho vypíše
                case 3:
                    # Získání jednotlivých vstupů společne s jejich validací
                    first_name = self.validate.validate_user_input("jméno")
                    last_name = self.validate.validate_user_input("příjmení")
                    found_person = self.insured_person.search_person(first_name, last_name)
                    print(found_person)
                    input("\nPro pokračování stiskněte ENTER...")
                    return self.choose_option()  # Vrací uživatele zpět na výběr možností

                # Čtvrtá možnost program ukončí
                case 4:
                    print("Program ukončen!")
                    end = 1
