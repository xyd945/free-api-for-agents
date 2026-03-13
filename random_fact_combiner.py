import urllib.request
import json
import concurrent.futures

def fetch_data(url, headers=None):
    """Helper function to fetch JSON data from a URL using built-in libraries."""
    if headers is None:
        headers = {'User-Agent': 'Mozilla/5.0 FreeAPIsCombiner/1.0'}
    
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

def get_useless_fact():
    data = fetch_data("https://uselessfacts.jsph.pl/api/v2/facts/random")
    return data.get("text", "Could not fetch a fact today.")

def get_kanye_quote():
    data = fetch_data("https://api.kanye.rest/")
    return data.get("quote", "Could not fetch Kanye wisdom.")

def get_dad_joke():
    # Dad joke API requires a specific Accept header for JSON
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 FreeAPIsCombiner/1.0'
    }
    data = fetch_data("https://icanhazdadjoke.com/", headers=headers)
    return data.get("joke", "Could not fetch a dad joke.")

def get_advice():
    # Advice slip API returns text sometimes if we aren't careful, but standard is JSON
    data = fetch_data("https://api.adviceslip.com/advice")
    if "slip" in data:
        return data["slip"].get("advice", "Could not fetch advice.")
    return "Could not fetch advice."

def get_dog_image():
    data = fetch_data("https://dog.ceo/api/breeds/image/random")
    return data.get("message", "Could not fetch a dog image.")

def main():
    print("Fetching your Daily Wisdom & Fun Dashboard...")
    print("-" * 50)
    
    # Fetch all endpoints concurrently to save time
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_fact = executor.submit(get_useless_fact)
        future_kanye = executor.submit(get_kanye_quote)
        future_joke = executor.submit(get_dad_joke)
        future_advice = executor.submit(get_advice)
        future_dog = executor.submit(get_dog_image)

        # Wait for results
        fact = future_fact.result()
        kanye = future_kanye.result()
        joke = future_joke.result()
        advice = future_advice.result()
        dog = future_dog.result()
        
    # Build Dashboard Output
    dashboard = f"""
==================================================
🌟 TODAY'S WISDOM & FUN DASHBOARD 🌟
==================================================

🤔 DID YOU KNOW?
"{fact}"

💡 ADVICE OF THE DAY:
"{advice}"

🎤 KANYE WEST SAYS:
"{kanye}"

🤣 DAD JOKE:
"{joke}"

🐶 DAILY DOG PIC URL to brighten your day:
{dog}

==================================================
    """
    
    print(dashboard)

if __name__ == "__main__":
    main()
