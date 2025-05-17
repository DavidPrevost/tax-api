from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Load tax data from JSON files
def load_tax_data():
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Create tax data if it doesn't exist
    if not os.path.exists('data/tax_rates.json'):
        tax_data = {
            "2024": {
                "US": {
                    "single": [
                        {"threshold": 11000, "rate": 0.10},
                        {"threshold": 44725, "rate": 0.12},
                        {"threshold": 95375, "rate": 0.22},
                        {"threshold": 182100, "rate": 0.24},
                        {"threshold": 231250, "rate": 0.32},
                        {"threshold": 578125, "rate": 0.35},
                        {"threshold": 999999999, "rate": 0.37}
                    ],
                    "married_joint": [
                        {"threshold": 22000, "rate": 0.10},
                        {"threshold": 89450, "rate": 0.12},
                        {"threshold": 190750, "rate": 0.22},
                        {"threshold": 364200, "rate": 0.24},
                        {"threshold": 462500, "rate": 0.32},
                        {"threshold": 693750, "rate": 0.35},
                        {"threshold": 999999999, "rate": 0.37}
                    ],
                    "head_of_household": [
                        {"threshold": 15700, "rate": 0.10},
                        {"threshold": 59850, "rate": 0.12},
                        {"threshold": 95350, "rate": 0.22},
                        {"threshold": 182100, "rate": 0.24},
                        {"threshold": 231250, "rate": 0.32},
                        {"threshold": 578100, "rate": 0.35},
                        {"threshold": 999999999, "rate": 0.37}
                    ],
                    "married_separate": [
                        {"threshold": 11000, "rate": 0.10},
                        {"threshold": 44725, "rate": 0.12},
                        {"threshold": 95375, "rate": 0.22},
                        {"threshold": 182100, "rate": 0.24},
                        {"threshold": 231250, "rate": 0.32},
                        {"threshold": 346875, "rate": 0.35},
                        {"threshold": 999999999, "rate": 0.37}
                    ]
                },
                "AL": {
                    "note": "Alabama has a flat tax rate",
                    "single": [
                        {"threshold": 999999999, "rate": 0.05}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.05}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.05}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.05}
                    ]
                },
                "AK": {
                    "note": "Alaska has no state income tax",
                    "single": [
                        {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.0}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.0}
                    ]
                },
                "AZ": {
                    "single": [
                        {"threshold": 28653, "rate": 0.0259},
                        {"threshold": 57305, "rate": 0.0334},
                        {"threshold": 171911, "rate": 0.0417},
                        {"threshold": 999999999, "rate": 0.045}
                    ],
                    "married_joint": [
                        {"threshold": 57305, "rate": 0.0259},
                        {"threshold": 114610, "rate": 0.0334},
                        {"threshold": 343821, "rate": 0.0417},
                        {"threshold": 999999999, "rate": 0.045}
                    ],
                    "head_of_household": [
                        {"threshold": 28653, "rate": 0.0259},
                        {"threshold": 57305, "rate": 0.0334},
                        {"threshold": 171911, "rate": 0.0417},
                        {"threshold": 999999999, "rate": 0.045}
                    ],
                    "married_separate": [
                        {"threshold": 28653, "rate": 0.0259},
                        {"threshold": 57305, "rate": 0.0334},
                        {"threshold": 171911, "rate": 0.0417},
                        {"threshold": 999999999, "rate": 0.045}
                    ]
                },
                "AR": {
                    "note": "Arkansas has adjusted its rates for 2024",
                    "single": [
                        {"threshold": 4300, "rate": 0.02},
                        {"threshold": 8500, "rate": 0.04},
                        {"threshold": 999999999, "rate": 0.049}
                    ],
                    "married_joint": [
                        {"threshold": 4300, "rate": 0.02},
                        {"threshold": 8500, "rate": 0.04},
                        {"threshold": 999999999, "rate": 0.049}
                    ],
                    "head_of_household": [
                        {"threshold": 4300, "rate": 0.02},
                        {"threshold": 8500, "rate": 0.04},
                        {"threshold": 999999999, "rate": 0.049}
                    ],
                    "married_separate": [
                        {"threshold": 4300, "rate": 0.02},
                        {"threshold": 8500, "rate": 0.04},
                        {"threshold": 999999999, "rate": 0.049}
                    ]
                },
                "CA": {
                    "single": [
                        {"threshold": 10099, "rate": 0.01},
                        {"threshold": 23942, "rate": 0.02},
                        {"threshold": 37788, "rate": 0.04},
                        {"threshold": 52455, "rate": 0.06},
                        {"threshold": 66295, "rate": 0.08},
                        {"threshold": 338639, "rate": 0.093},
                        {"threshold": 406364, "rate": 0.103},
                        {"threshold": 677275, "rate": 0.113},
                        {"threshold": 1000000, "rate": 0.123},
                        {"threshold": 999999999, "rate": 0.133}
                    ],
                    "married_joint": [
                        {"threshold": 20198, "rate": 0.01},
                        {"threshold": 47884, "rate": 0.02},
                        {"threshold": 75576, "rate": 0.04},
                        {"threshold": 104910, "rate": 0.06},
                        {"threshold": 132590, "rate": 0.08},
                        {"threshold": 677278, "rate": 0.093},
                        {"threshold": 812728, "rate": 0.103},
                        {"threshold": 1354550, "rate": 0.113},
                        {"threshold": 2000000, "rate": 0.123},
                        {"threshold": 999999999, "rate": 0.133}
                    ],
                    "head_of_household": [
                        {"threshold": 20198, "rate": 0.01},
                        {"threshold": 47884, "rate": 0.02},
                        {"threshold": 61730, "rate": 0.04},
                        {"threshold": 76397, "rate": 0.06},
                        {"threshold": 90237, "rate": 0.08},
                        {"threshold": 460547, "rate": 0.093},
                        {"threshold": 552658, "rate": 0.103},
                        {"threshold": 921095, "rate": 0.113},
                        {"threshold": 1000000, "rate": 0.123},
                        {"threshold": 999999999, "rate": 0.133}
                    ],
                    "married_separate": [
                        {"threshold": 10099, "rate": 0.01},
                        {"threshold": 23942, "rate": 0.02},
                        {"threshold": 37788, "rate": 0.04},
                        {"threshold": 52455, "rate": 0.06},
                        {"threshold": 66295, "rate": 0.08},
                        {"threshold": 338639, "rate": 0.093},
                        {"threshold": 406364, "rate": 0.103},
                        {"threshold": 677275, "rate": 0.113},
                        {"threshold": 1000000, "rate": 0.123},
                        {"threshold": 999999999, "rate": 0.133}
                    ]
                },
                "CO": {
                    "note": "Colorado has a flat tax rate",
                    "single": [
                        {"threshold": 999999999, "rate": 0.0443}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.0443}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.0443}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.0443}
                    ]
                },
                "CT": {
                    "single": [
                        {"threshold": 10000, "rate": 0.03},
                        {"threshold": 50000, "rate": 0.05},
                        {"threshold": 100000, "rate": 0.055},
                        {"threshold": 200000, "rate": 0.06},
                        {"threshold": 250000, "rate": 0.065},
                        {"threshold": 500000, "rate": 0.069},
                        {"threshold": 999999999, "rate": 0.0699}
                    ],
                    "married_joint": [
                        {"threshold": 20000, "rate": 0.03},
                        {"threshold": 100000, "rate": 0.05},
                        {"threshold": 200000, "rate": 0.055},
                        {"threshold": 400000, "rate": 0.06},
                        {"threshold": 500000, "rate": 0.065},
                        {"threshold": 1000000, "rate": 0.069},
                        {"threshold": 999999999, "rate": 0.0699}
                    ],
                    "head_of_household": [
                        {"threshold": 16000, "rate": 0.03},
                        {"threshold": 80000, "rate": 0.05},
                        {"threshold": 160000, "rate": 0.055},
                        {"threshold": 320000, "rate": 0.06},
                        {"threshold": 400000, "rate": 0.065},
                        {"threshold": 800000, "rate": 0.069},
                        {"threshold": 999999999, "rate": 0.0699}
                    ],
                    "married_separate": [
                        {"threshold": 10000, "rate": 0.03},
                        {"threshold": 50000, "rate": 0.05},
                        {"threshold": 100000, "rate": 0.055},
                        {"threshold": 200000, "rate": 0.06},
                        {"threshold": 250000, "rate": 0.065},
                        {"threshold": 500000, "rate": 0.069},
                        {"threshold": 999999999, "rate": 0.0699}
                    ]
                },
                "DE": {
                    "single": [
                        {"threshold": 2000, "rate": 0.0},
                        {"threshold": 5000, "rate": 0.022},
                        {"threshold": 10000, "rate": 0.039},
                        {"threshold": 20000, "rate": 0.048},
                        {"threshold": 25000, "rate": 0.052},
                        {"threshold": 60000, "rate": 0.055},
                        {"threshold": 999999999, "rate": 0.066}
                    ],
                    "married_joint": [
                        {"threshold": 2000, "rate": 0.0},
                        {"threshold": 5000, "rate": 0.022},
                        {"threshold": 10000, "rate": 0.039},
                        {"threshold": 20000, "rate": 0.048},
                        {"threshold": 25000, "rate": 0.052},
                        {"threshold": 60000, "rate": 0.055},
                        {"threshold": 999999999, "rate": 0.066}
                    ],
                    "head_of_household": [
                        {"threshold": 2000, "rate": 0.0},
                        {"threshold": 5000, "rate": 0.022},
                        {"threshold": 10000, "rate": 0.039},
                        {"threshold": 20000, "rate": 0.048},
                        {"threshold": 25000, "rate": 0.052},
                        {"threshold": 60000, "rate": 0.055},
                        {"threshold": 999999999, "rate": 0.066}
                    ],
                    "married_separate": [
                        {"threshold": 2000, "rate": 0.0},
                        {"threshold": 5000, "rate": 0.022},
                        {"threshold": 10000, "rate": 0.039},
                        {"threshold": 20000, "rate": 0.048},
                        {"threshold": 25000, "rate": 0.052},
                        {"threshold": 60000, "rate": 0.055},
                        {"threshold": 999999999, "rate": 0.066}
                    ]
                },
                "DC": {
                    "single": [
                        {"threshold": 10000, "rate": 0.04},
                        {"threshold": 40000, "rate": 0.06},
                        {"threshold": 60000, "rate": 0.065},
                        {"threshold": 350000, "rate": 0.085},
                        {"threshold": 1000000, "rate": 0.0925},
                        {"threshold": 999999999, "rate": 0.0975}
                    ],
                    "married_joint": [
                        {"threshold": 10000, "rate": 0.04},
                        {"threshold": 40000, "rate": 0.06},
                        {"threshold": 60000, "rate": 0.065},
                        {"threshold": 350000, "rate": 0.085},
                        {"threshold": 1000000, "rate": 0.0925},
                        {"threshold": 999999999, "rate": 0.0975}
                    ],
                    "head_of_household": [
                        {"threshold": 10000, "rate": 0.04},
                        {"threshold": 40000, "rate": 0.06},
                        {"threshold": 60000, "rate": 0.065},
                        {"threshold": 350000, "rate": 0.085},
                        {"threshold": 1000000, "rate": 0.0925},
                        {"threshold": 999999999, "rate": 0.0975}
                    ],
                    "married_separate": [
                        {"threshold": 10000, "rate": 0.04},
                        {"threshold": 40000, "rate": 0.06},
                        {"threshold": 60000, "rate": 0.065},
                        {"threshold": 350000, "rate": 0.085},
                        {"threshold": 1000000, "rate": 0.0925},
                        {"threshold": 999999999, "rate": 0.0975}
                    ]
                },
                "FL": {
                    "note": "Florida has no state income tax",
                    "single": [
                        {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.0}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.0}
                    ]
                },
                "GA": {
                    "note": "Georgia has a flat tax rate",
                    "single": [
                        {"threshold": 999999999, "rate": 0.0555}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.0555}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.0555}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.0555}
                    ]
                },
                "HI": {
                    "single": [
                        {"threshold": 2400, "rate": 0.014},
                        {"threshold": 4800, "rate": 0.032},
                        {"threshold": 9600, "rate": 0.055},
                        {"threshold": 14400, "rate": 0.064},
                        {"threshold": 19200, "rate": 0.068},
                        {"threshold": 24000, "rate": 0.072},
                        {"threshold": 36000, "rate": 0.076},
                        {"threshold": 48000, "rate": 0.079},
                        {"threshold": 150000, "rate": 0.0825},
                        {"threshold": 175000, "rate": 0.09},
                        {"threshold": 200000, "rate": 0.10},
                        {"threshold": 999999999, "rate": 0.11}
                    ],
                    "married_joint": [
                        {"threshold": 4800, "rate": 0.014},
                        {"threshold": 9600, "rate": 0.032},
                        {"threshold": 19200, "rate": 0.055},
                        {"threshold": 28800, "rate": 0.064},
                        {"threshold": 38400, "rate": 0.068},
                        {"threshold": 48000, "rate": 0.072},
                        {"threshold": 72000, "rate": 0.076},
                        {"threshold": 96000, "rate": 0.079},
                        {"threshold": 300000, "rate": 0.0825},
                        {"threshold": 350000, "rate": 0.09},
                        {"threshold": 400000, "rate": 0.10},
                        {"threshold": 999999999, "rate": 0.11}
                    ],
                    "head_of_household": [
                        {"threshold": 3600, "rate": 0.014},
                        {"threshold": 7200, "rate": 0.032},
                        {"threshold": 14400, "rate": 0.055},
                        {"threshold": 21600, "rate": 0.064},
                        {"threshold": 28800, "rate": 0.068},
                        {"threshold": 36000, "rate": 0.072},
                        {"threshold": 54000, "rate": 0.076},
                        {"threshold": 72000, "rate": 0.079},
                        {"threshold": 225000, "rate": 0.0825},
                        {"threshold": 262500, "rate": 0.09},
                        {"threshold": 300000, "rate": 0.10},
                        {"threshold": 999999999, "rate": 0.11}
                    ],
                    "married_separate": [
                        {"threshold": 2400, "rate": 0.014},
                        {"threshold": 4800, "rate": 0.032},
                        {"threshold": 9600, "rate": 0.055},
                        {"threshold": 14400, "rate": 0.064},
                        {"threshold": 19200, "rate": 0.068},
                        {"threshold": 24000, "rate": 0.072},
                        {"threshold": 36000, "rate": 0.076},
                        {"threshold": 48000, "rate": 0.079},
                        {"threshold": 150000, "rate": 0.0825},
                        {"threshold": 175000, "rate": 0.09},
                        {"threshold": 200000, "rate": 0.10},
                        {"threshold": 999999999, "rate": 0.11}
                    ]
                },
                "ID": {
                    "note": "Idaho has a flat tax rate",
                    "single": [
                        {"threshold": 999999999, "rate": 0.059}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.059}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.059}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.059}
                    ]
                },
                "IL": {
                    "note": "Illinois has a flat tax rate",
                    "single": [
                        {"threshold": 999999999, "rate": 0.0495}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.0495}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.0495}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.0495}
                    ]
                },
                "IN": {
                    "note": "Indiana has a flat tax rate",
                    "single": [
                        {"threshold": 999999999, "rate": 0.0323}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.0323}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.0323}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.0323}
                    ]
                },
                "IA": {
                    "note": "Iowa has a flat tax rate",
                    "single": [
                        {"threshold": 999999999, "rate": 0.0375}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.0375}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.0375}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.0375}
                    ]
                },
                "KS": {
                    "single": [
                        {"threshold": 15000, "rate": 0.031},
                        {"threshold": 30000, "rate": 0.0525},
                        {"threshold": 999999999, "rate": 0.057}
                    ],
                    "married_joint": [
                        {"threshold": 30000, "rate": 0.031},
                        {"threshold": 60000, "rate": 0.0525},
                        {"threshold": 999999999, "rate": 0.057}
                    ],
                    "head_of_household": [
                        {"threshold": 20000, "rate": 0.031},
                        {"threshold": 40000, "rate": 0.0525},
                        {"threshold": 999999999, "rate": 0.057}
                    ],
                    "married_separate": [
                        {"threshold": 15000, "rate": 0.031},
                        {"threshold": 30000, "rate": 0.0525},
                        {"threshold": 999999999, "rate": 0.057}
                    ]
                },
                "KY": {
                    "note": "Kentucky has a flat tax rate",
                    "single": [
                        {"threshold": 999999999, "rate": 0.044}
                    ],
                    "married_joint": [
                        {"threshold": 999999999, "rate": 0.044}
                    ],
                    "head_of_household": [
                        {"threshold": 999999999, "rate": 0.044}
                    ],
                    "married_separate": [
                        {"threshold": 999999999, "rate": 0.044}
                    ]
                },
                "LA": {
                    "single": [
                        {"threshold": 12500, "rate": 0.0185},
                        {"threshold": 50000, "rate": 0.035},
                        {"threshold": 999999999, "rate": 0.0425}
                    ],
                    "married_joint": [
                        {"threshold": 25000, "rate": 0.0185},
                        {"threshold": 100000, "rate": 0.035},
                        {"threshold": 999999999, "rate": 0.0425}
                    ],
                    "head_of_household": [
                        {"threshold": 12500, "rate": 0.0185},
                        {"threshold": 50000, "rate": 0.035},
                        {"threshold": 999999999, "rate": 0.0425}
                    ],
                    "married_separate": [
                        {"threshold": 12500, "rate": 0.0185},
                        {"threshold": 50000, "rate": 0.035},
                        {"threshold": 999999999, "rate": 0.0425}
                    ]
                },
                "ME": {
                    "single": [
                        {"threshold": 24500, "rate": 0.058},
                        {"threshold": 58050, "rate": 0.0675},
                        {"threshold": 999999999, "rate": 0.0715}
                    ],
                    "married_joint": [
                        {"threshold": 49000, "rate": 0.058},
                        {"threshold": 116100, "rate": 0.0675},
                        {"threshold": 999999999, "rate": 0.0715}
                    ],
                    "head_of_household": [
                        {"threshold": 36750, "rate": 0.058},
                        {"threshold": 87050, "rate": 0.0675},
                        {"threshold": 999999999, "rate": 0.0715}
                    ],
                    "married_separate": [
                        {"threshold": 24500, "rate": 0.058},
                        {"threshold": 58050, "rate": 0.0675},
                        {"threshold": 999999999, "rate": 0.0715}
                    ]
                },
                "MD": {
                    "single": [
                        {"threshold": 1000, "rate": 0.02},
                        {"threshold": 2000, "rate": 0.03},
                        {"threshold": 3000, "rate": 0.04},
                        {"threshold": 100000, "rate": 0.0475},
                        {"threshold": 125000, "rate": 0.05},
                        {"threshold": 150000, "rate": 0.0525},
                        {"threshold": 250000, "rate": 0.055},
                        {"threshold": 999999999, "rate": 0.0575}
                    ],
                    "married_joint": [
                        {"threshold": 1000, "rate": 0.02},
                        {"threshold": 2000, "rate": 0.03},
                        {"threshold": 3000, "rate": 0.04},
                        {"threshold": 150000, "rate": 0.0475},
                        {"threshold": 175000, "rate": 0.05},
                        {"threshold": 225000, "rate": 0.0525},
                        {"threshold": 300000, "rate": 0.055},
                        {"threshold": 999999999, "rate": 0.0575}
                    ],
                    "head_of_household": [
                        {"threshold": 1000, "rate": 0.02},
                        {"threshold": 2000, "rate": 0.03},
                        {"threshold": 3000, "rate": 0.04},
                        {"threshold": 125000, "rate": 0.0475},
                        {"threshold": 150000, "rate": 0.05},
                        {"threshold": 175000, "rate": 0.0525},
                        {"threshold": 250000, "rate": 0.055},
                        {"threshold": 999999999, "rate": 0.0575}
                    ],
                    "married_separate": [
                        {"threshold": 1000, "rate": 0.02},
                        {"threshold": 2000, "rate": 0.03},
                        {"threshold": 3000, "rate": 0.04},
                        {"threshold": 100000, "rate": 0.0475},
                        {"threshold": 125000, "rate": 0.05},
                        {"threshold": 150000, "rate": 0.0525},
                        {"threshold": 250000, "rate": 0.055},
                        {"threshold": 999999999, "rate": 0.0575}
                    ]
                },
                "MA": {
                    "single": [
                    {"threshold": 8700, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ],
                    "married_joint": [
                    {"threshold": 17400, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ],
                    "head_of_household": [
                    {"threshold": 13050, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ],
                    "married_separate": [
                    {"threshold": 8700, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ]
                },
                "MD": {
                    "single": [
                    {"threshold": 1000, "rate": 0.02},
                    {"threshold": 2000, "rate": 0.03},
                    {"threshold": 3000, "rate": 0.04},
                    {"threshold": 100000, "rate": 0.0475},
                    {"threshold": 125000, "rate": 0.05},
                    {"threshold": 150000, "rate": 0.0525},
                    {"threshold": 250000, "rate": 0.055},
                    {"threshold": 999999999, "rate": 0.0575}
                    ],
                    "married_joint": [
                    {"threshold": 1000, "rate": 0.02},
                    {"threshold": 2000, "rate": 0.03},
                    {"threshold": 3000, "rate": 0.04},
                    {"threshold": 150000, "rate": 0.0475},
                    {"threshold": 175000, "rate": 0.05},
                    {"threshold": 225000, "rate": 0.0525},
                    {"threshold": 300000, "rate": 0.055},
                    {"threshold": 999999999, "rate": 0.0575}
                    ],
                    "head_of_household": [
                    {"threshold": 1000, "rate": 0.02},
                    {"threshold": 2000, "rate": 0.03},
                    {"threshold": 3000, "rate": 0.04},
                    {"threshold": 150000, "rate": 0.0475},
                    {"threshold": 175000, "rate": 0.05},
                    {"threshold": 225000, "rate": 0.0525},
                    {"threshold": 300000, "rate": 0.055},
                    {"threshold": 999999999, "rate": 0.0575}
                    ],
                    "married_separate": [
                    {"threshold": 1000, "rate": 0.02},
                    {"threshold": 2000, "rate": 0.03},
                    {"threshold": 3000, "rate": 0.04},
                    {"threshold": 100000, "rate": 0.0475},
                    {"threshold": 125000, "rate": 0.05},
                    {"threshold": 150000, "rate": 0.0525},
                    {"threshold": 250000, "rate": 0.055},
                    {"threshold": 999999999, "rate": 0.0575}
                    ]
                },
                "ME": {
                    "single": [
                    {"threshold": 23000, "rate": 0.058},
                    {"threshold": 54450, "rate": 0.0675},
                    {"threshold": 999999999, "rate": 0.0715}
                    ],
                    "married_joint": [
                    {"threshold": 46000, "rate": 0.058},
                    {"threshold": 108900, "rate": 0.0675},
                    {"threshold": 999999999, "rate": 0.0715}
                    ],
                    "head_of_household": [
                    {"threshold": 34500, "rate": 0.058},
                    {"threshold": 81700, "rate": 0.0675},
                    {"threshold": 999999999, "rate": 0.0715}
                    ],
                    "married_separate": [
                    {"threshold": 23000, "rate": 0.058},
                    {"threshold": 54450, "rate": 0.0675},
                    {"threshold": 999999999, "rate": 0.0715}
                    ]
                },
                "MI": {
                    "single": [
                    {"threshold": 0, "rate": 0.0425},
                    {"threshold": 999999999, "rate": 0.0425}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.0425},
                    {"threshold": 999999999, "rate": 0.0425}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.0425},
                    {"threshold": 999999999, "rate": 0.0425}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.0425},
                    {"threshold": 999999999, "rate": 0.0425}
                    ]
                },
                "MN": {
                    "single": [
                    {"threshold": 28080, "rate": 0.0535},
                    {"threshold": 92230, "rate": 0.068},
                    {"threshold": 171220, "rate": 0.0785},
                    {"threshold": 999999999, "rate": 0.0985}
                    ],
                    "married_joint": [
                    {"threshold": 41050, "rate": 0.0535},
                    {"threshold": 163060, "rate": 0.068},
                    {"threshold": 284810, "rate": 0.0785},
                    {"threshold": 999999999, "rate": 0.0985}
                    ],
                    "head_of_household": [
                    {"threshold": 34570, "rate": 0.0535},
                    {"threshold": 138890, "rate": 0.068},
                    {"threshold": 227600, "rate": 0.0785},
                    {"threshold": 999999999, "rate": 0.0985}
                    ],
                    "married_separate": [
                    {"threshold": 20530, "rate": 0.0535},
                    {"threshold": 81530, "rate": 0.068},
                    {"threshold": 142410, "rate": 0.0785},
                    {"threshold": 999999999, "rate": 0.0985}
                    ]
                },
                "MO": {
                    "single": [
                    {"threshold": 1088, "rate": 0.015},
                    {"threshold": 2176, "rate": 0.02},
                    {"threshold": 3264, "rate": 0.025},
                    {"threshold": 4352, "rate": 0.03},
                    {"threshold": 5440, "rate": 0.035},
                    {"threshold": 6528, "rate": 0.04},
                    {"threshold": 7616, "rate": 0.045},
                    {"threshold": 8704, "rate": 0.05},
                    {"threshold": 9792, "rate": 0.055},
                    {"threshold": 999999999, "rate": 0.055}
                    ],
                    "married_joint": [
                    {"threshold": 1088, "rate": 0.015},
                    {"threshold": 2176, "rate": 0.02},
                    {"threshold": 3264, "rate": 0.025},
                    {"threshold": 4352, "rate": 0.03},
                    {"threshold": 5440, "rate": 0.035},
                    {"threshold": 6528, "rate": 0.04},
                    {"threshold": 7616, "rate": 0.045},
                    {"threshold": 8704, "rate": 0.05},
                    {"threshold": 9792, "rate": 0.055},
                    {"threshold": 999999999, "rate": 0.055}
                    ],
                    "head_of_household": [
                    {"threshold": 1088, "rate": 0.015},
                    {"threshold": 2176, "rate": 0.02},
                    {"threshold": 3264, "rate": 0.025},
                    {"threshold": 4352, "rate": 0.03},
                    {"threshold": 5440, "rate": 0.035},
                    {"threshold": 6528, "rate": 0.04},
                    {"threshold": 7616, "rate": 0.045},
                    {"threshold": 8704, "rate": 0.05},
                    {"threshold": 9792, "rate": 0.055},
                    {"threshold": 999999999, "rate": 0.055}
                    ],
                    "married_separate": [
                    {"threshold": 1088, "rate": 0.015},
                    {"threshold": 2176, "rate": 0.02},
                    {"threshold": 3264, "rate": 0.025},
                    {"threshold": 4352, "rate": 0.03},
                    {"threshold": 5440, "rate": 0.035},
                    {"threshold": 6528, "rate": 0.04},
                    {"threshold": 7616, "rate": 0.045},
                    {"threshold": 8704, "rate": 0.05},
                    {"threshold": 9792, "rate": 0.055},
                    {"threshold": 999999999, "rate": 0.055}
                    ]
                },
                "MS": {
                    "single": [
                    {"threshold": 5000, "rate": 0.04},
                    {"threshold": 10000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ],
                    "married_joint": [
                    {"threshold": 5000, "rate": 0.04},
                    {"threshold": 10000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ],
                    "head_of_household": [
                    {"threshold": 5000, "rate": 0.04},
                    {"threshold": 10000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ],
                    "married_separate": [
                    {"threshold": 5000, "rate": 0.04},
                    {"threshold": 10000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ]
                },
                "MT": {
                    "single": [
                    {"threshold": 3100, "rate": 0.01},
                    {"threshold": 5500, "rate": 0.02},
                    {"threshold": 8400, "rate": 0.03},
                    {"threshold": 11400, "rate": 0.04},
                    {"threshold": 14600, "rate": 0.05},
                    {"threshold": 18800, "rate": 0.06},
                    {"threshold": 999999999, "rate": 0.0675}
                    ],
                    "married_joint": [
                    {"threshold": 3100, "rate": 0.01},
                    {"threshold": 5500, "rate": 0.02},
                    {"threshold": 8400, "rate": 0.03},
                    {"threshold": 11400, "rate": 0.04},
                    {"threshold": 14600, "rate": 0.05},
                    {"threshold": 18800, "rate": 0.06},
                    {"threshold": 999999999, "rate": 0.0675}
                    ],
                    "head_of_household": [
                    {"threshold": 3100, "rate": 0.01},
                    {"threshold": 5500, "rate": 0.02},
                    {"threshold": 8400, "rate": 0.03},
                    {"threshold": 11400, "rate": 0.04},
                    {"threshold": 14600, "rate": 0.05},
                    {"threshold": 18800, "rate": 0.06},
                    {"threshold": 999999999, "rate": 0.0675}
                    ],
                    "married_separate": [
                    {"threshold": 3100, "rate": 0.01},
                    {"threshold": 5500, "rate": 0.02},
                    {"threshold": 8400, "rate": 0.03},
                    {"threshold": 11400, "rate": 0.04},
                    {"threshold": 14600, "rate": 0.05},
                    {"threshold": 18800, "rate": 0.06},
                    {"threshold": 999999999, "rate": 0.0675}
                    ]
                },
                "NC": {
                    "single": [
                    {"threshold": 0, "rate": 0.0499},
                    {"threshold": 999999999, "rate": 0.0499}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.0499},
                    {"threshold": 999999999, "rate": 0.0499}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.0499},
                    {"threshold": 999999999, "rate": 0.0499}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.0499},
                    {"threshold": 999999999, "rate": 0.0499}
                    ]
                },
                "ND": {
                    "single": [
                    {"threshold": 40525, "rate": 0.011},
                    {"threshold": 98100, "rate": 0.0204},
                    {"threshold": 204675, "rate": 0.0227},
                    {"threshold": 445000, "rate": 0.0264},
                    {"threshold": 999999999, "rate": 0.029}
                    ],
                    "married_joint": [
                    {"threshold": 67700, "rate": 0.011},
                    {"threshold": 163550, "rate": 0.0204},
                    {"threshold": 249150, "rate": 0.0227},
                    {"threshold": 445000, "rate": 0.0264},
                    {"threshold": 999999999, "rate": 0.029}
                    ],
                    "head_of_household": [
                    {"threshold": 54200, "rate": 0.011},
                    {"threshold": 139050, "rate": 0.0204},
                    {"threshold": 226800, "rate": 0.0227},
                    {"threshold": 445000, "rate": 0.0264},
                    {"threshold": 999999999, "rate": 0.029}
                    ],
                    "married_separate": [
                    {"threshold": 33850, "rate": 0.011},
                    {"threshold": 81775, "rate": 0.0204},
                    {"threshold": 124575, "rate": 0.0227},
                    {"threshold": 222500, "rate": 0.0264},
                    {"threshold": 999999999, "rate": 0.029}
                    ]
                },
                "NE": {
                    "single": [
                    {"threshold": 3340, "rate": 0.0246},
                    {"threshold": 19990, "rate": 0.0351},
                    {"threshold": 32210, "rate": 0.0501},
                    {"threshold": 999999999, "rate": 0.0684}
                    ],
                    "married_joint": [
                    {"threshold": 6660, "rate": 0.0246},
                    {"threshold": 39990, "rate": 0.0351},
                    {"threshold": 64430, "rate": 0.0501},
                    {"threshold": 999999999, "rate": 0.0684}
                    ],
                    "head_of_household": [
                    {"threshold": 6220, "rate": 0.0246},
                    {"threshold": 31830, "rate": 0.0351},
                    {"threshold": 64430, "rate": 0.0501},
                    {"threshold": 999999999, "rate": 0.0684}
                    ],
                    "married_separate": [
                    {"threshold": 3340, "rate": 0.0246},
                    {"threshold": 19990, "rate": 0.0351},
                    {"threshold": 32210, "rate": 0.0501},
                    {"threshold": 999999999, "rate": 0.0684}
                    ]
                },
                "NH": {
                    "single": [
                    {"threshold": 0, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.05}
                    ]
                },
                "NJ": {
                    "single": [
                    {"threshold": 20000, "rate": 0.014},
                    {"threshold": 35000, "rate": 0.0175},
                    {"threshold": 40000, "rate": 0.035},
                    {"threshold": 75000, "rate": 0.05525},
                    {"threshold": 500000, "rate": 0.0637},
                    {"threshold": 1000000, "rate": 0.0897},
                    {"threshold": 999999999, "rate": 0.1075}
                    ],
                    "married_joint": [
                    {"threshold": 20000, "rate": 0.014},
                    {"threshold": 50000, "rate": 0.0175},
                    {"threshold": 70000, "rate": 0.0245},
                    {"threshold": 80000, "rate": 0.035},
                    {"threshold": 150000, "rate": 0.05525},
                    {"threshold": 500000, "rate": 0.0637},
                    {"threshold": 1000000, "rate": 0.0897},
                    {"threshold": 999999999, "rate": 0.1075}
                    ],
                    "head_of_household": [
                    {"threshold": 20000, "rate": 0.014},
                    {"threshold": 50000, "rate": 0.0175},
                    {"threshold": 70000, "rate": 0.0245},
                    {"threshold": 80000, "rate": 0.035},
                    {"threshold": 150000, "rate": 0.05525},
                    {"threshold": 500000, "rate": 0.0637},
                    {"threshold": 1000000, "rate": 0.0897},
                    {"threshold": 999999999, "rate": 0.1075}
                    ],
                    "married_separate": [
                    {"threshold": 20000, "rate": 0.014},
                    {"threshold": 35000, "rate": 0.0175},
                    {"threshold": 40000, "rate": 0.035},
                    {"threshold": 75000, "rate": 0.05525},
                    {"threshold": 500000, "rate": 0.0637},
                    {"threshold": 1000000, "rate": 0.0897},
                    {"threshold": 999999999, "rate": 0.1075}
                    ]
                },
                "NM": {
                    "single": [
                    {"threshold": 5500, "rate": 0.017},
                    {"threshold": 11000, "rate": 0.032},
                    {"threshold": 16000, "rate": 0.047},
                    {"threshold": 210000, "rate": 0.049},
                    {"threshold": 999999999, "rate": 0.059}
                    ],
                    "married_joint": [
                    {"threshold": 8000, "rate": 0.017},
                    {"threshold": 16000, "rate": 0.032},
                    {"threshold": 24000, "rate": 0.047},
                    {"threshold": 315000, "rate": 0.049},
                    {"threshold": 999999999, "rate": 0.059}
                    ],
                    "head_of_household": [
                    {"threshold": 8000, "rate": 0.017},
                    {"threshold": 16000, "rate": 0.032},
                    {"threshold": 24000, "rate": 0.047},
                    {"threshold": 315000, "rate": 0.049},
                    {"threshold": 999999999, "rate": 0.059}
                    ],
                    "married_separate": [
                    {"threshold": 4000, "rate": 0.017},
                    {"threshold": 8000, "rate": 0.032},
                    {"threshold": 12000, "rate": 0.047},
                    {"threshold": 157500, "rate": 0.049},
                    {"threshold": 999999999, "rate": 0.059}
                    ]
                },
                "NV": {
                    "single": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ]
                },
                "NY": {
                    "single": [
                    {"threshold": 8500, "rate": 0.04},
                    {"threshold": 11700, "rate": 0.045},
                    {"threshold": 13900, "rate": 0.0525},
                    {"threshold": 80650, "rate": 0.0585},
                    {"threshold": 215400, "rate": 0.0625},
                    {"threshold": 1077550, "rate": 0.0685},
                    {"threshold": 5000000, "rate": 0.0965},
                    {"threshold": 25000000, "rate": 0.103},
                    {"threshold": 999999999, "rate": 0.109}
                    ],
                    "married_joint": [
                    {"threshold": 17150, "rate": 0.04},
                    {"threshold": 23600, "rate": 0.045},
                    {"threshold": 27900, "rate": 0.0525},
                    {"threshold": 161550, "rate": 0.0585},
                    {"threshold": 323200, "rate": 0.0625},
                    {"threshold": 2155350, "rate": 0.0685},
                    {"threshold": 5000000, "rate": 0.0965},
                    {"threshold": 25000000, "rate": 0.103},
                    {"threshold": 999999999, "rate": 0.109}
                    ],
                    "head_of_household": [
                    {"threshold": 12800, "rate": 0.04},
                    {"threshold": 17650, "rate": 0.045},
                    {"threshold": 20900, "rate": 0.0525},
                    {"threshold": 107650, "rate": 0.0585},
                    {"threshold": 269300, "rate": 0.0625},
                    {"threshold": 1616450, "rate": 0.0685},
                    {"threshold": 5000000, "rate": 0.0965},
                    {"threshold": 25000000, "rate": 0.103},
                    {"threshold": 999999999, "rate": 0.109}
                    ],
                    "married_separate": [
                    {"threshold": 8500, "rate": 0.04},
                    {"threshold": 11700, "rate": 0.045},
                    {"threshold": 13900, "rate": 0.0525},
                    {"threshold": 80650, "rate": 0.0585},
                    {"threshold": 215400, "rate": 0.0625},
                    {"threshold": 1077550, "rate": 0.0685},
                    {"threshold": 5000000, "rate": 0.0965},
                    {"threshold": 25000000, "rate": 0.103},
                    {"threshold": 999999999, "rate": 0.109}
                    ]
                },
                "OH": {
                    "single": [
                    {"threshold": 26050, "rate": 0.0285},
                    {"threshold": 46100, "rate": 0.0333},
                    {"threshold": 92150, "rate": 0.038},
                    {"threshold": 115300, "rate": 0.0427},
                    {"threshold": 999999999, "rate": 0.0399}
                    ],
                    "married_joint": [
                    {"threshold": 26050, "rate": 0.0285},
                    {"threshold": 46100, "rate": 0.0333},
                    {"threshold": 92150, "rate": 0.038},
                    {"threshold": 115300, "rate": 0.0427},
                    {"threshold": 999999999, "rate": 0.0399}
                    ],
                    "head_of_household": [
                    {"threshold": 26050, "rate": 0.0285},
                    {"threshold": 46100, "rate": 0.0333},
                    {"threshold": 92150, "rate": 0.038},
                    {"threshold": 115300, "rate": 0.0427},
                    {"threshold": 999999999, "rate": 0.0399}
                    ],
                    "married_separate": [
                    {"threshold": 26050, "rate": 0.0285},
                    {"threshold": 46100, "rate": 0.0333},
                    {"threshold": 92150, "rate": 0.038},
                    {"threshold": 115300, "rate": 0.0427},
                    {"threshold": 999999999, "rate": 0.0399}
                    ]
                },
                "OK": {
                    "single": [
                    {"threshold": 1000, "rate": 0.005},
                    {"threshold": 2500, "rate": 0.01},
                    {"threshold": 3750, "rate": 0.02},
                    {"threshold": 4900, "rate": 0.03},
                    {"threshold": 7200, "rate": 0.04},
                    {"threshold": 8700, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.045}
                    ],
                    "married_joint": [
                    {"threshold": 2000, "rate": 0.005},
                    {"threshold": 5000, "rate": 0.01},
                    {"threshold": 7500, "rate": 0.02},
                    {"threshold": 9800, "rate": 0.03},
                    {"threshold": 12200, "rate": 0.04},
                    {"threshold": 15000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.045}
                    ],
                    "head_of_household": [
                    {"threshold": 2000, "rate": 0.005},
                    {"threshold": 5000, "rate": 0.01},
                    {"threshold": 7500, "rate": 0.02},
                    {"threshold": 9800, "rate": 0.03},
                    {"threshold": 12200, "rate": 0.04},
                    {"threshold": 15000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.045}
                    ],
                    "married_separate": [
                    {"threshold": 1000, "rate": 0.005},
                    {"threshold": 2500, "rate": 0.01},
                    {"threshold": 3750, "rate": 0.02},
                    {"threshold": 4900, "rate": 0.03},
                    {"threshold": 7200, "rate": 0.04},
                    {"threshold": 8700, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.045}
                    ]
                },
                "OR": {
                    "single": [
                    {"threshold": 3650, "rate": 0.0475},
                    {"threshold": 9200, "rate": 0.0675},
                    {"threshold": 125000, "rate": 0.0875},
                    {"threshold": 999999999, "rate": 0.099}
                    ],
                    "married_joint": [
                    {"threshold": 7300, "rate": 0.0475},
                    {"threshold": 18400, "rate": 0.0675},
                    {"threshold": 250000, "rate": 0.0875},
                    {"threshold": 999999999, "rate": 0.099}
                    ],
                    "head_of_household": [
                    {"threshold": 7300, "rate": 0.0475},
                    {"threshold": 18400, "rate": 0.0675},
                    {"threshold": 250000, "rate": 0.0875},
                    {"threshold": 999999999, "rate": 0.099}
                    ],
                    "married_separate": [
                    {"threshold": 3650, "rate": 0.0475},
                    {"threshold": 9200, "rate": 0.0675},
                    {"threshold": 125000, "rate": 0.0875},
                    {"threshold": 999999999, "rate": 0.099}
                    ]
                },
                "PA": {
                    "single": [
                    {"threshold": 0, "rate": 0.0307},
                    {"threshold": 999999999, "rate": 0.0307}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.0307},
                    {"threshold": 999999999, "rate": 0.0307}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.0307},
                    {"threshold": 999999999, "rate": 0.0307}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.0307},
                    {"threshold": 999999999, "rate": 0.0307}
                    ]
                },
                "RI": {
                    "single": [
                    {"threshold": 66200, "rate": 0.0375},
                    {"threshold": 150550, "rate": 0.0475},
                    {"threshold": 999999999, "rate": 0.0599}
                    ],
                    "married_joint": [
                    {"threshold": 66200, "rate": 0.0375},
                    {"threshold": 150550, "rate": 0.0475},
                    {"threshold": 999999999, "rate": 0.0599}
                    ],
                    "head_of_household": [
                    {"threshold": 66200, "rate": 0.0375},
                    {"threshold": 150550, "rate": 0.0475},
                    {"threshold": 999999999, "rate": 0.0599}
                    ],
                    "married_separate": [
                    {"threshold": 66200, "rate": 0.0375},
                    {"threshold": 150550, "rate": 0.0475},
                    {"threshold": 999999999, "rate": 0.0599}
                    ]
                },
                "SD": {
                    "single": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ]
                },
                "TN": {
                    "single": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ]
                },
                "TX": {
                    "single": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ]
                },
                "VA": {
                    "single": [
                    {"threshold": 3000, "rate": 0.02},
                    {"threshold": 5000, "rate": 0.03},
                    {"threshold": 17000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.0575}
                    ],
                    "married_joint": [
                    {"threshold": 3000, "rate": 0.02},
                    {"threshold": 5000, "rate": 0.03},
                    {"threshold": 17000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.0575}
                    ],
                    "head_of_household": [
                    {"threshold": 3000, "rate": 0.02},
                    {"threshold": 5000, "rate": 0.03},
                    {"threshold": 17000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.0575}
                    ],
                    "married_separate": [
                    {"threshold": 3000, "rate": 0.02},
                    {"threshold": 5000, "rate": 0.03},
                    {"threshold": 17000, "rate": 0.05},
                    {"threshold": 999999999, "rate": 0.0575}
                    ]
                },
                "VT": {
                    "single": [
                    {"threshold": 40950, "rate": 0.0335},
                    {"threshold": 99200, "rate": 0.066},
                    {"threshold": 206950, "rate": 0.076},
                    {"threshold": 999999999, "rate": 0.0875}
                    ],
                    "married_joint": [
                    {"threshold": 68400, "rate": 0.0335},
                    {"threshold": 165350, "rate": 0.066},
                    {"threshold": 251950, "rate": 0.076},
                    {"threshold": 999999999, "rate": 0.0875}
                    ],
                    "head_of_household": [
                    {"threshold": 54700, "rate": 0.0335},
                    {"threshold": 140900, "rate": 0.066},
                    {"threshold": 229450, "rate": 0.076},
                    {"threshold": 999999999, "rate": 0.0875}
                    ],
                    "married_separate": [
                    {"threshold": 34200, "rate": 0.0335},
                    {"threshold": 82675, "rate": 0.066},
                    {"threshold": 125975, "rate": 0.076},
                    {"threshold": 999999999, "rate": 0.0875}
                    ]
                },
                "WA": {
                    "single": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ]
                },
                "WI": {
                    "single": [
                    {"threshold": 12760, "rate": 0.0354},
                    {"threshold": 25520, "rate": 0.0465},
                    {"threshold": 280950, "rate": 0.0627},
                    {"threshold": 999999999, "rate": 0.0765}
                    ],
                    "married_joint": [
                    {"threshold": 17010, "rate": 0.0354},
                    {"threshold": 34030, "rate": 0.0465},
                    {"threshold": 374030, "rate": 0.0627},
                    {"threshold": 999999999, "rate": 0.0765}
                    ],
                    "head_of_household": [
                    {"threshold": 12760, "rate": 0.0354},
                    {"threshold": 25520, "rate": 0.0465},
                    {"threshold": 280950, "rate": 0.0627},
                    {"threshold": 999999999, "rate": 0.0765}
                    ],
                    "married_separate": [
                    {"threshold": 8510, "rate": 0.0354},
                    {"threshold": 17010, "rate": 0.0465},
                    {"threshold": 187020, "rate": 0.0627},
                    {"threshold": 999999999, "rate": 0.0765}
                    ]
                },
                "WV": {
                    "single": [
                    {"threshold": 10000, "rate": 0.03},
                    {"threshold": 25000, "rate": 0.04},
                    {"threshold": 40000, "rate": 0.045},
                    {"threshold": 60000, "rate": 0.06},
                    {"threshold": 999999999, "rate": 0.065}
                    ],
                    "married_joint": [
                    {"threshold": 10000, "rate": 0.03},
                    {"threshold": 25000, "rate": 0.04},
                    {"threshold": 40000, "rate": 0.045},
                    {"threshold": 60000, "rate": 0.06},
                    {"threshold": 999999999, "rate": 0.065}
                    ],
                    "head_of_household": [
                    {"threshold": 10000, "rate": 0.03},
                    {"threshold": 25000, "rate": 0.04},
                    {"threshold": 40000, "rate": 0.045},
                    {"threshold": 60000, "rate": 0.06},
                    {"threshold": 999999999, "rate": 0.065}
                    ],
                    "married_separate": [
                    {"threshold": 10000, "rate": 0.03},
                    {"threshold": 25000, "rate": 0.04},
                    {"threshold": 40000, "rate": 0.045},
                    {"threshold": 60000, "rate": 0.06},
                    {"threshold": 999999999, "rate": 0.065}
                    ]
                },
                "WY": {
                    "single": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_joint": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "head_of_household": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ],
                    "married_separate": [
                    {"threshold": 0, "rate": 0.0},
                    {"threshold": 999999999, "rate": 0.0}
                    ]
                }
            }
        }
        with open('data/tax_rates.json', 'w') as f:
            json.dump(tax_data, f, indent=2)
    
    # Load tax data
   
    with open('data/tax_rates.json', 'r') as f:
        tax_rates = json.load(f)
    
    return tax_rates

# Load tax data at startup
tax_rates = load_tax_data()

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Tax Rate API",
        "endpoints": {
            "Tax Rates": "/api/[year]/[state_code]/[filing_status]",
        },
        "available_years": list(tax_rates.keys()),
        "available_states": list(tax_rates.keys()),
        "available_filing_statuses": ["single", "married_joint", "head_of_household", "married_separate"]
    })

@app.route('/api/<year>/<state_code>/<filing_status>')
def get_rates(state_code, year, filing_status):
    state_code = state_code.upper()
    
    if year not in tax_rates:
        return jsonify({"error": f"State {state_code} not found"}), 404
    
    if state_code not in tax_rates[year]:
        return jsonify({"error": f"Year {year} not found for state {state_code}"}), 404
    
    if filing_status not in tax_rates[year][state_code]:
        return jsonify({"error": f"Filing status {filing_status} not found for state {state_code} in year {year}"}), 404
    
    return jsonify({
        "state": state_code,
        "year": year,
        "filing_status": filing_status,
        "tax_brackets": tax_rates[year][state_code][filing_status]
    })  

@app.route('/api/<year>/states')
def get_states(year):
    return jsonify({
        "states": list(tax_rates[year].keys())
    })

@app.route('/api/years')
def get_years():
    years = list(tax_rates.keys())
    
    return jsonify({
        "federal_years": years,
    })

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)