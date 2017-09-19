from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
import numpy, random, pyglet

def draw_polygon(file_name,sides,radius,fillcolor=None):
    if fillcolor == True:
        fillcolor = [1,1,1]
    signal_radius = radius
    print('signal_radius:'+str(signal_radius)+'\n')
    staircase = data.StairHandler(startVal = 2*signal_radius,
                      stepType = 'lin', stepSizes=[0.1*signal_radius],
                      nUp=1, nDown=1,nReversals=4, minVal=signal_radius)
    for thisIncrement in staircase:
        #print(thisIncrement)
        test_radius = thisIncrement
        #print('test_radius'+ str(test_radius)+'\n')
        signal_side= 15*random.choice([-1,1])
        #print('signal_side: '+ str(signal_side))
        if signal_side >0:
            signal_render = 'right'
        else:
            signal_render = 'left'
        test_side = -signal_side
        #print('signal_render: '+ str(signal_render))
        polygon_signal = visual.Polygon(win=mywin, edges=sides,
                    radius=signal_radius,fillColor=[1,1,1],pos=(signal_side, 0))
        polygon_test = visual.Polygon(win=mywin, edges=sides,
                    radius=test_radius, fillColor=[1,1,1],pos=(-signal_side, 0))
        if signal_render == 'left':
            if signal_radius > test_radius:
                #print('entered the left loop one')
                bigger = 'left'
                #print(bigger)
            else:
                #print('Entered the left loop two')
                bigger = 'right'
        if signal_render == 'right':
            if signal_radius > test_radius:
                #print('Entered the right loop one')
                bigger = 'right'
                #print(bigger)
            else:
                #print('Entered the right loop two')
                bigger = 'left'
        polygon_signal.draw()
        polygon_test.draw()
        mywin.flip()
        print('Bigger: ' + bigger)
        thisResp=None
        while thisResp==None:
            allKeys=event.waitKeys()
            for thisKey in allKeys:
                if thisKey=='z':
                    if bigger == 'left': thisResp = 1
                    else: thisResp = -1
                if thisKey=='m':
                    if bigger == 'right': thisResp = 1
                    else: thisResp = -1
                if thisKey in ['q', 'escape']:
                    core.quit()
            event.clearEvents()
        staircase.addData(thisResp)
        #print('This Response: ' + str(thisResp))
        file_name.write(str(sides)+','+str((fillcolor==None))+','
        +str(signal_radius)+','+str(test_radius)+','+str(thisResp)+'\n')
        core.wait(1.0)
        mywin.flip()
    staircase.saveAsPickle('poly-'+str(sides)+'_'
    + str(fillcolor==None)+'_'+ str(radius))
    print('reversals:')
    print(staircase.reversalIntensities)
    approxThreshold = numpy.average(staircase.reversalIntensities[-6:])
    print('mean of final 6 reversals = %.3f' % (approxThreshold))

subject_name = {'Name':'please enter your name'}
subject_name['time_and_date'] = data.getDateStr()
dlg = gui.DlgFromDict(subject_name, title='Weber\'s Law Experiment',
                                                        fixed=['time_and_date'])
if dlg.OK:
    toFile('parameters.pickle', subject_name)
else:
    core.quit()

file_name = subject_name['Name'] + subject_name['time_and_date']
text_file = open(file_name+'.csv', 'w')
text_file.write('polygon,outline_or_filled, signal_size, test_size, correct\n')

mywin = visual.Window([1920,1080],allowGUI=True, monitor='testMonitor',
                                                                    units='deg')

#signal_radii = [5.5,0.5,3.5,1.0,2.0]


draw_polygon(text_file,sides=9,radius=5.5,fillcolor=True)
draw_polygon(text_file,sides=3,radius=3.5,fillcolor=True)
draw_polygon(text_file,sides=5,radius=5.5,fillcolor=True)
draw_polygon(text_file,sides=7,radius=1.0,fillcolor=True)
draw_polygon(text_file,sides=5,radius=3.5,fillcolor=True)
draw_polygon(text_file,sides=7,radius=0.5,fillcolor=True)
draw_polygon(text_file,sides=9,radius=0.5,fillcolor=True)
draw_polygon(text_file,sides=3,radius=2.0,fillcolor=True)
draw_polygon(text_file,sides=5,radius=2.0,fillcolor=True)
draw_polygon(text_file,sides=9,radius=1.0,fillcolor=True)
draw_polygon(text_file,sides=3,radius=0.5,fillcolor=True)
draw_polygon(text_file,sides=7,radius=5.5,fillcolor=True)
draw_polygon(text_file,sides=9,radius=3.5,fillcolor=True)
draw_polygon(text_file,sides=3,radius=5.5,fillcolor=True)
draw_polygon(text_file,sides=7,radius=3.5,fillcolor=True)
draw_polygon(text_file,sides=5,radius=0.5,fillcolor=True)
draw_polygon(text_file,sides=7,radius=2.0,fillcolor=True)
draw_polygon(text_file,sides=5,radius=1.0,fillcolor=True)
draw_polygon(text_file,sides=3,radius=1.0,fillcolor=True)
draw_polygon(text_file,sides=9,radius=2.0,fillcolor=True)

mywin.close()
core.quit()
