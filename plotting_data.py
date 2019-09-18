import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
from statistics import mean

    
def plotting_bar_data(data, years, months, month, yp, city, name_type):
    
    data_types = {"prec":["Precipitation (mm)"],"icy":["Days with Tmin<-10°C"],"frosty":["Days with Tmax<0°C"],"cold":["Days with Tmin<0°C"], \
                  "warm":["Days with Tmax>25°C"],"hot":["Days with Tmax>30°C"],"very_hot":["Days with Tmax>35°C"],"night":["Nights with Tmin>20°C"], \
                  "hmd":["Mean air humidity (%)"],"max_temp":["Maximum temperature (°C)"],"min_temp":["Minimum temperature (°C)"], \
                  "max":["Maximum snow depth (cm)"],"cum":["Cm-days"],"snwd":["Number of days with snow cover"]} 
            
    data_per_city = pd.DataFrame({data_types[name_type][0]:data}, index = years)
    
    if (len(data) <= 5):
        par = 8
    elif (len(data) > 5 and len(data) <= 10):
        par = 12
    else:
        par = 18
    rcParams['figure.figsize'] = par, 10
    
    if (name_type == 'prec'):
        data_per_city.plot(kind = "bar", width = 0.35, color = 'dodgerblue', rot = 40) 
        plt.ylim(0, max(data) + max(data)//10)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight='bold')

    elif (name_type == 'icy' or name_type == 'frosty' or name_type == 'cold'):
        data_per_city.plot(kind = "bar", width = 0.35, color = 'royalblue', rot = 40)
        plt.ylim(0, max(data) + 5)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight='bold')

    elif (name_type == 'warm' or name_type == 'hot' or name_type == 'very_hot' or name_type == 'night'):
        data_per_city.plot(kind = "bar", width = 0.35, color = 'firebrick', rot = 40)
        plt.ylim(0, max(data) + 5)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight='bold')

    elif (name_type == 'hmd'):
        data_per_city.plot.bar(width = 0.35,color='teal',fontsize=10,rot =40)
        plt.ylim(0, max(data) + max(data)//10)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')
   
    elif (name_type == 'max'):
        data_per_city.plot.bar(width = 0.35,color='royalblue',fontsize=10,rot =40)
        plt.ylim(0, max(data) + max(data)//15 + 5)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')

    elif (name_type == 'cum'):
        data_per_city.plot.bar(width = 0.35,color='royalblue',fontsize=10,rot =40)
        plt.ylim(0, max(data) + max(data)//10 + 5)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')

    elif (name_type == 'snwd'):
        data_per_city.plot.bar(width = 0.35,color='royalblue',fontsize=10,rot =40)
        plt.ylim(0, max(data) + 5)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')

    elif(name_type == 'max_temp'):
        data_per_city.plot.bar(width = 0.35,color='orangered',fontsize=10,rot =40)
        plt.ylim(min(data) - 4, max(data) + 4)
        if (mean(data) > 0.0):
            for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
                plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')
        else:
            for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
                plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='top', fontdict={'fontweight':500, 'size':14},weight = 'bold')
    
    else:
        data_per_city.plot.bar(width = 0.35,color='dodgerblue',fontsize=10,rot =40)
        plt.ylim(min(data) - 4, max(data) + 4)
        if (mean(data) < 0.0):
            for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
                plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='top', fontdict={'fontweight':500, 'size':14},weight = 'bold')
        else:
            for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
                plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')

    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 20)
    plt.legend(fontsize=12)
    if (month != None):
        plt.title(city + ': ' + months[month-1], fontsize = 25)
    else:
        plt.title(city + ': ' + yp, fontsize = 25)
    plt.grid(lw=0.5)
    


    

