from urllib import request

url = 'https://data.winnipeg.ca/resource/x5er-sfwa.csv'


def download_stock_data(csv_url):
    # connect to internet
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")

    # r means raw (good idea when working with file path)
    dest_url = r"goog.csv"

    fx = open(dest_url, "w")

    for line in lines:
        fx.write(line + "\n")

    fx.close()


download_stock_data(url)