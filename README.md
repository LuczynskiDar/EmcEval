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

#### DataReader
There are 3 classes:
 - Common, containing common properties and methos

* Class Commons
``` Python
class Commons:
    def __init__(self, filename: str):
```

* Class ActToolLog

``` Python
class ActToolLog(Commons):
    def __init__(self, filename: str):
        super(ActToolLog, self).__init__(filename)
```
* Class GeneratorLog
``` Python
class GeneratorLog(Commons):
    def __init__(self, filename: str):
        super(GeneratorLog, self).__init__(filename)
```
