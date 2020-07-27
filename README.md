# 2020 sensor miniproject

The Fall 2020 sensor miniproject involves a set of simulated internet-connected sensors.
In today's global development and customer environment, we often use simulated sensors to stress-test infrastructure against impairments including:

* excessive traffic
* delayed / lost traffic
* incorrect data

## Motivation

Relevant to both senior design and real-world work, often money is not the problem, but time.
We cannot afford to wait a couple weeks for the sensor to arrive, we need to get to work right away with the infrastructure supporting that sensor.

During each stage of design iteration from concept through prototyping and scale to manufacturing, it is beneficial to simulate real-world situations to help uncover unexpected problems in the design or architecture.
Having an engineering wireframe that is iteratively filled in by disparate engineering teams maximizes design efficiency and time to market for local and global design teams.
This assignment is also motivated by the one-day or two-day interview processes that occur for advanced undergraduate and graduate jobs.

A key factor in this assignment is working in two-person teams, where the design and test responsibilities should be approximately evenly divided.

## Assignment

The "new normal" set in 2020 has made building HVAC management more important than ever.
Office, lab and classroom spaces may go unused for day weeks, then suddenly being used perhaps with windows open, and then unused again.
Monitoring room temperatures is an important proxy for events including:

* adequate airflow to the room
* detecting abandoned open windows
* comfort for occupants without wasting HVAC resources
* unexpected occupancy (non-authorized times)

The IoT simulator we provide has a daemon to which the simulated sensor nodes connect.
The sensor to daemon network is opaque and out of scope for the students' work.
This daemon emits data packets as they arrive (unpredictable timing and quantity of packets) to the backend service the teams provide.

## Example

WebSockets are used for this task as they are lightweight and suited to irregular data streams.
A simple example using the Python
[websockets](https://github.com/aaugustin/websockets)
package is run using two Terminal windows:

```sh
python ws_server.py
```

then open another Terminal / Command Prompt and type

```sh
python ws_client.py
```

Notice that text typed is reflected via the server.
An arbitrarily large number of clients can connect to the server and have independent conversations.
