import requests
import matplotlib.pyplot as plt
from datetime import datetime

def get_bitcoin_prices_last_20_days():
    # URL для получения исторических данных о цене биткоина
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

    # Параметры запроса: валюта (usd) и количество дней (20)
    params = {"vs_currency": "usd", "days": "20"}

    # Выполняем GET-запрос к API
    response = requests.get(url, params=params)

    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        data = response.json()
        prices = data["prices"]

        # Преобразуем timestamp в дату и цену в удобный формат
        price_data = {}
        for price in prices:
            date = datetime.fromtimestamp(price[0] / 1000).strftime(
                "%d.%m.%Y"
            )  # Формат DD.MM.YYYY
            price_usd = price[1]
            # Сохраняем только одну цену за день
            if date not in price_data:
                price_data[date] = price_usd

        # Преобразуем словарь в список кортежей и сортируем по дате
        sorted_price_data = sorted(
            price_data.items(), key=lambda x: datetime.strptime(x[0], "%d.%m.%Y")
        )
        return sorted_price_data
    else:
        print("Ошибка при получении данных:", response.status_code)
        return None


def generate_report(price_data):
    if price_data:
        print("Отчёт об изменении цены биткоина за последние 20 дней:")
        print("=" * 50)
        for i in range(len(price_data) - 1):
            current_date, current_price = price_data[i]
            next_date, next_price = price_data[i + 1]
            price_change = next_price - current_price
            change_percentage = (price_change / current_price) * 100

            print(f"Дата: {current_date}")
            print(f"Цена: ${current_price:.2f}")
            print(
                f"Изменение цены на следующий день ({next_date}): ${price_change:.2f} ({change_percentage:.2f}%)"
            )
            print("-" * 50)
    else:
        print("Нет данных для формирования отчёта.")


def plot_price_chart(price_data):
    if price_data:
        dates = [item[0] for item in price_data]
        prices = [item[1] for item in price_data]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, prices, marker="o", linestyle="-", color="b")
        plt.title("Изменение цены биткоина за последние 20 дней")
        plt.xlabel("Дата")
        plt.ylabel("Цена (USD)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Нет данных для построения графика.")


if __name__ == "__main__":
    price_data = get_bitcoin_prices_last_20_days()
    generate_report(price_data)
    plot_price_chart(price_data)

