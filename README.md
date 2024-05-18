# forecast_india_statewise_energy_backend
This repository holds a Flask app and a random forest model that takes state, year, population .Also command to build Docker image and deploy web service on render.

The backend is live at URI='https://forecast-india-statewise-energy-backend.onrender.com/predict'. Hit it with json containing 3 fields, e.g.:

{ "State/Union Territory": "West Bengal", "End_Year": 2024, "population(crores)": 9.97 }

output:

{ "avail_crore_kWh": 6720.77, "req_crore_kWh": 7481.98 }
