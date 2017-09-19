from __future__ import print_function
from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
import numpy as np, random, pyglet, os
import pylab
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy import stats
from matplotlib import style

#style.use('ggplot')

common_path = '/media/al/Fat32/webers_law'
subjects = ['gaurav','arpit','aditya','sandhra','samyak','rohit','sai',
            'mahendra','rohitmurali','pragyadeep']
subjects_caps = ['GAURAV','ARPIT','ADITYA','SANDHRA','SAMYAK','ROHIT',
                 'SAI','MAHENDRA','ROHITMURALI','PRAGYADEEP']
polygons = ['triangle','pentagon','heptagon','nonagon']
polygon_edges = [3,5,7,9]
polygon_edges_to_name = dict(zip(polygon_edges,polygons))
polygon_name_to_edges = dict(zip(polygons,polygon_edges))
signal_radii = [0.5,1.0,2.0,3.5,5.5]
df = pd.DataFrame(index=subjects,columns=signal_radii)

def update_dataframe(edges,subjects):
    for subject in subjects:
        for radius in signal_radii:
            path = common_path + '/' + subject + '/'
            staircase = fromFile(path+'poly-'+str(edges)+'_False_'
                                                        +str(radius)+'.psydat')
            approxThreshold = np.average(staircase.reversalIntensities[-6:])
            JND = abs(approxThreshold-radius)
            df.at[subject,radius] = JND
            #print(df)

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def create_weber_plot(edges, polygon):
    mean_JND_values = []
    error_bars = []
    for radius in signal_radii:
        column_slice = df.loc[:,radius]
        mean_JND_values.append(np.mean(column_slice))
        error_bars.append(np.std(column_slice))
        #print(mean_JND_values)
        #print(error_bars)
    x = np.array(signal_radii)
    y = np.array(mean_JND_values)
    e = np.array(error_bars)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    line = slope*x+intercept
    plt.plot(x,y,'o', x, line)
    pylab.title('Weber\'s Law for perception of size of ' + polygon +
                                    ' (Slope= '+ str(truncate(slope, 3)) + ')')
    plt.xlabel(r'Intensity of signal ($I$) (radius of the polygon)')
    plt.ylabel(r'Just Noticeable Difference (JND) or $\Delta$ I')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    plt.errorbar(x, y, e, linestyle='None', marker='^')
    #plt.show()
    return slope

def find_weber_constant(name,edges):
    subject = [str(name)]
    update_dataframe(edges,subject)
    webers_constant = create_weber_plot(edges,polygon_edges_to_name[edges])
    return webers_constant

##create_plot(3,'triangle')
##create_plot(5,'pentagon')
##create_plot(7,'heptagon')
##create_plot(9,'nonagon')
webers_constant = {}
for polygon in polygons:
    _index = 1
    for name in subjects:
        webers_constant[_index] =
                        find_weber_constant(name,polygon_name_to_edges[polygon])
        _index += 1
    lists = sorted(webers_constant.items())
    print(lists)
    x, y = zip(*lists)
    plt.figure()
    plt.scatter(x,y)
    pylab.title('Weber\'s constant for various subjects (' + str(polygon) + ')')
    plt.xlabel('Indices of the subjects')
    plt.ylabel('Weber\'s constant ' + r'$K$')
    plt.show()
