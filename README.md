## Verification of Weber's Law

### Abstract
Weber’s Law (also known as the Weber-Fechner law and Weber’s Law of Just
Noticeable Difference) states that the just noticeable difference of stimulus intensity
(i.e ∆ I), abbreviated as JND, is directly proportional to the original
stimulus intensity. Mathematically,

∆I ∝ I 

∆I = k.I 

Intuitively speaking, the stronger a signal is, the harder it is to notice small
deviations from it. Weber’s law has been succesfully applied in the fields
of sensory perception, psychophysics, numerical cognition, pharmacology and
finance[1]. In this short study, I intend to verify the applicability of Weber’s
law to the human visual perception system. Specifically, I will try to determine
if Weber’s law is valid for visual perception of just noticeable differences for
sizes of various polygons. Size, intensity and weight, three commonly perceived
quantities are known to follow the Weber’s Law of perception. This study will
validate the perception of size. My study will include four different polygons; 1)
Triangles, 2) Pentagons, 3) Heptagons, 4) Nonagons. I also intend to observe if
increasing or decreasing the number of edges of the polygon affects the Weber’s
constant.

### Experimental Methods

The basic experiment is laid out in bulletin points below:

• The study was conducted on 10 subjects (males and females). They were
presented a blank screen on which two similarly shaped polygons of different
sizes appeared. The task was to identify which of the two shapes was bigger. 
They were asked to press the ‘z’ key if they thought the left polygon
was larger; the ‘m’ key if they thought the right one was larger. Their
responses were and stored in a csv file and python pickles (serialization
objects).

• I primarily used visual stimulus for this study. Vision system is responsible
for perception of sizes of objects.

• Four basic polygon shapes were used; 1) Triangle, 2) Pentagon, 3) Heptagon,
4) Nonagon. Here ‘stimuli’ refers to the size of the polygon. I used
the open-source Python library Psychopy[2]. Psychopy defines the size
of polygons by a ‘radius’. I used five different values of radius for each
polygon.

• For each polygon and each radius, the screen displayed two similarly
shaped polygons, one with a size equal to the stimulus and other a test
value.

• Out of the pair (one test-polygon and one original stimulus-polygon)
shown at every render of the screen, the test-polygon initially started
as twice the size of the stimulus-polygon. The size was incrementally
decreased (with a step size equal to ten percent of the original stimulus
size) when the subject correctly identified the larger polygon[3].When the
subject made a mistake, the test polygon size was increased again. This
was easily achieved by using the staircase method of the Psychopy library.
To avoid bias through random guessing, the subjects had to consecutively
identify two larger polygons for the test-polygon size to decrease while they
need only commit one mistake for the size to increase again (a modified
version of the B´ek´esy method).

• There was no fixed number of trial. The staircase method in Psychopy
takes a parameter called reversals. What a reversal essentially means is
the number of times the subjects approached the configuration in which
the size of the test-polygon was equal to the size of the stimulus-polygon.
This happens because initially when the size of the test-polygon is twice
the size of the stimulus-polygon the subjects can easily figure out the
difference. When the size become equal they are prone to making mistakes
and when they do, the difference in size of the polygons increases. The
subjects then start noting the differences precisely again and the sizes of
the two polygons approach the same value. The nReversals parameter in
the staircase method was set to 4.

• The code that was used for this experiment is attached at the end of
this report. The experiment.py scripts runs the experiment while the
plotting.py leverages on the pickle (serialization) objects produced by the
experiment.py script and plots the mean values of JNDs in sizes against
the initial signal size for each polygon.

### Results

The plots of the mean values of JNDs of sizes across the 10 subjects against
the original signal value sizes are shown below. The various radius values used
are 0.5, 1.0, 2.0, 3.5, 5.5. The error bars show standard deviation. Note that the
scale of the y − axis is different from the x − axis.

![alt text](https://github.com/ayan-al/webers-law-verification/blob/master/JND_plots.PNG)

The value of Weber’s constant in each case is given by the slope of the plot. The values of k for triangles, pentagons, heptagons and nonagons are 1.0 × 10−1 , 4.2 × 10−2 , 7.5 × 10−2 and 5.3 × 10−2 respectively. Clearly, the plots confirm Weber’ Law (R2 values are given in the plot captions).

Weber’s constant does differ across subjects. The plot of the Weber’s constant for each polygon and each subject against their indices (note that the indices are not in any given order; certainly not in order of the trials) is given below. There is a wide spread of Weber’s constant over the subjects.

![alt text](https://github.com/ayan-al/webers-law-verification/blob/master/webers_constant_plots.PNG)

Guessing or cheating was prevented in the study by modifying the staircase statement. (Explained in Experimental Procedures). Needless to say, the signal-polygon was randomly assigned to one of the sides (left or right) in every render.

It is also clear that Weber’s constant varies for each polygon type. However
it does not show any graded increase or decrease as the number of edges of the
polygon is varied.

### Discussion
From this brief study, it is indeed clear that Weber’s law is followed in the recognition of polygon sizes. As shown, the value of Weber’s constant is different across the subjects. This obviously means that their JNDs would also be different. This is the source of noise in the data. The results were not significantly different when the experiment was done on the same subject twice (data not shown). Changing the number of edges in the polygon did change the Weber’s constant but not in any conceivable pattern. As such, no concrete reason can be attributed to this change. Also, changing the color of the polygon on the screen did not have any effect on the Weber’s constant for each polygon (data not shown). This may suggest that colour has no effect on the perception of size in the case of polygons. I cannot include myself as one of the subjects because I have written the code for the experiment! As such I am aware of the previous and the next stimulus. Not to mention I also know the method that the experiment uses to avoid random guessing. Clearly, there is a huge “Experimenter’s Bias”.

### References

1. https://en.wikipedia.org/wiki/WeberFechner_law
2. www.psychopy.org
3. Holden JK, Francisco EM, Zhang Z, Baric C, Tommerdahl M. An Undergraduate Laboratory Exercise to Study Weber’s Law. Journal of Under- graduate Neuroscience Education. 2011;9(2):A71-A74.
