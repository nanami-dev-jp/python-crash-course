## 11-1

def city_country(city, country, population=None):
    """都市名と国名・(任意で)人口を受け取り、文字列を返す"""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"