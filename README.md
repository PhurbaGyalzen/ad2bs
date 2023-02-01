# AD2BS Conversion API

The AD to BS Conversion API Endpoint is a comprehensive tool for converting Nepali Bikram Sambat (BS) dates to Gregorian (AD) dates. With this API endpoint, you can easily and quickly convert any BS date to its corresponding AD date, without the need for complex calculations or manual conversions. The API is highly efficient and accurate, ensuring that the conversions are always precise and reliable. Whether you're working with a large dataset or just need to perform a single conversion, this API endpoint has you covered, providing you with fast and convenient date conversion capabilities at your fingertips.


A fast and reliable API for converting between Nepali Bikram Sambat (BS) and Gregorian (AD) dates.

## Features
- Two-way date conversion between BS and AD
- Accurate and efficient algorithms
- Accepts year, month, and day as body parameters in JSON format
- Fast and convenient date conversion

## Usage
To convert a BS date to an AD date, send a POST request to the API endpoint with the following JSON body parameters:

- year (int)
- month (int)
- day (int)

Example JSON body:

```
{
  "year": 2080,
  "month": 2,
  "day": 29
}
```

Response
The API will return a JSON object with the following fields:
- status: (bool)
- result: (str)

```
{
    "status": true,
    "result": "2023 April 28 Friday"
}
```
Example JSON response:

## Support
For any questions or concerns, please contact the API support team.
