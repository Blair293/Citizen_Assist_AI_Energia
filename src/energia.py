from dataclasses import dataclass

@dataclass
class EnergyScenario:
    old_lamp_w: float = 60
    led_lamp_w: float = 9
    quantity: int = 5
    hours_per_day: float = 5
    days_per_month: int = 30
    tariff_per_kwh: float = 0.90
    led_price: float = 12.0
    solar_system_kwp: float = 0.5
    peak_sun_hours: float = 4.5
    performance_ratio: float = 0.80
    solar_installation_cost: float = 3500.0

def monthly_consumption(power_w, quantity, hours_day, days):
    """Calcula o consumo mensal em kWh."""
    if min(power_w, quantity, hours_day, days) < 0:
        raise ValueError("Os parâmetros de consumo não podem ser negativos.")
    return power_w * quantity * hours_day * days / 1000

def monthly_cost(consumption_kwh, tariff):
    if consumption_kwh < 0 or tariff < 0:
        raise ValueError("Consumo e tarifa não podem ser negativos.")
    return consumption_kwh * tariff

def analyze(s):
    old_kwh = monthly_consumption(s.old_lamp_w, s.quantity, s.hours_per_day, s.days_per_month)
    led_kwh = monthly_consumption(s.led_lamp_w, s.quantity, s.hours_per_day, s.days_per_month)
    saved_kwh = old_kwh - led_kwh
    saved_monthly = monthly_cost(saved_kwh, s.tariff_per_kwh)
    led_investment = s.quantity * s.led_price
    solar_generation = s.solar_system_kwp * s.peak_sun_hours * s.days_per_month * s.performance_ratio
    solar_offset = min(solar_generation, old_kwh)
    solar_monthly_value = monthly_cost(solar_offset, s.tariff_per_kwh)
    return {
        "old_kwh": old_kwh, "led_kwh": led_kwh, "saved_kwh": saved_kwh,
        "old_cost": monthly_cost(old_kwh, s.tariff_per_kwh),
        "led_cost": monthly_cost(led_kwh, s.tariff_per_kwh),
        "saved_monthly": saved_monthly, "led_investment": led_investment,
        "led_payback_months": led_investment / saved_monthly if saved_monthly > 0 else None,
        "solar_generation": solar_generation, "solar_offset": solar_offset,
        "solar_monthly_value": solar_monthly_value,
        "solar_cost": s.solar_installation_cost,
        "solar_payback_months": s.solar_installation_cost / solar_monthly_value if solar_monthly_value > 0 else None
    }
