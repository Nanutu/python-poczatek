class TaxCalculator:

    TAX_RATES = {
        "fruits and vegetables": 0.05,
        "Food": 0.08
    }
    OTHER = 0.2

    @staticmethod
    def tax_for_order_element(order_element):
        product_category = order_element.product.category_name
        if product_category in TaxCalculator.TAX_RATES:
            tax_rate = TaxCalculator.TAX_RATES[product_category]
        else:
            tax_rate = TaxCalculator.OTHER
        return tax_rate * order_element.calculate_price()
