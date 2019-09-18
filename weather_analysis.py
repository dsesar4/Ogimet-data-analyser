from init_analysis import *
from plotting_data import *
from ogimet_fetchers import *

month = None
season = None

print('\nWelcome to climate analysis for Ogimet data! Please enter: ')
station = str(input('Station ID: '))
name = str(input('Name of the station: '))
start_year = int(input('Insert starting year: '))
num_of_years = int(input('Insert number of years: '))
years = []
for k in range (0, num_of_years):
    years.append(start_year + k)
months = setting_env()
year_part = int(input('Seasonal(0) or monthly(1) analysis? '))
if (year_part == 0):
    season = int(input('Season: winter(0), spring(1), summer(2) or autumn(3)? '))
else:
    month = int(input('Month(by number): '))
print('\nThank you! Now please wait for analysis to finish!')

yp = ''

if (year_part == 0):
    
    season_months, yp = setting_months(season)
    years_plot = setting_years(years, yp)
    
    icy_season, frosty_season, cold_season, warm_season, hot_season, very_hot_season, \
    night_season, precip_season, max_snow_season, cum_snow_season, snow_days_season, \
    hum_season, max_temp_season, min_temp_season = stats_ogimet_seasonal(years, season_months, station) 
    plotting_bar_data(precip_season, years_plot, months, month, yp, name, "prec")
    plotting_bar_data(max_temp_season, years_plot, months, month, yp, name, "max_temp")
    plotting_bar_data(min_temp_season, years_plot, months, month, yp, name, "min_temp")
    plotting_bar_data(hum_season, years_plot, months, month, yp, name, 'hmd')

    tmd = str(input('Print day-type stats(y/n)? '))
    snd = str(input('Print snowy data(y/n)? '))
    
    if (tmd == 'y'):
        plotting_bar_data(icy_season, years_plot, months, month, yp, name, "icy")
        plotting_bar_data(frosty_season, years_plot, months, month, yp, name, "frosty")
        plotting_bar_data(cold_season, years_plot, months, month, yp, name, "cold")
        plotting_bar_data(warm_season, years_plot, months, month, yp, name, "warm")
        plotting_bar_data(hot_season, years_plot, months, month, yp, name, "hot")
        plotting_bar_data(very_hot_season, years_plot, months, month, yp, name, "very_hot")
        plotting_bar_data(night_season, years_plot, months, month, yp, name, 'night')
    
    if (snd == 'y'):
        plotting_bar_data(snow_days_season, years_plot, months, month, yp, name, "snwd")
        plotting_bar_data(max_snow_season, years_plot, months, month, yp, name, "max")
        plotting_bar_data(cum_snow_season, years_plot, months, month, yp, name, "cum")
        
    print('\nStart script again for more insights!')
    
    
else:
    
    years_plot = setting_years(years, yp)

    icy_month, frosty_month, cold_month, warm_month, hot_month, very_hot_month, \
    night_month, precip_month, max_snow_month, cum_snow_month, snow_days_month, \
    hum_month, max_temp_month, min_temp_month = stats_ogimet_monthly(years, month, station)
    
    plotting_bar_data(precip_month, years_plot, months, month, yp, name, "prec")
    plotting_bar_data(max_temp_month, years_plot, months, month, yp, name, "max_temp")
    plotting_bar_data(min_temp_month, years_plot, months, month, yp, name, "min_temp")
    plotting_bar_data(hum_month, years_plot, months, month, yp, name, 'hmd')

    tmd = str(input('Print day-type stats(y/n)? '))
    snd = str(input('Print snowy data(y/n)? '))
    
    if (tmd == 'y'):
    
        plotting_bar_data(icy_month, years_plot, months, month, yp, name, "icy")
        plotting_bar_data(frosty_month, years_plot, months, month, yp, name, "frosty")
        plotting_bar_data(cold_month, years_plot, months, month, yp, name, "cold")
        plotting_bar_data(warm_month, years_plot, months, month, yp, name, "warm")
        plotting_bar_data(hot_month, years_plot, months, month, yp, name, "hot")
        plotting_bar_data(very_hot_month, years_plot, months, month, yp, name, "very_hot")
        plotting_bar_data(night_month, years_plot, months, month, yp, name, 'night')
    
    if (snd == 'y'):
        plotting_bar_data(snow_days_month, years_plot, months, month, yp, name, "snwd")
        plotting_bar_data(max_snow_month, years_plot, months, month, yp, name, "max")
        plotting_bar_data(cum_snow_month, years_plot, months, month, yp, name, "cum")

    print('\nStart script again for more insights!')

    
