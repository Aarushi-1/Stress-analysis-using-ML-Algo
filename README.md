# Stress-analysis-using-ML-Algo

## About Dataset
The dataset was collected while wearing the watch. For duration of the study conducted the participant was made to drive on a city road and on a Highway. The starting point was City1which had traffic and narrow roads for the driver to drive. From where the route was taken as such which includes an highway and lesser traffic but fast moving then from there we arrive at City 2 which again is filled with all sorts of traffic and bumpy roads. In the city 2 from a round about U turn was taken and same route was taken till end point in city1 which is also the starting point.
The dataset contains following fields :
Participant code: Every participant or the subject on whom the activity was performed has been given code. This code is acronymized with two alphabets and a digit at the third place.
Gender: Every participants gender is noted and coded M for male participant and F for female participant. 
Time Stamp: Every participants activity stating time and ending time is noted. This value is in the time format “%H:%M:%s”. Hours, minutes and seconds are noted.
Road Type: The numerical categorisation of the road types is done. 1 stands for highway. 2 stands for City 1 and City 2. 3 stands for Roundabout time.

![Test Image 1](https://github.com/Aarushi-1/Stress-analysis-using-ML-Algo/blob/master/Major%20Project%20Images/1_Dataset%20screenshot.png)

Fig – Screen shot of the dataset. 
Heart Rate: The heart rate is noted. It is a float value up to 2 decimal places. The range is between 63 to 113 bpm.
Body temperature: The body temperature reading is noted in this column. This is also a float value with 2 decimal places. 
Stress: The stress values are noted down in this column. The value ranges between 0 to 1. The value contains up to 6 decimal places. With 0 being the least stressed to 5 being the most stressed reading.
Scale: The stress scale is set between 1 to 5. The numerical values from thee stress column are mapped here with equal divisions.

The image below shows detailed view of the datset. dataset.describe() and dataset.shape() functions were used.

![describe dataset](https://github.com/Aarushi-1/Stress-analysis-using-ML-Algo/blob/master/Major%20Project%20Images/2_Dataset%20shape%20and%20describe.png)

Evaluation paraemeters are shown below with accuracy, f1 score, support precision etc. metrices.

![Evaluation Parameters](https://github.com/Aarushi-1/Stress-analysis-using-ML-Algo/blob/master/Major%20Project%20Images/3_Evaluation.png)

## Stress prediction using custom values

The following output is predicted for the given custom inputs is:

![Prediction result](https://github.com/Aarushi-1/Stress-analysis-using-ML-Algo/blob/master/Major%20Project%20Images/4_Predicted%20Output.png)

## Graphical Representations:

![coloured stress levels](https://github.com/Aarushi-1/Stress-analysis-using-ML-Algo/blob/master/Major%20Project%20Images/Mapped%20color%20coded%20graph.png)

Fig – Showing the mapping between the actual stress values and the scale of stress coded between 1-5.

![Error Image](https://github.com/Aarushi-1/Stress-analysis-using-ML-Algo/blob/master/Major%20Project%20Images/5_Error%20Rate%20Graph.png)

The graph shows the error rate for the algorithm.

![individual plots](https://github.com/Aarushi-1/Stress-analysis-using-ML-Algo/blob/master/Major%20Project%20Images/Individual%20graphs.png)

Fig-Individual graphs for the feature list.

![line plot](https://github.com/Aarushi-1/Stress-analysis-using-ML-Algo/blob/master/Major%20Project%20Images/Line%20Plot.png)

Fig-Line plot for the feature list

![error rate](https://github.com/Aarushi-1/Stress-analysis-using-ML-Algo/blob/master/Major%20Project%20Images/5_Error%20Rate%20Graph.png)

Fig-Error rate graph
