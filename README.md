## Abstract
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

## Experimental Methods

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

