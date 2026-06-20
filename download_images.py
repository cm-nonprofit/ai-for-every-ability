import os, json, urllib.request, urllib.parse, ssl, random

UNSPLASH_API_KEY = 'buhc7QncQ0ZMcCjMWpJhQ-NIiIjmoNeFYE4IyOiCbVA'
ASSETS = 'assets'

ssl_ctx = ssl.create_default_context()


def download_image(query, filename, orientation='landscape'):
    os.makedirs(ASSETS, exist_ok=True)
    try:
        params = urllib.parse.urlencode({'query': query, 'per_page': 10, 'orientation': orientation})
        url = f'https://api.unsplash.com/search/photos?{params}'
        req = urllib.request.Request(url, headers={'Authorization': f'Client-ID {UNSPLASH_API_KEY}'})
        with urllib.request.urlopen(req, context=ssl_ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        if data.get('results'):
            pick = random.choice(data['results'])
            image_url = pick['urls']['regular']
            with urllib.request.urlopen(image_url, context=ssl_ctx, timeout=15) as img_resp:
                img_data = img_resp.read()
            path = os.path.join(ASSETS, filename)
            with open(path, 'wb') as f:
                f.write(img_data)
            print(f"Downloaded: {filename} (query: {query})")
            return True
    except Exception as e:
        print(f"Failed {filename} ({query}): {e}")
    return False


download_image('inclusive classroom assistive technology', 'program1.jpg')
download_image('sign language communication hands', 'program2.jpg')
download_image('parent child therapy session', 'program3.jpg')
download_image('autism sensory friendly room', 'program4.jpg')
download_image('wheelchair accessibility ramp city', 'program5.jpg')
download_image('neural network glowing abstract', 'hero-bg.jpg')
download_image('diverse community gathering smiling', 'impact-bg.jpg')
download_image('hands reaching out support care', 'problem-bg.jpg')

print("Done.")
