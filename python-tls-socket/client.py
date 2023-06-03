import ssl
import socket


SERVER_ADDRESS = "localhost"
SERVER_PORT = 5000

CERTIFICATE_FILE = "./_certs/root-ca.pem"


def main():
    # Wrap the socket, just as like in the server.
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Create a context, just like as for the server
    context = ssl.create_default_context()

    # Load the server's CA
    context.load_verify_locations(CERTIFICATE_FILE)

    tls_socket_connection = context.wrap_socket(socket_connection, server_hostname=SERVER_ADDRESS)

    # Connect and send data! Standard python socket stuff can go here.
    tls_socket_connection.connect((SERVER_ADDRESS, SERVER_PORT))
    tls_socket_connection.sendall(b"Hello, server! This was encrypted.")


if __name__ == "__main__":
    main()
