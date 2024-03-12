def confirm_transaction(message):
    sender, receiver, amount = int(message["sender"]), int(message["receiver"]), int(message["amount"])
    print(f"Confirming transaction sender: {sender}, receiver: {receiver}, amount: {amount}")

    accounts = execute_sql_query(["SELECT * FROM bank_account"])[0]
    old_sender, old_receiver = accounts[sender - 1][1:3], accounts[receiver - 1][1:3]

    if int(old_sender[1]) < amount:
        print(f"Insufficient funds: sender: {sender}, receiver: {receiver}, amount: {amount}")
    else:
        publish_message(str({"body": {"sender": sender, "receiver": receiver, "amount": amount}}), True)
        print(f"Transaction confirmed: sender: {sender}, receiver: {receiver}, amount: {amount}")
