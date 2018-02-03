# socket-example

This example demonstrates how to create and connect to a socket.

## Run Instructions

Follow these steps to run the example on EIB.

### Prerequesits

* Have EIB installed
* Have a Python Client SDK (>2.0.0) downloaded

## Setup

* Download or Clone Repo
* Change directory to app: `cd app`
* Compile socket
    ```
    $> gcc socket.c -o socket
    ```
* Build Docker Image
    ```
    $> docker build -t devtest/socket .
    ```
* Onboard to EIB
    ```
    $> dtedgectl onboard -T application -f socket.yaml
    ```
* Change directory to client: `cd ../client`
* Copy Python client SDK files (`ensclient.py`, `mecsdk.conf`)
* Edit mecsdk.conf, check correct DiscoveryURL value for local setup
* Run Client
    ```
    $> python client.py
    2018-02-03 21:17:43,192 INFO     ensclient.py      535 Loading MEC SDK settings
    2018-02-03 21:17:43,211 INFO     ensclient.py      665 1 probe candidate cloudlets found by discovery
    2018-02-03 21:17:43,211 INFO     ensclient.py      397 [Cloudlet:eib.local][App:socket]: Probe START
    2018-02-03 21:17:43,215 INFO     ensclient.py      464 [Cloudlet:eib.local][App:socket]: Completed 10 RTT probes. Mean RTT:0.00015811920166
    2018-02-03 21:17:44,217 INFO     ensclient.py      678 Probes completed for all Cloudlet candidates
    2018-02-03 21:17:44,217 INFO     ensclient.py      690 Sorted Probe Report
    2018-02-03 21:17:44,218 INFO     ensclient.py      691 ===================
    2018-02-03 21:17:44,218 INFO     ensclient.py      694 Cloudlet: eib.local RTT: 0.00015811920166
    2018-02-03 21:17:44,218 INFO     ensclient.py      696 Selected cloudlet for provision: eib.local
    2018-02-03 21:17:44,218 INFO     ensclient.py      711 Requesting provisioning of socket
    2018-02-03 21:17:46,003 INFO     ensclient.py      717 Provision completed for socket
    2018-02-03 21:17:46,003 INFO     ensclient.py      302 Create ENSNetworkSession to interface socket.socket-network on application devtest.socket
    2018-02-03 21:17:46,003 INFO     ensclient.py      313 Connecting to Network interface socket.socket-network at {u'networkId': u'socket-network', u'endpoint': u'tcp://10.0.2.15:60713'}
    Endpoints received from Edge-10.0.2.15:60713
    Sent start signal
    ('Received: %s', 'Sat Feb  3 20:17:47 2018\r\n')
    2018-02-03 21:17:57,511 INFO     ensclient.py      819 App: [socket], Deployment Id: [1517502422] deleted.
    ```
