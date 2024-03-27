# MondayAssignment

## Q1:NASA Image Search
This Python script queries the NASA image API to search for assets related to "Ilan Ramon". It then filters out images with original file sizes larger than 1000 KB and saves the results to a CSV file.

### Prerequisites

Before running the script, ensure that you have the following:

- Python installed on your system (version 3.x recommended).
- Necessary Python packages installed. You can install them using pip:

    ```
    pip install requests
    ```

### Usage

1. Clone the repository or download the script directly.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

    ```
    python monday.comHW.py
    ```

### Description

The script performs the following steps:

1. Constructs a URL for the NASA image API search endpoint.
2. Sends a GET request to the NASA API with the search parameters.
3. Parses the JSON response to extract relevant image data.
4. Iterates over the items in the response, checking for images and their sizes.
5. Downloads each image to check its size and filters out images larger than 1000 KB.
6. Writes the filtered results to a CSV file named `output.csv`.

### Parameters

- **URL**: The endpoint URL for the NASA image API.
- **Search Parameters**: The script searches for assets related to "Ilan Ramon" using the 'q' parameter.
- **Output File**: The script saves the filtered results to a CSV file named `output.csv`.

### Dependencies

- `requests`: Used for sending HTTP requests and handling responses.
- `csv`: Used for reading and writing CSV files.

### Notes

- Make sure to replace the `'YOUR_API_KEY'` placeholder with your actual NASA API key.
- The script may take some time to execute depending on the number of images returned by the API and their sizes.
- Ensure you have a stable internet connection while running the script to download images from the NASA API.

## Q2 : EC2 & RDS pricing in AWS enviroment
Q2.pdf fole provides guidance on optimizing costs for AWS EC2 and RDS instances by understanding the factors influencing pricing and implementing strategies to reduce and optimize costs.

## Author

This script was written by Abdallah Assi.
