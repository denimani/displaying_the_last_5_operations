from operation_data import last_five_operations
from transfer_data import TransferData


def show_result():
    for operation in last_five_operations():
        transfer_data = TransferData(operation["date"], operation["description"],
                                     operation["to"], operation["operationAmount"]["amount"],
                                     operation["operationAmount"]["currency"]["name"])
        if operation.get("from"):
            print(
                f'{transfer_data.data_date_and_description()}\n'
                f'{transfer_data.data_from_whom(operation["from"])} -> {transfer_data.data_to_whom()}\n'
                f'{transfer_data.data_moneys()}\n'
            )
        else:
            print(
                f'{transfer_data.data_date_and_description()}\n'
                f'{transfer_data.data_to_whom()}\n'
                f'{transfer_data.data_moneys()}\n'
            )


show_result()
