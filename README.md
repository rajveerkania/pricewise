# PriceWise

PriceWise is an innovative web project designed to provide users with a seamless and intelligent solution for comparing product prices between two of the leading e-commerce giants, Amazon and Flipkart. With its advanced algorithms and user-friendly interface, PriceWise empowers shoppers to make informed purchasing decisions while maximizing savings.

## Installation

Install the required packages using the package manager [pip](https://pip.pypa.io/en/stable/).

```terminal
pip install -r requirements.txt
```

## Usage

In order to start the server, use the following command on your terminal

```terminal
python manage.py runserver
```

## Working

Once the HTML content of the product pages is fetched, the BeautifulSoup4 package is employed to parse and navigate the HTML structure. This allows you to extract relevant information such as product names, prices, descriptions, ratings, and reviews.

The scraped data from both websites is then compared to identify price differences and other relevant details. This comparison is performed within your Django web app.

Finally, the compared data is presented to the user through the web interface.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)