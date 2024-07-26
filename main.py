import pandas as pd
import plotly.express as px
import json
import sys

# https://simplemaps.com/data/us-zips


def get_zip_from_address(address: str):
    return address.split(" ")[-2][:5]


def main():
    args = sys.argv[1:]
    path_to_csv = args[0]

    # Import GeoJSON
    geojson_file = open("./virginia-zip-codes-_1615.geojson")
    zip_geojson = json.load(geojson_file)

    # Import Sales CSV
    df_sales = pd.read_csv(path_to_csv)

    # Get count of zips from sales
    sales_dict = {}
    df_sales_cleaned = df_sales.dropna(subset=["Customer Address"])
    for row in df_sales_cleaned["Customer Address"]:
        zip_from_address = get_zip_from_address(str(row))
        if zip_from_address in sales_dict.keys():
            sales_dict[zip_from_address] = sales_dict[zip_from_address] + 1
        else:
            sales_dict[zip_from_address] = 1

    df_zip_sales = pd.DataFrame(sales_dict, index=[0])
    df_zip_sales_melted = pd.melt(df_zip_sales)

    max_sales_count = df_zip_sales_melted["value"].max()

    print(max_sales_count)

    # Create choropleth figure
    fig = px.choropleth_mapbox(
        df_zip_sales_melted,
        geojson=zip_geojson,
        locations="variable",
        featureidkey="properties.ZCTA5CE10",
        center={"lat": 37.4316, "lon": -78.6569},
        color="value",
        color_continuous_scale="Viridis",
        range_color=(0, max_sales_count),
        mapbox_style="carto-positron",
        labels={"value": "Number of Sales"},
    )

    fig.show()


if __name__ == "__main__":
    main()
