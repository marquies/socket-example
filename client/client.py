#!/usr/bin/python
import socket
import sys
import ensclient

# Edge Network Service: specific globals - START
# NOTE: Update this section as per onboarded field parameters
EDGE_USER_ID = 'devtest'
EDGE_APP_NAME = 'socket'

EDGE_MS_NAME = 'socket'
EDGE_NW_BIND_NAME = 'socket-network'

EDGE_F_SEPARATOR = '.'

EDGE_APP_ID = EDGE_USER_ID + EDGE_F_SEPARATOR + EDGE_APP_NAME
EDGE_NW_BINDING_ID = EDGE_MS_NAME + EDGE_F_SEPARATOR + EDGE_NW_BIND_NAME
# Edge Network Service: specific globals - END


# Edge Network Service: Initializations - START
# Initialize Edge connection -
#   - this will discover the nearest suitable cloudlet
#   - request for an application instance to be created
edge_conn_client = ensclient.ENSClient(EDGE_APP_ID)
edge_conn_session = None
edge_sess_endpoint = None


if edge_conn_client.init():
    # Application instance created on Edge, create connection on the
    # provided endpoint
    edge_conn_session = edge_conn_client.connect(EDGE_NW_BINDING_ID)

    edge_sess_endpoint = ensclient.ENSEndpoint(edge_conn_session.binding["endpoint"])
    print('Endpoints received from Edge-{}:{}'.format(
        edge_sess_endpoint.host, edge_sess_endpoint.port))
    host = edge_sess_endpoint.host
    port = edge_sess_endpoint.port

    # Connection handle must be passed to the CalculatorService
else:
    print('Failed to initialize connection with Edge')
    sys.exit(1)

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.connect((host, int(port)))

    client_socket.send(str.encode("start"))
    print("Sent start signal")
except Exception as e:
            print(e)


try:
    r = client_socket.recv(90456)
    print("Received: %s", r)
except Exception as e:
    print(e)
