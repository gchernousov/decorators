from log_decorator import log_decorator

# курс валют на 25.06.2022:
CURRENCY_DICT = {
    "USD": 53.32,
    "EUR": 55.96,
    "BRL": 10.29,
    "INR": 0.68,
    "KZT": 0.11,
    "CNY": 8.02,
    "PLN": 11.94,
    "TRY": 3.07,
    "UAH": 1.80,
    "JPY": 0.39
}


@log_decorator("requests.log")
def converter(rub: int, currency: str):
    if currency in CURRENCY_DICT:
        v = CURRENCY_DICT[currency]
        result = rub / v
        return round(result, 2)
    else:
        return f"Данных о валюте {currency} нет."


if __name__ == "__main__":

    print(converter(500, "USD"))
    # print(converter(1000, "TRY"))
    # print(converter(100, "EUR"))
    # print(converter(25000, "CNY"))
    # print(converter(9000, "ZBR"))
    # print(converter(7000, "PLN"))
    # print(converter(100000, "BRL"))