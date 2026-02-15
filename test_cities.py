from city_functions import city_country

def test_city_country_population():
    """'santiago', 'chile'の組み合わせが正しく動くかどうかをテストする"""
    formatted_name = city_country('santiago', 'chile', population=5000000)
    assert formatted_name == 'Santiago, Chile - population 5000000'