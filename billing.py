def calculate_delivery_cost(city: str, weight_kg: float) -> float:
    if city == "Ivano-Frankivsk":
        base_rate = 50.0
    elif city == "Kyiv":
        base_rate = 80.0
    else:
        base_rate = 110.0
    return base_rate + (weight_kg * 15.0)


def process_standard_invoice(amount: float, city: str, weight_kg: float, tax_rate: float = 0.20) -> dict:
    """Обробка стандартного інвойсу без Common та Control Coupling (tax_rate передається явно з замовчуванням 0.20)."""
    delivery = calculate_delivery_cost(city, weight_kg)
    total = (amount * (1 + tax_rate)) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}

def process_tax_exempt_invoice(amount: float, city: str, weight_kg: float) -> dict:
    """Обробка інвойсу без ПДВ без Control Coupling (окрема прозора функція)."""
    delivery = calculate_delivery_cost(city, weight_kg)
    total = amount + delivery
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
