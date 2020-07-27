# Sensor simulation miniproject

![Actions Status](https://github.com/BostonUniversitySeniorDesign/2020-sensor-miniproject/workflows/ci/badge.svg)

The Fall 2020 sensor miniproject uses simulated internet-connected sensors.
Simulated sensors are used to test proposed designs against impairments including delayed, missing or incorrect data.
The IoT simulator
[ws_server.py](./ws_server.py)
emits data packets with random timing to the backend service
[ws_client.py](./ws_client.py).

## Assignment

This assignment is done in two-person teams, where each student should run the simulation and work together on the analysis and turn in **one joint report**.
The maximum number of points possible for this assignment is 100.

This simulation was tested to work on standard computers such as a laptop or Raspberry Pi.
If you try to run it in a virtual machine or browser-based cloud resource, the code may not work or require additional system configuration.
Typically sensor prototypes are worked on with a laptop, so that is the suggested use case for this assignment.


### Task 0: setup Python websockets

(15 points total for this section)

Prototyping across STEM disciplines is typically done with Python.
If you don't already have Python,
[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
is a small but powerful Python distribution for MacOS, Windows and Linux.
The Microsoft
[Windows Store also has Python](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab).
Python 3.8 is recommended for this assignment and in general, particularly if you are using a Windows computer.

Websockets are used for this task as they are lightweight and suited to irregular data streams.
Python
[websockets](https://websockets.readthedocs.io/)
provide server / client Websockets API.
Python websockets is installed (along with prerequisites) from Terminal:

```sh
python -m pip install websockets
```

Please "fork" this GitHub repository and place all your assignment responses and results into **Report.md** in your repository.
By forking this repo, you will be able to more easily integrate any updates I might make to this repo as bugs are discovered or other enhancements are made.
Report.md is a Markdown formatted text file with links to or inline figures of the plots generated in PNG format.

A simple example is run using two Terminal windows.
In the first Terminal run:

```sh
python ws_server.py
```

then open another Terminal / Command Prompt and type:

```sh
python ws_client.py
```

#### Task 0 points

(15 points for this section)

* setup and run the Python code as described above on your computer
* What is the greeting string issued by the server to the client upon first connecting?

### Task 1: data flow

Python standard library includes
[JSON](https://docs.python.org/3/library/json.html),
which is a common serialization format used to interchange data amongst networked devices.
Normally we would store the retrieved data into a database.
However here since we're just testing for a fixed amount of time and this is a short assignment, we just store the JSON data to a file as-is, line by line as they come in.

Python file operations are generally done via
[open()](https://docs.python.org/3/library/functions.html#open)
and can use syntax like:

```python
file = open("myfile.txt", mode="a")

# other code

file.write(txt + "\n")
file.flush()

# other code

file.close()
```

While file I/O streaming and many other options exist, for this assignment we can simply write within the main `for` or `while` loop.

#### Task 1 points

(20 points total for this section)

* Add Python code to ws_client.py that saves the JSON data to a text file as it comes in (message by message)

### Task 2: Analysis

Run the server and client and collect data.
Run them for at least 20 minutes so that you get hundreds of data values.
The data will be stored to a text file that you implemented in Task #1 (be sure this file is actually saving data incrementally before you let it run for a while).

#### Task 2 points

(20 points total for this section)

* what are the median and variance observed from the temperature data (at least 100 values)  [3 points]
* what are the median and variance observed from the occupancy data (at least 100 values)  [3 points]
* plot the probability distribution function for each sensor type? [6 points]
* What is the mean and variance of the *time interval* of the sensor readings? Please plot its probability distribution function. Does it mimic a well-known distribution for connection intervals in large systems? [8 points]

### Task 3: Design

(25 points total for this section)

* implement an algorithm that detects anomalies in sensor data
* Does a persistent change in these sensor statistics always indicate a failed sensor?
* What are possible bounds on temperature for each room type?

### Task 4: Conclusions

(20 points total for this section)

Please create Report.md, a Markdown format text file in the top level of your GitHub repository.
The report should be concise, the equivalent of about 2 pages.
Please compose the report as if it were an informal engineering memo to give to your manager in a workplace.

Some points to think about:

* how is this simulation reflective of the real world?
* how is this simulation deficient? What factors does it fail to account for?
* how is the difficulty of initially using this Python websockets library as compared to a compiled language e.g. [C++ websockets](https://github.com/facundofarias/awesome-websockets#c-1)
* would it be better to have the server poll the sensors, or the sensors reach out to the server when they have data?
