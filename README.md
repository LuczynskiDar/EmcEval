# EMC Evaluation
> Python project to match UUT log data with EMC generator log.

EMC Evaluation, a side project to support EMC data evaluation, written in Python 3. 
Scripts were written using PyCharm IDE, and later on the parsed data were analysed in
Jupyter using Pandas and visualised using Seaborn and Matplotlib.

## Data, Sripts and Notebook

### Data 
Source data are located in /Data folder. 

#### Generator log file
EMC test generator log, text file.
* Monitor.txt
#### UUT log file
Data logged by a service tool connected to the tested device.
* Test_results.txt

### Scripts
There are 2 scripts DataReader, FrequencyFinder

#### [DataReader]
There are 3 classes:
* Class Commons, contains common properties and methods.
``` Python
class Commons:
    def __init__(self, filename: str):
```
* Class ActToolLog, inherits from class Commons, and contains unique properties to read UUT log file.
``` Python
class ActToolLog(Commons):
    def __init__(self, filename: str):
        super(ActToolLog, self).__init__(filename)
```
* Class GeneratorLog, inherits from class Commons, and contains unique properties to read Generator log file.
``` Python
class GeneratorLog(Commons):
    def __init__(self, filename: str):
        super(GeneratorLog, self).__init__(filename)
```
#### [FrequencyFinder](https://github.com/LuczynskiDar/EmcEval/blob/master/FrequencyFinder.py)
Contains FrequencyFinder class, used to find a generated frequency, time span in certain moment of time.
Frequency Finder instance is used in the Jupyter notebook, finds and adds found frequency generator's dataframe.
``` Python
class FrequencyFinder:
    def __init__(self, generator: dict):
```
### Notebook
[EmcEval notebook](https://github.com/LuczynskiDar/EmcEval/blob/master/EmcEval.ipynb) was created to parse both log files into Pandas data frame. Analyse the data using
helper functions for graphical representations, and other such as shifting column in the data frame
or adding test frequency markers, checking if the data are in desired specification.
