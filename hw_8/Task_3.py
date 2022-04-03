import sys
import datetime
import requests
from requests.exceptions import HTTPError, ConnectionError


def print_form(message):
    print(">")
    print('-' * 14)
    print(message)
    print('=' * 14)


def print_exchange_rate(currency_str, rate_str):
    print_form(f"{currency_str}\n\n{rate_str}")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit()

    currency_code = ''
    if len(sys.argv) >= 2:
        currency_code = sys.argv[1]
        if len(currency_code) > 3:
            print_form(
                f"{currency_code}\n\n" +
                f"Currency code cannot be longer than 3 characters: {currency_code} \n" +
                "For a list of supported currency codes see:\n" +
                "\thttps://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json\n   (json field 'cc')"
            )
            exit()

    requested_date = datetime.datetime.now()

    if len(sys.argv) >= 3:
        try:
            requested_date = datetime.datetime.fromisoformat(sys.argv[2])
        except Exception as err_or:
            print_form("Invalid date: " + sys.argv[2])
            exit()

        if requested_date <= datetime.datetime.fromisoformat("1996-01-05"):
            print_form(f"Date provided: {requested_date} \n is earlier than the date from which exchange rates are "
                       f"available (1996-01-06 for USD).For other currencies availability start dates "
                       f"may be even later.")
            exit()

    date_str = requested_date.strftime("%Y%m%d")

    request_URL = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code.upper()}" \
                  f"&date={date_str}&json"

    try:
        rate_json = requests.get(request_URL)

        if 'Request unsuccessful.' in rate_json.text:
            print("Request unsuccessfull. Please try later (e.g. in 1-3 minutes).")
            exit()

    except HTTPError as http_error:
        print_form(f'HTTP error occurred: {http_error}')
        exit()
    except ConnectionError as connect_error:
        print_form(f'Connection error occurred (please ensure that site https://bank.gov.ua is reachable '
                   f'from this machine): \n {connect_error}')
        exit()
    except Exception as err_or:
        print_form(f'System Error: {err_or}')
        exit()

    if len(rate_json.json()) == 0:
        print_form("Invalid currency: " + currency_code)
        exit()

    received_rate_json = rate_json.json()[0]
    print_exchange_rate(received_rate_json['cc'], received_rate_json['rate'])
    