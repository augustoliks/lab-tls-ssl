import ssl
import socket


SOCKET_ADRRESS = "localhost"
SOCKET_PORT = 5000

CERTIFICATE_FILE = "./_certs/root-ca.pem"
CERTIFICATE_FILE_PRIVATE_KEY = "./_certs/root-ca-key.pem"



def main():
    # First, create a context. The default settings are probably the best here.
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    # Load the CA (self-signed, in this case) and the corresponding private key (also self-signed, in this case)
    context.load_cert_chain(
        certfile=CERTIFICATE_FILE,
        keyfile=CERTIFICATE_FILE_PRIVATE_KEY
    )

    # Create a standard TCP socket, bind it to an address, and listen for connections
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_connection.bind((SOCKET_ADRRESS, SOCKET_PORT))
    socket_connection.listen()

    while True:
    
        # conn is a standard python socket, addr is where it originated
        conn, addr = socket_connection.accept()
    
        # wrap the standard socket with the SSLContext, now it is a secure connection
        with context.wrap_socket(conn, server_side=True) as secure_conn:
    
            # data can be read/sent just like as in standard sockets
            data = secure_conn.recv(1024)
            print(data)


if __name__ == "__main__":
    main()
