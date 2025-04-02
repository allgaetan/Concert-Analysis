from concerts import Concerts
   
if __name__ == "__main__":
    concerts = Concerts(file_path="history.csv")

    test_routine = 1
    if test_routine:
        print("\nAll concerts seen:")
        print(concerts)

        print("\nAll bands seen:")
        bands = concerts.get_bands()
        print(bands)
        print(f"Number of bands seen: {len(bands)}")

        print("\nCities:")
        print(concerts.get_cities())

        print("\nVenues:")
        print(concerts.get_venues())

        print("\nConcert seen on May 5th 2018:")
        print(concerts.get_concert("05/05/2018"))

        print("\nConcerts seen between January 1st 2018 and January 1st 2020:")
        print(concerts.get_concerts_between_dates(start_date="01/01/2018", end_date="01/01/2020"))

        print("\nConcerts seen in Paris:")
        print(concerts.get_concerts_by_city("Paris"))

        print("\nConcerts seen at Bataclan:")
        print(concerts.get_concerts_by_venue("Bataclan"))

        print("\nConcerts where Meshuggah played:")
        print(concerts.get_concerts_by_band("Meshuggah"))

        print("\nNumber of times each band has been seen with the dates (written in bands.csv):")
        print(concerts.get_bands_count(write_to_csv=True, dates=True))

        print("\nConcerts seen in February 2023:")
        print(concerts.get_concerts_by_month("02/2023"))

        print("\nConcerts seen in 2023:")
        print(concerts.get_concerts_by_year("2023"))

        print("\nPlotting the number of concerts and been seen by month...")
        concerts.plot_by_month()

        print("\nPlotting the number of concerts and been seen by year...")
        concerts.plot_by_year()

        print("Done.")
