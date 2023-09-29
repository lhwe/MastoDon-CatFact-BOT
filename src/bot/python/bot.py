import time
import requests
from mastodon import Mastodon
mastodon = Mastodon(
    client_id="Ur Client ID",
    client_secret="Ur Secret",
    access_token="Ur token",
    api_base_url="https://wehavecookies.social"
)
while True:
    try:
        response = requests.get("https://catfact.ninja/fact")
        if response.status_code == 200:
            fact_data = response.json()
            randomcatfact = fact_data.get("fact")
            if randomcatfact:
                for countdown in range(15, 0, -1):
                    x = time.strftime("%H:%M:%S", time.localtime(time.time()))
                    countdown_msg = f"[{x}] Cat Fact in {countdown} seconds... "
                    print(countdown_msg)
                    time.sleep(1)
                post = f"Cat Fact: {randomcatfact} ðŸ±\n{x}"
                mastodon.status_post(post)
                print(f"[{x}] Posted a cat-fact!")
    except Exception as e:
        print(f"[{x}] An error occurred: {e}")
