# Ogimet data analyser

This script is used for Ogimet (weather) data visualization. There are vast amounts of weather and climate data available on Ogimet, but it's usually just tables or synops. With this script you can easily visualize climate data and visualize bar charts with a lot of useful information and scale up weather data usage.

Main advantage is simplicity. Only start script (weather_analysis), input station ID, starting year and time interval. That's it, script does rest of the job!

You can choose between two options:

1. Seasonal (ex. winter, summer...) data analysis
2. Monthly (ex. january, july...) data analysis.

There are 14 bar charts available for instant visualization: 1. Precipitation, 2. Maximum temperature, 3. Minimum temperature, 4. Humidity, 5. Days with snow cover, 6. Maximum snow depth, 7. Cumulative (cm) snow cover, 8. Number of days with Tmin<-10°C, 9. Number of days with Tmax<0°C, 10. Number of days with Tmin<0°C, 11. Number of days with Tmax>25°C, 12. Number of days with Tmax>30°C, 13. Number of days with Tmax>35°C, 14. Number of days with Tmin>20°C. 

Script is started by running weather_analysis.py. Parameters for analysis are then manually inserted. Init_analysis.py initializes data for analysis. Ogimet_fetchers.py does most of the job fetching data from Ogimet and putting it in pandas dataframes and lists. Plotting_data.py plots your data on bar charts.

The more data or longer period, the more you wait for fetchers to get it. Usually it shouldn't take it more than 2 minutes, even for longer/bigger amounts of data analysed.

You can easily add more charts with different borders as long as data used for analysis is available via Ogimet.

Don't overuse and abuse. Enjoy! :)
