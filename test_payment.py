import pytest
from payment import PaymentService

service = PaymentService()


def test_card_payment():
    assert service.pay_by_card(100) == "Paiement par carte accepté : 100€"


def test_paypal_payment():
    assert service.pay_by_paypal(50) == "Paiement par PayPal accepté : 50€"


def test_apple_pay_payment():
    assert service.pay_by_apple_pay(75) == "Paiement par Apple Pay accepté : 75€"


def test_google_pay_payment():
    assert service.pay_by_google_pay(200) == "Paiement par Google Pay accepté : 200€"


def test_card_invalid_amount():
    with pytest.raises(ValueError, match="Montant invalide"):
        service.pay_by_card(-10)


def test_paypal_invalid_amount():
    with pytest.raises(ValueError, match="Montant invalide"):
        service.pay_by_paypal(0)


def test_apple_pay_invalid_amount():
    with pytest.raises(ValueError, match="Montant invalide"):
        service.pay_by_apple_pay("gratuit")


def test_google_pay_invalid_amount():
    with pytest.raises(ValueError, match="Montant invalide"):
        service.pay_by_google_pay(-1)
