import json
import pandas as pd


INPUT_FILE = "Data/yelp_academic_dataset_business (1).json"
OUTPUT_FILE = "outputs/yelp_business_flattened.csv"

rows = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)
        attributes = item.get("attributes", {}) or {}
        hours = item.get("hours", {}) or {}
        row = {
            "business_id": item.get("business_id"),
            "name": item.get("name"),
            "city": item.get("city"),
            "state": item.get("state"),
            "postal_code": item.get("postal_code"),
            "latitude": item.get("latitude"),
            "longitude": item.get("longitude"),
            "stars": item.get("stars"),
            "review_count": item.get("review_count"),
            "is_open": item.get("is_open"),
            "categories": item.get("categories"),
            "restaurants_price_range": attributes.get("RestaurantsPriceRange2"),
            "bike_parking": attributes.get("BikeParking"),
            "business_accept_credit_cards": attributes.get("BusinessAcceptsCreditCards"), 
            "good_for_kids": attributes.get("GoodForKids"), 
            "restaurants_take_out": attributes.get("RestaurantsTakeOut"), 
            "restaurants_delivery": attributes.get("RestaurantsDelivery"),
            "wheelchair_access": attributes.get("WheelchairAccesible"), 
             "outdoor_seating": attributes.get("OutdoorSeating"), 
             "monday_hours": hours.get("Monday"), 
             "tuesday_hours": hours.get("Tuesday"), 
             "wednesday_hours": hours.get("Wednesday"), 
             "thursday_hours": hours.get("Thursday"), 
              "friday_hours": hours.get("Friday"), 
             "saturday_hours": hours.get("Saturday"), 
             "sunday_hours": hours.get("Sunday"), 


        }
        rows.append(row)
df = pd.DataFrame(rows)
print (df.head())
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
 
