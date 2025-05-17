from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Load tax data from JSON files
def load_tax_data():
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Create federal tax data if it doesn't exist
    if not os.path.exists('data/federal_tax_rates.json'):
        federal_tax_data = {
            "2024": {
                "single": [
                    {"bracket": 0, "rate": 0.10},
                    {"bracket": 11000, "rate": 0.12},
                    {"bracket": 44725, "rate": 0.22},
                    {"bracket": 95375, "rate": 0.24},
                    {"bracket": 182100, "rate": 0.32},
                    {"bracket": 231250, "rate": 0.35},
                    {"bracket": 578125, "rate": 0.37}
                ],
                "married_joint": [
                    {"bracket": 0, "rate": 0.10},
                    {"bracket": 22000, "rate": 0.12},
                    {"bracket": 89450, "rate": 0.22},
                    {"bracket": 190750, "rate": 0.24},
                    {"bracket": 364200, "rate": 0.32},
                    {"bracket": 462500, "rate": 0.35},
                    {"bracket": 693750, "rate": 0.37}
                ],
                "head_of_household": [
                    {"bracket": 0, "rate": 0.10},
                    {"bracket": 15700, "rate": 0.12},
                    {"bracket": 59850, "rate": 0.22},
                    {"bracket": 95350, "rate": 0.24},
                    {"bracket": 182100, "rate": 0.32},
                    {"bracket": 231250, "rate": 0.35},
                    {"bracket": 578100, "rate": 0.37}
                ],
                "married_separate": [
                    {"bracket": 0, "rate": 0.10},
                    {"bracket": 11000, "rate": 0.12},
                    {"bracket": 44725, "rate": 0.22},
                    {"bracket": 95375, "rate": 0.24},
                    {"bracket": 182100, "rate": 0.32},
                    {"bracket": 231250, "rate": 0.35},
                    {"bracket": 346875, "rate": 0.37}
                ]
            }
        }
        with open('data/federal_tax_rates.json', 'w') as f:
            json.dump(federal_tax_data, f, indent=2)
    
    # Create state tax data if it doesn't exist
    if not os.path.exists('data/state_tax_rates.json'):
        state_tax_data = {
            "AL": {
                "2024": {
                    "note": "Alabama has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.05}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.05}
                    ],
                    "head_of_household": [
                        {"bracket": 0, "rate": 0.05}
                    ],
                    "married_separate": [
                        {"bracket": 0, "rate": 0.05}
                    ]
                }
            },
            "AK": {
                "2024": {
                    "note": "Alaska has no state income tax",
                    "single": [
                        {"bracket": 0, "rate": 0.0}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0}
                    ],
                    "head_of_household": [
                        {"bracket": 0, "rate": 0.0}
                    ],
                    "married_separate": [
                        {"bracket": 0, "rate": 0.0}
                    ]
                }
            },
            "AZ": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0259},
                        {"bracket": 28653, "rate": 0.0334},
                        {"bracket": 57305, "rate": 0.0417},
                        {"bracket": 171911, "rate": 0.045}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0259},
                        {"bracket": 57305, "rate": 0.0334},
                        {"bracket": 114610, "rate": 0.0417},
                        {"bracket": 343821, "rate": 0.045}
                    ]
                }
            },
            "AR": {
                "2024": {
                    "note": "Arkansas has adjusted its rates for 2024",
                    "single": [
                        {"bracket": 0, "rate": 0.02},
                        {"bracket": 4300, "rate": 0.04},
                        {"bracket": 8500, "rate": 0.049}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.02},
                        {"bracket": 4300, "rate": 0.04},
                        {"bracket": 8500, "rate": 0.049}
                    ]
                }
            },
            "CA": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.01},
                        {"bracket": 10099, "rate": 0.02},
                        {"bracket": 23942, "rate": 0.04},
                        {"bracket": 37788, "rate": 0.06},
                        {"bracket": 52455, "rate": 0.08},
                        {"bracket": 66295, "rate": 0.093},
                        {"bracket": 338639, "rate": 0.103},
                        {"bracket": 406364, "rate": 0.113},
                        {"bracket": 677275, "rate": 0.123},
                        {"bracket": 1000000, "rate": 0.133}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.01},
                        {"bracket": 20198, "rate": 0.02},
                        {"bracket": 47884, "rate": 0.04},
                        {"bracket": 75576, "rate": 0.06},
                        {"bracket": 104910, "rate": 0.08},
                        {"bracket": 132590, "rate": 0.093},
                        {"bracket": 677278, "rate": 0.103},
                        {"bracket": 812728, "rate": 0.113},
                        {"bracket": 1354550, "rate": 0.123},
                        {"bracket": 2000000, "rate": 0.133}
                    ]
                }
            },
            "CO": {
                "2024": {
                    "note": "Colorado has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0443}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0443}
                    ]
                }
            },
            "CT": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.03},
                        {"bracket": 10000, "rate": 0.05},
                        {"bracket": 50000, "rate": 0.055},
                        {"bracket": 100000, "rate": 0.06},
                        {"bracket": 200000, "rate": 0.065},
                        {"bracket": 250000, "rate": 0.069},
                        {"bracket": 500000, "rate": 0.0699}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.03},
                        {"bracket": 20000, "rate": 0.05},
                        {"bracket": 100000, "rate": 0.055},
                        {"bracket": 200000, "rate": 0.06},
                        {"bracket": 400000, "rate": 0.065},
                        {"bracket": 500000, "rate": 0.069},
                        {"bracket": 1000000, "rate": 0.0699}
                    ]
                }
            },
            "DE": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 2000, "rate": 0.022},
                        {"bracket": 5000, "rate": 0.039},
                        {"bracket": 10000, "rate": 0.048},
                        {"bracket": 20000, "rate": 0.052},
                        {"bracket": 25000, "rate": 0.055},
                        {"bracket": 60000, "rate": 0.066}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 2000, "rate": 0.022},
                        {"bracket": 5000, "rate": 0.039},
                        {"bracket": 10000, "rate": 0.048},
                        {"bracket": 20000, "rate": 0.052},
                        {"bracket": 25000, "rate": 0.055},
                        {"bracket": 60000, "rate": 0.066}
                    ]
                }
            },
            "DC": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.04},
                        {"bracket": 10000, "rate": 0.06},
                        {"bracket": 40000, "rate": 0.065},
                        {"bracket": 60000, "rate": 0.085},
                        {"bracket": 350000, "rate": 0.0925},
                        {"bracket": 1000000, "rate": 0.0975}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.04},
                        {"bracket": 10000, "rate": 0.06},
                        {"bracket": 40000, "rate": 0.065},
                        {"bracket": 60000, "rate": 0.085},
                        {"bracket": 350000, "rate": 0.0925},
                        {"bracket": 1000000, "rate": 0.0975}
                    ]
                }
            },
            "FL": {
                "2024": {
                    "note": "Florida has no state income tax",
                    "single": [
                        {"bracket": 0, "rate": 0.0}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0}
                    ]
                }
            },
            "GA": {
                "2024": {
                    "note": "Georgia has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0555}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0555}
                    ]
                }
            },
            "HI": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.014},
                        {"bracket": 2400, "rate": 0.032},
                        {"bracket": 4800, "rate": 0.055},
                        {"bracket": 9600, "rate": 0.064},
                        {"bracket": 14400, "rate": 0.068},
                        {"bracket": 19200, "rate": 0.072},
                        {"bracket": 24000, "rate": 0.076},
                        {"bracket": 36000, "rate": 0.079},
                        {"bracket": 48000, "rate": 0.0825},
                        {"bracket": 150000, "rate": 0.09},
                        {"bracket": 175000, "rate": 0.10},
                        {"bracket": 200000, "rate": 0.11}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.014},
                        {"bracket": 4800, "rate": 0.032},
                        {"bracket": 9600, "rate": 0.055},
                        {"bracket": 19200, "rate": 0.064},
                        {"bracket": 28800, "rate": 0.068},
                        {"bracket": 38400, "rate": 0.072},
                        {"bracket": 48000, "rate": 0.076},
                        {"bracket": 72000, "rate": 0.079},
                        {"bracket": 96000, "rate": 0.0825},
                        {"bracket": 300000, "rate": 0.09},
                        {"bracket": 350000, "rate": 0.10},
                        {"bracket": 400000, "rate": 0.11}
                    ]
                }
            },
            "ID": {
                "2024": {
                    "note": "Idaho has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.059}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.059}
                    ]
                }
            },
            "IL": {
                "2024": {
                    "note": "Illinois has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0495}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0495}
                    ]
                }
            },
            "IN": {
                "2024": {
                    "note": "Indiana has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0323}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0323}
                    ]
                }
            },
            "IA": {
                "2024": {
                    "note": "Iowa has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0375}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0375}
                    ]
                }
            },
            "KS": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.031},
                        {"bracket": 15000, "rate": 0.0525},
                        {"bracket": 30000, "rate": 0.057}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.031},
                        {"bracket": 30000, "rate": 0.0525},
                        {"bracket": 60000, "rate": 0.057}
                    ]
                }
            },
            "KY": {
                "2024": {
                    "note": "Kentucky has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.044}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.044}
                    ]
                }
            },
            "LA": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0185},
                        {"bracket": 12500, "rate": 0.035},
                        {"bracket": 50000, "rate": 0.0425}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0185},
                        {"bracket": 25000, "rate": 0.035},
                        {"bracket": 100000, "rate": 0.0425}
                    ]
                }
            },
            "ME": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.058},
                        {"bracket": 24500, "rate": 0.0675},
                        {"bracket": 58050, "rate": 0.0715}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.058},
                        {"bracket": 49000, "rate": 0.0675},
                        {"bracket": 116100, "rate": 0.0715}
                    ]
                }
            },
            "MD": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.02},
                        {"bracket": 1000, "rate": 0.03},
                        {"bracket": 2000, "rate": 0.04},
                        {"bracket": 3000, "rate": 0.0475},
                        {"bracket": 100000, "rate": 0.05},
                        {"bracket": 125000, "rate": 0.0525},
                        {"bracket": 150000, "rate": 0.055},
                        {"bracket": 250000, "rate": 0.0575}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.02},
                        {"bracket": 1000, "rate": 0.03},
                        {"bracket": 2000, "rate": 0.04},
                        {"bracket": 3000, "rate": 0.0475},
                        {"bracket": 150000, "rate": 0.05},
                        {"bracket": 175000, "rate": 0.0525},
                        {"bracket": 225000, "rate": 0.055},
                        {"bracket": 300000, "rate": 0.0575}
                    ]
                }
            },
            "MA": {
                "2024": {
                    "note": "Massachusetts has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.05}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.05}
                    ]
                }
            },
            "MI": {
                "2024": {
                    "note": "Michigan has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0405}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0405}
                    ]
                }
            },
            "MN": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0535},
                        {"bracket": 31440, "rate": 0.068},
                        {"bracket": 103600, "rate": 0.0785},
                        {"bracket": 183560, "rate": 0.0985}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0535},
                        {"bracket": 45760, "rate": 0.068},
                        {"bracket": 180790, "rate": 0.0785},
                        {"bracket": 283690, "rate": 0.0985}
                    ]
                }
            },
            "MS": {
                "2024": {
                    "note": "Mississippi has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0495}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0495}
                    ]
                }
            },
            "MO": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 1253, "rate": 0.015},
                        {"bracket": 2506, "rate": 0.02},
                        {"bracket": 3759, "rate": 0.025},
                        {"bracket": 5012, "rate": 0.03},
                        {"bracket": 6265, "rate": 0.035},
                        {"bracket": 7518, "rate": 0.04},
                        {"bracket": 8771, "rate": 0.045},
                        {"bracket": 10024, "rate": 0.0495}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 1253, "rate": 0.015},
                        {"bracket": 2506, "rate": 0.02},
                        {"bracket": 3759, "rate": 0.025},
                        {"bracket": 5012, "rate": 0.03},
                        {"bracket": 6265, "rate": 0.035},
                        {"bracket": 7518, "rate": 0.04},
                        {"bracket": 8771, "rate": 0.045},
                        {"bracket": 10024, "rate": 0.0495}
                    ]
                }
            },
            "MT": {
                "2024": {
                    "note": "Montana has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0575}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0575}
                    ]
                }
            },
            "NE": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 3700, "rate": 0.0351},
                        {"bracket": 22170, "rate": 0.0451},
                        {"bracket": 35730, "rate": 0.0582}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 7370, "rate": 0.0351},
                        {"bracket": 44330, "rate": 0.0451},
                        {"bracket": 71450, "rate": 0.0582}
                    ]
                }
            },
            "NV": {
                "2024": {
                    "note": "Nevada has no state income tax",
                    "single": [
                        {"bracket": 0, "rate": 0.0}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0}
                    ]
                }
            },
            "NH": {
                "2024": {
                    "note": "New Hampshire only taxes interest and dividend income at 4%",
                    "single": [
                        {"bracket": 0, "rate": 0.04}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.04}
                    ]
                }
            },
            "NJ": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.014},
                        {"bracket": 20000, "rate": 0.0175},
                        {"bracket": 35000, "rate": 0.035},
                        {"bracket": 40000, "rate": 0.05525},
                        {"bracket": 75000, "rate": 0.0637},
                        {"bracket": 500000, "rate": 0.0897},
                        {"bracket": 1000000, "rate": 0.1075}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.014},
                        {"bracket": 20000, "rate": 0.0175},
                        {"bracket": 50000, "rate": 0.035},
                        {"bracket": 70000, "rate": 0.05525},
                        {"bracket": 80000, "rate": 0.0637},
                        {"bracket": 150000, "rate": 0.0897},
                        {"bracket": 500000, "rate": 0.1075},
                        {"bracket": 1000000, "rate": 0.1075}
                    ]
                }
            },
            "NM": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.019},
                        {"bracket": 5500, "rate": 0.032},
                        {"bracket": 11000, "rate": 0.047},
                        {"bracket": 16000, "rate": 0.049},
                        {"bracket": 210000, "rate": 0.059}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.019},
                        {"bracket": 8000, "rate": 0.032},
                        {"bracket": 16000, "rate": 0.047},
                        {"bracket": 24000, "rate": 0.049},
                        {"bracket": 315000, "rate": 0.059}
                    ]
                }
            },
            "NY": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.04},
                        {"bracket": 13900, "rate": 0.045},
                        {"bracket": 80650, "rate": 0.0525},
                        {"bracket": 215400, "rate": 0.0585},
                        {"bracket": 1077550, "rate": 0.0625},
                        {"bracket": 5000000, "rate": 0.0685},
                        {"bracket": 25000000, "rate": 0.103}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.04},
                        {"bracket": 27900, "rate": 0.045},
                        {"bracket": 161550, "rate": 0.0525},
                        {"bracket": 323200, "rate": 0.0585},
                        {"bracket": 2155350, "rate": 0.0625},
                        {"bracket": 5000000, "rate": 0.0685},
                        {"bracket": 25000000, "rate": 0.103}
                    ]
                }
            },
            "NC": {
                "2024": {
                    "note": "North Carolina has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0475}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0475}
                    ]
                }
            },
            "ND": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 1000, "rate": 0.011},
                        {"bracket": 40525, "rate": 0.0204},
                        {"bracket": 98100, "rate": 0.0227},
                        {"bracket": 204675, "rate": 0.0264},
                        {"bracket": 445000, "rate": 0.029}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 1000, "rate": 0.011},
                        {"bracket": 67700, "rate": 0.0204},
                        {"bracket": 163550, "rate": 0.0227},
                        {"bracket": 249150, "rate": 0.0264},
                        {"bracket": 445000, "rate": 0.029}
                    ]
                }
            },
            "OH": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 26050, "rate": 0.02765},
                        {"bracket": 46100, "rate": 0.03226},
                        {"bracket": 92150, "rate": 0.03688},
                        {"bracket": 115300, "rate": 0.03990}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0},
                        {"bracket": 26050, "rate": 0.02765},
                        {"bracket": 46100, "rate": 0.03226},
                        {"bracket": 92150, "rate": 0.03688},
                        {"bracket": 115300, "rate": 0.03990}
                    ]
                }
            },
            "OK": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0025},
                        {"bracket": 1000, "rate": 0.0075},
                        {"bracket": 2500, "rate": 0.0175},
                        {"bracket": 3750, "rate": 0.0275},
                        {"bracket": 4900, "rate": 0.0375},
                        {"bracket": 7200, "rate": 0.0475}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0025},
                        {"bracket": 2000, "rate": 0.0075},
                        {"bracket": 5000, "rate": 0.0175},
                        {"bracket": 7500, "rate": 0.0275},
                        {"bracket": 9800, "rate": 0.0375},
                        {"bracket": 12200, "rate": 0.0475}
                    ]
                }
            },
            "OR": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0475},
                        {"bracket": 3750, "rate": 0.0675},
                        {"bracket": 9450, "rate": 0.0875},
                        {"bracket": 125000, "rate": 0.099}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0475},
                        {"bracket": 7500, "rate": 0.0675},
                        {"bracket": 18900, "rate": 0.0875},
                        {"bracket": 250000, "rate": 0.099}
                    ]
                }
            },
            "PA": {
                "2024": {
                    "note": "Pennsylvania has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0307}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0307}
                    ]
                }
            },
            "RI": {
                "2024": {
                    "single": [
                        {"bracket": 0, "rate": 0.0375},
                        {"bracket": 73450, "rate": 0.0475},
                        {"bracket": 166950, "rate": 0.0599}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0375},
                        {"bracket": 73450, "rate": 0.0475},
                        {"bracket": 166950, "rate": 0.0599}
                    ]
                }
            },
            "SC": {
                "2024": {
                    "note": "South Carolina has a flat tax rate",
                    "single": [
                        {"bracket": 0, "rate": 0.0625}
                    ],
                    "married_joint": [
                        {"bracket": 0, "rate": 0.0625}
                    ]
                }
            },
            "SD": {
                "2024": {
                    "note": "South Dakota has no state income tax",
                    "single": [
                        {"bracket": 0, "rate": 0.0}
                    ],
                    "married_joint": [
                        {"bracket": 0,
        with open('data/state_tax_rates.json', 'w') as f:
            json.dump(state_tax_data, f, indent=2)
    
    # Load tax data
    with open('data/federal_tax_rates.json', 'r') as f:
        federal_tax_rates = json.load(f)
    
    with open('data/state_tax_rates.json', 'r') as f:
        state_tax_rates = json.load(f)
    
    return federal_tax_rates, state_tax_rates

# Load tax data at startup
federal_tax_rates, state_tax_rates = load_tax_data()

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Tax Rate API",
        "endpoints": {
            "Federal Tax Rates": "/api/federal/[year]/[filing_status]",
            "State Tax Rates": "/api/state/[state_code]/[year]/[filing_status]",
            "Calculate Federal Tax": "/api/calculate/federal?income=[income]&year=[year]&filing_status=[filing_status]",
            "Calculate State Tax": "/api/calculate/state?state=[state_code]&income=[income]&year=[year]&filing_status=[filing_status]"
        },
        "available_years": list(federal_tax_rates.keys()),
        "available_states": list(state_tax_rates.keys()),
        "available_filing_statuses": ["single", "married_joint", "head_of_household", "married_separate"]
    })

@app.route('/api/federal/<year>/<filing_status>')
def get_federal_rates(year, filing_status):
    if year not in federal_tax_rates:
        return jsonify({"error": f"Year {year} not found"}), 404
    
    if filing_status not in federal_tax_rates[year]:
        return jsonify({"error": f"Filing status {filing_status} not found"}), 404
    
    return jsonify({
        "year": year,
        "filing_status": filing_status,
        "tax_brackets": federal_tax_rates[year][filing_status]
    })

@app.route('/api/state/<state_code>/<year>/<filing_status>')
def get_state_rates(state_code, year, filing_status):
    state_code = state_code.upper()
    
    if state_code not in state_tax_rates:
        return jsonify({"error": f"State {state_code} not found"}), 404
    
    if year not in state_tax_rates[state_code]:
        return jsonify({"error": f"Year {year} not found for state {state_code}"}), 404
    
    if filing_status not in state_tax_rates[state_code][year]:
        return jsonify({"error": f"Filing status {filing_status} not found for state {state_code} in year {year}"}), 404
    
    return jsonify({
        "state": state_code,
        "year": year,
        "filing_status": filing_status,
        "tax_brackets": state_tax_rates[state_code][year][filing_status]
    })

@app.route('/api/calculate/federal')
def calculate_federal_tax():
    income = request.args.get('income', type=float)
    year = request.args.get('year', '2024')
    filing_status = request.args.get('filing_status', 'single')
    
    if not income:
        return jsonify({"error": "Income parameter is required"}), 400
    
    if year not in federal_tax_rates:
        return jsonify({"error": f"Year {year} not found"}), 404
    
    if filing_status not in federal_tax_rates[year]:
        return jsonify({"error": f"Filing status {filing_status} not found"}), 404
    
    brackets = federal_tax_rates[year][filing_status]
    tax = calculate_tax(income, brackets)
    
    return jsonify({
        "income": income,
        "year": year,
        "filing_status": filing_status,
        "tax_amount": tax,
        "effective_rate": tax / income if income > 0 else 0
    })

@app.route('/api/calculate/state')
def calculate_state_tax():
    state_code = request.args.get('state', '').upper()
    income = request.args.get('income', type=float)
    year = request.args.get('year', '2024')
    filing_status = request.args.get('filing_status', 'single')
    
    if not state_code:
        return jsonify({"error": "State parameter is required"}), 400
        
    if not income:
        return jsonify({"error": "Income parameter is required"}), 400
    
    if state_code not in state_tax_rates:
        return jsonify({"error": f"State {state_code} not found"}), 404
    
    if year not in state_tax_rates[state_code]:
        return jsonify({"error": f"Year {year} not found for state {state_code}"}), 404
    
    if filing_status not in state_tax_rates[state_code][year]:
        return jsonify({"error": f"Filing status {filing_status} not found for state {state_code} in year {year}"}), 404
    
    brackets = state_tax_rates[state_code][year][filing_status]
    tax = calculate_tax(income, brackets)
    
    return jsonify({
        "state": state_code,
        "income": income,
        "year": year,
        "filing_status": filing_status,
        "tax_amount": tax,
        "effective_rate": tax / income if income > 0 else 0
    })

def calculate_tax(income, brackets):
    """Calculate tax based on marginal tax brackets"""
    tax = 0
    prev_bracket = 0
    
    # Sort brackets by amount (ascending)
    sorted_brackets = sorted(brackets, key=lambda x: x["bracket"])
    
    for i, bracket in enumerate(sorted_brackets):
        # If this is the last bracket or income falls within this bracket range
        if i == len(sorted_brackets) - 1 or income <= sorted_brackets[i+1]["bracket"]:
            tax += (income - prev_bracket) * bracket["rate"]
            break
        else:
            # Calculate tax for this bracket range
            tax += (sorted_brackets[i+1]["bracket"] - prev_bracket) * bracket["rate"]
            prev_bracket = sorted_brackets[i+1]["bracket"]
    
    return tax

@app.route('/api/states')
def get_states():
    return jsonify({
        "states": list(state_tax_rates.keys())
    })

@app.route('/api/years')
def get_years():
    federal_years = list(federal_tax_rates.keys())
    
    state_years = {}
    for state in state_tax_rates:
        state_years[state] = list(state_tax_rates[state].keys())
    
    return jsonify({
        "federal_years": federal_years,
        "state_years": state_years
    })

@app.route('/api/update/federal', methods=['POST'])
def update_federal_rates():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Update federal tax rates
    try:
        global federal_tax_rates
        federal_tax_rates.update(data)
        
        # Save to file
        with open('data/federal_tax_rates.json', 'w') as f:
            json.dump(federal_tax_rates, f, indent=2)
        
        return jsonify({"message": "Federal tax rates updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/update/state', methods=['POST'])
def update_state_rates():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Update state tax rates
    try:
        global state_tax_rates
        state_tax_rates.update(data)
        
        # Save to file
        with open('data/state_tax_rates.json', 'w') as f:
            json.dump(state_tax_rates, f, indent=2)
        
        return jsonify({"message": "State tax rates updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
