# MondayAssignment

![image](https://github.com/abd129-0/MondayAssignment/assets/75143506/bdcf979a-add6-4b4c-baae-b57d70c12c9c)

## Q1:NASA Image Search
This Python script queries the NASA image API to search for assets related to "Ilan Ramon". It then filters out images with original file sizes larger than 1000 KB and saves the results to a CSV file.

### Prerequisites

Before running the script, ensure that you have the following:

- Install Python 3, You can download Python from the official website: https://www.python.org/downloads/
- Necessary Python packages installed. You can install them using pip:

    ```
    pip install requests
    ```

    ```
    pip install configparser
    ```


### Usage

1. Navigate to the directory where you want to clone the repository using the cd command:
   ```
   cd /path/to/desired/directory
   ```

2. Clone the repository or download the script directly:
    ```
    git clone https://github.com/abd129-0/MondayAssignment.git
    ```
3. Navigate to the directory containing the script:
    ```
    cd <path>/monday.comHW
    ```

4. Before running the script, make sure to modify the configuration file (`config.ini`) according to your setup.

5. Open a terminal or command prompt.

6. Run the script using the following command:
    ```
    python monday.comHW.py
    ```

7. The script will create a new CSV file in the current directory.

    


### Description

Before running the script, please ensure to modify the configuration path (`config.ini`) accordingly based on your setup. 

The script performs the following steps:

1. Constructs a URL for the NASA image API search endpoint.
2. Sends a GET request to the NASA API with the search parameters.
3. Parses the JSON response to extract relevant image data.
4. Iterates over the items in the response, checking for images and their sizes.
5. Downloads each image to check its size and filters out images larger than 1000 KB.
6. Writes the filtered results to a CSV file named `output1.csv`.


### Example run in AWS EC2 enviroment
1. Clonning the repository:

    ![image](https://github.com/abd129-0/MondayAssignment/assets/75143506/9d31f2b0-5488-47fe-85e9-59752367dbb9)
   
2. Navigating to the directory that containing the script:

    ![image](https://github.com/abd129-0/MondayAssignment/assets/75143506/f0c9b041-ab89-4ac1-85ab-1ce1e22c8587)

3. Running the script:

    ![image](https://github.com/abd129-0/MondayAssignment/assets/75143506/2d41612d-fcae-4495-8848-06423e2f16b8)

4. results :

   ![image](https://github.com/abd129-0/MondayAssignment/assets/75143506/8671b323-78d6-4476-88f3-338914137b7d)

   ![image](https://github.com/abd129-0/MondayAssignment/assets/75143506/29b7c9c4-d250-4cd3-8b17-3245b1c706c2)



### Parameters

- **URL**: The endpoint URL for the NASA image API.
- **Search Parameters**: The script searches for assets related to "Ilan Ramon" using the 'q' parameter.
- **Output File**: The script saves the filtered results to a CSV file named `output.csv`.
  

### Dependencies

- `requests`: Used for sending HTTP requests and handling responses.
- `csv`: Used for reading and writing CSV files.
- `configparser`: Used for parsing configuration files.
- `os`: Provides a portable way to use operating system-dependent functionality.


## Q2 : EC2 & RDS pricing in AWS enviroment
- Q2AWSpricing.pdf file provides guidance on optimizing costs for AWS EC2 and RDS instances by understanding the factors influencing pricing and implementing strategies to reduce and optimize costs.

  ![image](https://github.com/abd129-0/MondayAssignment/assets/75143506/396a7c77-a927-4b0b-8da6-2c4f7bff6aef)
  

  ![image](https://github.com/abd129-0/MondayAssignment/assets/75143506/8b2f4b1e-b488-4edc-93e4-873df98b0d03)



## Author

This script was written by Abdallah Assi.
