from concerts import Concerts
   
if __name__ == "__main__":
    concerts = Concerts(file_path="history.csv")
    """
    Functionnalities test:
    
    print(concerts)
    print(concerts.get_bands())
    print("Number of bands:", len(concerts.get_bands()))
    print(concerts.get_cities())
    print(concerts.get_venues())
    print(concerts.get_concert("05/05/2018"))
    print(concerts.get_concerts_between_dates(start_date="01/01/2018", end_date="01/01/2020"))
    print(concerts.get_concerts_by_city("Paris"))
    print(concerts.get_concerts_by_venue("Bataclan"))
    print(concerts.get_concerts_by_band("Deathawaits"))
    print(concerts.get_bands_count(write_to_csv=True))
    print(concerts.get_concerts_by_month("02/2023"))
    print(concerts.get_concerts_by_year("2023"))"
    concerts.plot_by_month()
    concerts.plot_by_year()
    """
    concerts.get_bands_count(write_to_csv=True, details=True)