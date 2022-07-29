class atm:
    def __init__(self,id_card,password,saving=10000):#double underscore dunder
        self.id_card=id_card
        self.password=password
        self.saving=saving

    def deposit(self):
        income=int(input("How much do you want to deposit in this account : "))
        self.saving=self.saving+income
        print(f"Your balance is {self.saving} Bath.")

    def withdraw(self):
        outcome=int(input("How much do you want to withdraw in this account : "))
        if  self.saving<outcome:
            print(f"your current balane is not enough.")
        else:
            self.saving=self.saving-outcome
            print(f"Your balance is {self.saving} Bath.")

    def check_balance(self):
        print(f"Your current balance is {self.saving} Bath.")

    def transfer_to_account(self):
        account_to_transfer=int(input("Please insert Accout ID which you want to transfer : "))
        transfer_amount=int(input("How much do you want to transfer to this account : "))
        if self.saving<transfer_amount:
            print(f"your current balane is not enough.")
        else:
            self.saving=self.saving-transfer_amount
            print(f"Your current balance is {self.saving} Bath.")
    
    def transfer_to_foreign(self):
        country_to_transfer=str(input("Please insert country which you want to transfer (e.g. 'japan,'usa','Brtish'): "))
        account_foreign=int(input("Please insert Accout ID which you want to transfer : "))
        transfer_amount=int(input("How much do you want to transfer to this other currency : "))

        if country_to_transfer=="japan":
            rate=float(0.265688)
            withdraw_bth=rate*transfer_amount           
        elif country_to_transfer=="usa":
            rate=float(36.69)
            withdraw_bth=rate*transfer_amount
        else:
            rate=float(43.68)
            withdraw_bth=rate*transfer_amount
    
        while withdraw_bth<self.saving:
            self.saving=self.saving-withdraw_bth
            print(f"Currency rate is {rate}.Your current balance witrhdraw is {withdraw_bth} ")
            print(f"Your current balance is {self.saving} Bath.")
            break
        else:
            print(f"your current balane is not enough.")
