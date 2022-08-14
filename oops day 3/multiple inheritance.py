class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show your account open status")
    def deposit(self):
        print("this will show your deposited account")
    def test(self):
        print("this is test method for bank class")

class hdfc_bank:
    def hdfc_to_icici(self):
        print("this is for showing all the transaction happend to icici through hdfc")
    def test(self):
        print("this method from hdfc  bank")

class ineuron_bank:
    def account_status_icici(self):
        print("this is account status in icici")

class icici(hdfc_bank, bank, ineuron_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.transaction()
i.test()
i.account_status_icici()

# in case of name conflict it will take according to order place
