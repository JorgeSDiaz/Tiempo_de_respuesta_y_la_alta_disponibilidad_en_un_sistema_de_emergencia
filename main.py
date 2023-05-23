import random
from time import time

from phone_numbers_extractor import extract_numbers_from_google_csv
from request import send_post_request

CONTACTS = []


def save_list_in_txt(list_to_save: list, file_name: str) -> None:
    text_list = ",".join(list_to_save)

    with open(file_name + ".txt", "w") as file:
        file.write(str(text_list))


def format_number(country_code: str, number: str) -> str:
    formatted_number = number.replace("+", "", -1).replace(" ", "", -1)\
        .replace(":", "", -1).replace("#", "", -1)\
        .replace("-", "", -1)

    if not formatted_number.startswith("57"):
        number_without_code = "".join(formatted_number.split())[2::]
        formatted_number = country_code + number_without_code

    return formatted_number


def alert(message: str, cant: int) -> float:
    start = time()
    for i in range(cant):
        index = int(random.random() * len(CONTACTS))
        data = {
            "message": message,
            "phone": CONTACTS[index]
        }
        response_data = send_post_request(data)
        if response_data:
            print(f"Response for request {i + 1}:", response_data)
    end = time()
    return end - start


def main() -> None:
    contacts = extract_numbers_from_google_csv("contacts.csv")

    for index in range(len(contacts)):
        contacts[index] = format_number("57", str(contacts[index]))

    contacts = list(filter(lambda x: len(x) == 12, contacts))
    for contact in contacts:
        CONTACTS.append(contact)

    cant = input("Insert the number of requests you wish to make: ")
    while cant != "0":
        alert("""
            Test: Temblor en Bogota
                  prueba de funcionalidad ECI - Arquitectura Empresarial
            """, int(cant))

        cant = input("Insert the number of requests you wish to make: ")

    save_list_in_txt(contacts, "contacts")


if __name__ == '__main__':
    main()
