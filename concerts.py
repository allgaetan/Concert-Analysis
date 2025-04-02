from utils import *

class Concerts:
    def __init__(self, file_path=None, df=None):
        if file_path:
            self.data = load_csv(file_path)
        elif len(df) != 0:
            self.data = df
        else:
            self.data = pd.DataFrame(columns=["Date", "Bands", "City", "Venue"])

    def __str__(self):
        return f"{self.data}"
    
    def get_bands(self):
        all_bands = []
        for index, row in self.data.iterrows():
            bands = parse_bands(self.data, index)
            for band in bands:
                if band not in all_bands:
                    all_bands.append(band)
        all_bands = sorted(all_bands)
        return all_bands
    
    def get_cities(self):
        all_cities = []
        for index, row in self.data.iterrows():
            city = str(row["City"])
            if city not in all_cities:
                all_cities.append(city)
        all_cities = sorted(all_cities)
        return all_cities
    
    def get_venues(self):
        all_venues = []
        for index, row in self.data.iterrows():
            venue = str(row["Venue"])
            if venue not in all_venues:
                all_venues.append(venue)
        all_venues = sorted(all_venues)
        return all_venues

    def get_concert(self, date):
        concert = self.data[self.data["Date"] == date]
        return concert

    def get_concerts_between_dates(self, start_date=None, end_date=None):
        concerts = pd.DataFrame(columns=self.data.columns)
        if start_date is None:
            start_date = "01/01/2000"
        if end_date is None:
            end_date = "01/01/2100"
        start_date = str_to_date(start_date)
        end_date = str_to_date(end_date)
        rows = []
        for index, row in self.data.iterrows():
            date = str_to_date(row["Date"])
            if start_date <= date <= end_date:
                rows.append(row)
        concerts = pd.concat([concerts, pd.DataFrame(rows)], ignore_index=True)
        return concerts
    
    def get_concerts_by_city(self, city):
        concerts = pd.DataFrame(columns=self.data.columns)
        rows = []
        for index, row in self.data.iterrows():
            if str(row["City"]) == city:
                rows.append(row)
        concerts = pd.concat([concerts, pd.DataFrame(rows)], ignore_index=True)
        return concerts
    
    def get_concerts_by_venue(self, venue):
        concerts = pd.DataFrame(columns=self.data.columns)
        rows = []
        for index, row in self.data.iterrows():
            if str(row["Venue"]) == venue:
                rows.append(row)
        concerts = pd.concat([concerts, pd.DataFrame(rows)], ignore_index=True)
        return concerts

    def get_concerts_by_band(self, band):
        concerts = pd.DataFrame(columns=self.data.columns)
        rows = []
        for index, row in self.data.iterrows():
            bands = parse_bands(self.data, index)
            if band in bands:
                rows.append(row)
        concerts = pd.concat([concerts, pd.DataFrame(rows)], ignore_index=True)
        return concerts
    
    def get_bands_count(self, write_to_csv=False, details=False):
        bands = self.get_bands()
        bands_count = pd.DataFrame(columns=["Band", "Count"])
        rows = []
        for band in bands:
            count = get_band_count(self.data, band)
            if details:
                concerts = Concerts(df=self.get_concerts_by_band(band))
                rows.append({"Band": band, "Count": count, "Concerts": concerts})
            else:
                rows.append({"Band": band, "Count": count})
        bands_count = pd.concat([bands_count, pd.DataFrame(rows)], ignore_index=True)
        bands_count = bands_count.sort_values(by=["Count"], ascending=False)

        if write_to_csv:
            bands_count.to_csv("bands.csv", index=False)

        return bands_count

    def get_concerts_by_month(self, month):
        if month.split("/")[0] == "02":
            start_date = "01/02/" + month.split("/")[1]
            end_date = "28/02/" + month.split("/")[1]
        elif month.split("/")[0] in ["04", "06", "09", "11"]:
            start_date = "01/" + month.split("/")[0] + "/" + month.split("/")[1]
            end_date = "30/" + month.split("/")[0] + "/" + month.split("/")[1]
        else:
            start_date = "01/" + month.split("/")[0] + "/" + month.split("/")[1]
            end_date = "31/" + month.split("/")[0] + "/" + month.split("/")[1]
        concerts = self.get_concerts_between_dates(start_date=start_date, end_date=end_date)
        return concerts
    
    def get_concerts_by_year(self, year):
        start_date = "01/01/" + year
        end_date = "31/12/" + year
        concerts = self.get_concerts_between_dates(start_date=start_date, end_date=end_date)
        return concerts
    
    def plot_by_month(self):
        start_date = self.data["Date"][0]
        end_date = self.data["Date"][len(self.data)-1]
        year_span = [str(year) for year in range(int(start_date.split("/")[2]), int(end_date.split("/")[2]) + 1)]
        months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        month_span = []
        n_concerts = []
        n_bands = []
        for i, year in enumerate(year_span):
            for j, month in enumerate(months):
                month = month + "/" + year
                month_span.append(month)
                c = Concerts(df=self.get_concerts_by_month(month))
                n_concerts.append(len(c.data))
                n_bands.append(len(c.get_bands()))

        return plot(month_span, n_concerts, n_bands)
        
    def plot_by_year(self):
        start_date = self.data["Date"][0]
        end_date = self.data["Date"][len(self.data)-1]
        year_span = [str(year) for year in range(int(start_date.split("/")[2]), int(end_date.split("/")[2]) + 1)]
        n_concerts = []
        n_bands = []
        for i, year in enumerate(year_span):
            c = Concerts(df=self.get_concerts_by_year(year))
            n_concerts.append(len(c.data))
            n_bands.append(len(c.get_bands()))

        return plot(year_span, n_concerts, n_bands)