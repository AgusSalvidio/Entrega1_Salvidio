from .promo_code import PromoCode

class PromoCodeManagementSystem:

    def __init__(self):
        self.promo_codes_repo = PromoCode.objects

    def promo_codes(self):
        return self.promo_codes_repo.all()
