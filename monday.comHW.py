import requests
import csv

def fetch_nasa_data(url, params):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data from NASA API. Status code: {response.status_code}")
        return None

def process_nasa_data(data):
    results = []
    if data:
        for item in data['collection']['items']:
            if item['data'][0]['media_type'] == 'image':
                image_url = item['links'][0]['href'].replace("thumb", "orig")
                image_response = requests.get(image_url, stream=True)
                # convert byte to KB
                image_size_kb = int(image_response.headers.get('content-length', 0)) / 1024 
                if image_size_kb > 1000:
                    results.append({
                        'Nasa_id': item['data'][0]['nasa_id'],
                        'kb': image_size_kb
                    })
    return results

def write_to_csv(results, filename='output.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Nasa_id', 'kb']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

def main():
    url = "https://images-api.nasa.gov/search"
    params = {
        'q': 'Ilan Ramon'
    }
    
    data = fetch_nasa_data(url, params)
    if data:
        results = process_nasa_data(data)
        write_to_csv(results)

if __name__ == "__main__":
    main()
