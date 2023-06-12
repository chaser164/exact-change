def exact_change(amount_paid, item_cost, currency):

    def change_pesos(amount_paid, item_cost):
        pesos_to_usd = amount_paid * 0.058
        return item_cost - pesos_to_usd

    def change_yen(amount_paid, item_cost):
        yen_to_usd = amount_paid * 0.0072
        return item_cost - yen_to_usd 

    def change_euros(amount_paid, item_cost):
        euros_to_usd = amount_paid * 1.08
        return item_cost - euros_to_usd 

    def change_ruble(amount_paid, item_cost):
        ruble_to_usd = amount_paid * 0.012
        return item_cost - ruble_to_usd 
    
