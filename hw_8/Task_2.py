import requests
from time import sleep
from sys import argv


class CitiesData:
    # Connect to API server
    headers = {
        'x-rapidapi-key': "21c453a4d6mshf97b6774430c674p1b1149jsn804d3d516f1a",
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
    }

    def __init__(self, city):
        self.city = str(city)

    @staticmethod
    def error():
        return f'{"-" * 14}\nSystem Error\n{"=" * 14}'

    def invalid_name(self):
        return f'{"-" * 14} \n{self.city}\n\nInvalid city name: {self.city}\n {"=" * 14}'

    @staticmethod
    def currency(country_code: str):
        # Takes the country code from 'show_info' and return a currency of one
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/" + country_code

        try:
            response = requests.request("GET", url, headers=CitiesData.headers, timeout=5).json()
        except requests.RequestException:
            return CitiesData.error()

        res = response['data']['currencyCodes'][0]
        return res if res else 'No info'

    def show_city_info(self):
        # Main function, does  request to the API, forming the result
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
        querystring = {"namePrefix": self.city}

        try:
            response = requests.request("GET", url, headers=self.headers, params=querystring, timeout=5).json()
        except requests.RequestException:
            return CitiesData.error()

        if response['metadata']['totalCount'] == 0:
            return self.invalid_name()
        response = response['data']
        response = sorted(response, key=lambda x: x['population'], reverse=True)

        res = []
        for item in response:
            sleep(1.5)  # Since the api doesn't allow more than 1 request per second
            if item['population'] == 0:
                continue
            res.extend(
                [
                    "-" * 14, '\n', self.city, '\n\n', item['country'], '\n',
                    CitiesData.currency(item['countryCode']), '\n', str(item['population']), '\n', "=" * 14, '\n'
                ]
            )

        return ''.join(res)

    @staticmethod
    def main():
        # Launcher
        args = argv[1:]
        print(args)
        data = ' '.join(args)
        data = data.capitalize()
        data = CitiesData(data)
        return data.show_city_info()


if __name__ == '__main__':
    # Start
    print(CitiesData.main())
