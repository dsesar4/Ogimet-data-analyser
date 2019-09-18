
def setting_env():
    
    months = ['january','february','march','april','may','june','july',\
              'august','september','october','november','december']
    
    return months


def setting_months(season):
    
    if (season == 0):
        season_months = [1,2,12]
        yp = 'winter'
    elif (season == 1):
        season_months = [3,4,5]
        yp = 'spring'
    elif (season == 2):
        season_months = [6,7,8]
        yp = 'summer'
    else:
        season_months = [9,10,11]
        yp = 'autumn'
        
    return season_months, yp

def setting_years(years, yp):
    years_plot = []
    for i in range(0, len(years)):
        if (yp != 'winter'):
            years_plot.append(str(years[i]) + '.')
        else:
            years_plot.append(str(years[i]) + '.' + '/' + str(years[i]+ 1) + '.')
    return years_plot


    

