class PaymentService:
    def _validate(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Montant invalide")

    def pay_by_card(self, amount):
        self._validate(amount)
        return f"Paiement par carte accepté : {amount}€"

    def pay_by_paypal(self, amount):
        self._validate(amount)
        return f"Paiement par PayPal accepté : {amount}€"

    def pay_by_apple_pay(self, amount):
        self._validate(amount)
        return f"Paiement par Apple Pay accepté : {amount}€"

    def pay_by_google_pay(self, amount):
        self._validate(amount)
        return f"Paiement par Google Pay accepté : {amount}€"
