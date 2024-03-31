import requests
import csv
import configparser
import os

# Function to fetch data from NASA API
def fetch_nasa_data(url, params):
    """
    Fetches data from the NASA API.

    Args:
    url (str): The URL of the API endpoint.
    params (dict): Parameters to be passed with the request.

    Returns:
    dict: JSON response from the API.
    """
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data from NASA API. Status code: {response.status_code}")
        return None

# Function to process NASA data
def process_nasa_data(data):
    """
    Processes NASA data to filter out images and their sizes.

    Args:
    data (dict): JSON data received from the NASA API.

    Returns:
    list: List of dictionaries containing NASA ID and image size in KB.
    """
    results = []
    if data:
        for index, item in enumerate(data['collection']['items'], start=1):
            if item['data'][0]['media_type'] == 'image':
                image_url = item['links'][0]['href'].replace("thumb", "orig")
                print(f"Processing image {index}")  # Print the processing message with image index
                image_response = requests.get(image_url, stream=True)
                # convert byte to KB
                image_size_kb = int(image_response.headers.get('content-length', 0)) / 1024
                if image_size_kb > 1000:
                    results.append({
                        'Nasa_id': item['data'][0]['nasa_id'],
                        'kb': image_size_kb
                    })
    return results

# Function to write results to a CSV file
def write_to_csv(results, filename='output.csv'):
    """
    Writes processed NASA data to a CSV file.

    Args:
    results (list): List of dictionaries containing NASA ID and image size in KB.
    filename (str): Name of the output CSV file.
    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Nasa_id', 'kb']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

# Main function to orchestrate the process
def main():
    # Read configuration from external file
    config = configparser.ConfigParser()
    config.read('config.ini')  # Path to your configuration file

    # URL for NASA API request
    url = "https://images-api.nasa.gov/search"

    # Parameters from configuration file or environment variables
    params = {
        'q': config.get('NASA', 'query') if 'NASA' in config else os.environ.get('NASA_QUERY', 'Ilan Ramon')
    }

    # Fetch data from NASA API
    data = fetch_nasa_data(url, params)

    # Process NASA data
    if data:
        results = process_nasa_data(data)
        # Write processed data to CSV
        write_to_csv(results)

# Entry point of the program
if __name__ == "__main__":
    main()
