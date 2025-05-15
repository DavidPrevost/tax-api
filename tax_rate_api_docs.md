# Tax Rate API Documentation

This API provides access to federal and state marginal tax rates and allows for tax calculations.

## Installation

1. Clone this repository or download the files
2. Install dependencies:
   ```
   pip install flask
   ```
3. Run the server:
   ```
   python app.py
   ```

The server will run on `http://localhost:5000` by default.

## API Endpoints

### Home
- **URL**: `/`
- **Method**: `GET`
- **Response**: Basic information about available endpoints

### Federal Tax Rates
- **URL**: `/api/federal/{year}/{filing_status}`
- **Method**: `GET`
- **URL Parameters**:
  - `year`: The tax year (e.g., "2024")
  - `filing_status`: The filing status (e.g., "single", "married_joint", "head_of_household", "married_separate")
- **Response**: Federal tax brackets for the specified year and filing status

### State Tax Rates
- **URL**: `/api/state/{state_code}/{year}/{filing_status}`
- **Method**: `GET`
- **URL Parameters**:
  - `state_code`: The two-letter state code (e.g., "CA", "NY", "TX")
  - `year`: The tax year (e.g., "2024")
  - `filing_status`: The filing status (e.g., "single")
- **Response**: State tax brackets for the specified state, year, and filing status

### Calculate Federal Tax
- **URL**: `/api/calculate/federal`
- **Method**: `GET`
- **Query Parameters**:
  - `income`: The income amount (required)
  - `year`: The tax year (default: "2024")
  - `filing_status`: The filing status (default: "single")
- **Response**: Calculated federal tax amount and effective tax rate

### Calculate State Tax
- **URL**: `/api/calculate/state`
- **Method**: `GET`
- **Query Parameters**:
  - `state`: The two-letter state code (required)
  - `income`: The income amount (required)
  - `year`: The tax year (default: "2024")
  - `filing_status`: The filing status (default: "single")
- **Response**: Calculated state tax amount and effective tax rate

### Get Available States
- **URL**: `/api/states`
- **Method**: `GET`
- **Response**: List of available state codes

### Get Available Years
- **URL**: `/api/years`
- **Method**: `GET`
- **Response**: List of available years for federal and state tax rates

### Update Federal Tax Rates
- **URL**: `/api/update/federal`
- **Method**: `POST`
- **Request Body**: JSON object containing federal tax rate data
- **Response**: Success message

### Update State Tax Rates
- **URL**: `/api/update/state`
- **Method**: `POST`
- **Request Body**: JSON object containing state tax rate data
- **Response**: Success message

## Example Usage

### Get Federal Tax Rates for Single Filers in 2024
```
GET http://localhost:5000/api/federal/2024/single
```

### Calculate Federal Tax for $75,000 Income
```
GET http://localhost:5000/api/calculate/federal?income=75000&year=2024&filing_status=single
```

### Calculate California State Tax for $75,000 Income
```
GET http://localhost:5000/api/calculate/state?state=CA&income=75000&year=2024&filing_status=single
```

## Data Structure

The API uses JSON files to store tax data:
- `data/federal_tax_rates.json`: Federal tax brackets by year and filing status
- `data/state_tax_rates.json`: State tax brackets by state, year, and filing status

## Adding More Data

You can add more tax years, states, or filing statuses by:
1. Using the update endpoints to add new data
2. Manually editing the JSON files in the `data` directory
