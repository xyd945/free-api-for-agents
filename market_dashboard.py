import urllib.request
import json
import concurrent.futures

def fetch_data(url, headers=None):
    """Helper function to fetch JSON data from a URL using built-in libraries."""
    if headers is None:
        headers = {'User-Agent': 'Mozilla/5.0 MarketDashboard/1.0'}
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return data
            else:
                return {"error": f"HTTP {response.status}"}
    except Exception as e:
        return {"error": str(e)}

def get_exchange_rates():
    """Fetch USD exchange rates to EUR, GBP, JPY using Frankfurter API."""
    data = fetch_data("https://api.frankfurter.app/latest?from=USD&to=EUR,GBP,JPY")
    if "error" in data:
        return {"error": data["error"]}
    return data.get("rates", {})

def get_crypto_prices():
    """Fetch Bitcoin and Ethereum prices via CoinGecko."""
    data = fetch_data("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd")
    if "error" in data:
        return {"error": data["error"]}
    return {
        "BTC": data.get("bitcoin", {}).get("usd", "N/A"),
        "ETH": data.get("ethereum", {}).get("usd", "N/A")
    }

def get_us_national_debt():
    """Fetch the latest Total Public Debt Outstanding from the U.S. Treasury."""
    url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?fields=record_date,tot_pub_debt_out_amt&page[size]=1&sort=-record_date"
    data = fetch_data(url)
    if "error" in data:
        return {"error": data["error"], "date": "N/A"}
    try:
        latest = data["data"][0]
        debt_amount = float(latest.get("tot_pub_debt_out_amt", 0))
        # Format as Trillions
        formatted_debt = f"${debt_amount / 1_000_000_000_000:.2f} Trillion"
        return {"amount": formatted_debt, "date": latest.get("record_date", "N/A")}
    except (KeyError, IndexError, ValueError):
        return {"error": "Failed to parse debt data", "date": "N/A"}

def main():
    print("Fetching Global Economic Dashboard...")
    print("-" * 50)
    
    # Fetch data concurrently for faster load time
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_fx = executor.submit(get_exchange_rates)
        future_crypto = executor.submit(get_crypto_prices)
        future_debt = executor.submit(get_us_national_debt)

        # Retrieve results
        fx_rates = future_fx.result()
        crypto_prices = future_crypto.result()
        us_debt = future_debt.result()
        
    dashboard = f"""
==================================================
📊 EXECUTIVE MARKET DASHBOARD 
==================================================

💱 FOREIGN EXCHANGE (1 USD)
- EUR: {fx_rates.get('EUR', 'N/A')}
- GBP: {fx_rates.get('GBP', 'N/A')}
- JPY: {fx_rates.get('JPY', 'N/A')}

🪙 CRYPTOCURRENCY MARKETS
- Bitcoin (BTC) : ${crypto_prices.get('BTC', 'N/A'):,}
- Ethereum (ETH): ${crypto_prices.get('ETH', 'N/A'):,}

🇺🇸 U.S. NATIONAL DEBT
- Total Outstanding: {us_debt.get('amount', us_debt.get('error', 'N/A'))}
- As of Record Date: {us_debt.get('date', 'N/A')}

==================================================
    """
    
    print(dashboard)

if __name__ == "__main__":
    main()
