class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show your account open status")
    def deposit(self):
        print("this will show your deposited account")

class hdfc_bank(bank):
    def hdfc_to_icici(self):
        print("this is for showing all the transaction happend to icici through hdfc")

class icici(hdfc_bank):
    pass
i = icici()
i.hdfc_to_icici()
i.deposit()
i.account_opening()
i.transaction()