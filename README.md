# Python Currency Converter Scripts

A Python script that converts currencies using real-time exchange rates from an online API. This tool allows you to convert between different currencies with ease.

## Features

- **Real-Time Conversion**: Converts currency values based on up-to-date exchange rates.
- **Supports Multiple Currencies**: Allows conversion between many commonly used currencies.
- **API Integration**: Fetches exchange rates from a currency API (e.g., [ExchangeRate-API](https://www.exchangerate-api.com/)).

## Requirements

- **Python 3.x**
- **API Key**: You will need an API key from a currency exchange service (e.g., ExchangeRate-API).

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Python_Currency_Converter_Scripts.git
    cd Python_Currency_Converter_Scripts
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Get API Key**:

    Sign up for an API key at a currency exchange service provider such as [ExchangeRate-API](https://www.exchangerate-api.com/).

4. **Set up the API Key**:

    In the script, replace the placeholder for the API key with your actual key.

    ```python
    api_key = 'your_api_key'
    ```

5. **Run the Script:**

    ```bash
    python converter.py
    ```

### How to Use

- The script will prompt you to enter the source currency, target currency, and the amount to convert.
- It will then fetch the latest exchange rate and calculate the converted value.

### Project Structure

- `converter.py`: Main script that handles the conversion logic and interacts with the API.
- `requirements.txt`: Lists necessary libraries such as `requests` for API calls.

## Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

## License

This project is open-source and available for educational purposes.
 
