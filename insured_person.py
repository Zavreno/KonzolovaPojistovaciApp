class ManageInsuredPerson:
    # Třída řešící práci se samotnými pojištenci uloženými v kolekci
    # Konstruktor, v nemž máme definovaný seznam, do kterého budeme vkládat údaje jednotlivých osob uložených ve slovníku
    def __init__(self):
        self.persons_list = []

    # Metoda přijme atributy zadané uživatelem a následně je uloží do slovníku, který je pak vložen do seznamu
    def add_person(self, first_name, last_name, phone_number, age):
        person_dict = {
            "first": first_name,
            "last": last_name,
            "age": age,
            "phone": phone_number
        }
        self.persons_list.append(person_dict)

    # Metoda přijme uživatelem zadané atributy, které pak porovnává se všemi pojištenci v seznamu.
    # Pokud je nalezena shoda, vrátí údáje vyhledávané osoby
    def search_person(self, first_name, last_name):
        for person in self.persons_list:
            if person["first"] == first_name and person["last"] == last_name:
                return f"\n{person["first"]}\t{person["last"]}\t{person["age"]}\t\t{person["phone"]}"
        1return f"Pojištěný nenalezen!"

    # Metoda, která vrací celý seznam pojištěnců
    def __str__(self):
        result = ""
        for person in self.persons_list:
            result += f"{person['first']}\t{person['last']}\t{person['age']}\t\t{person['phone']}\n"
        return result
