from supabase_service import get_contacts
from src.zapi_service import send_message


def main():
    try:
        contacts = get_contacts()
        print(contacts)
        print(f"{len(contacts)} contatos encontrados")

        if not contacts:
            print("Nenhum contato encontrado.")
            return

        for contact in contacts:

            print(
                f"Enviando mensagem para "
                f"{contact['Nome']}..."
            )

            response = send_message(
                contact["Telefone"],
                contact["Nome"]
            )

            print(
                f"Status: {response.status_code}"
            )

    except Exception as error:
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()