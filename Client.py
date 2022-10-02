import socket
import time
from pathlib import Path
time.sleep(5)
soc = socket.socket()
port = 4321
soc.bind(('', port))
print("Client socket successfully created")
server_port = 9876
soc.connect(('127.0.0.1', server_port))
print("Successfully connected to Server")

# variable declaration
buffer_size = 4096

while True:
    userChoice = int(
        input("\n 1 Calculate PI \n 2 Add \n 3 Sort Array \n 4 Matrix Multiplication \n 5 Exit\n"))
    match userChoice:
        case 1:
            soc.send("1".encode())
            pi_result = soc.recv(buffer_size).decode()
            print("Value of PI is ", pi_result)
        case 2:
            add_input = (
                input("Enter the two numbers to add with space in between\n").split(" "))
            add_input = str([int(ele) for ele in add_input])
            soc.send(("2"+add_input).encode())
            add_result = soc.recv(buffer_size).decode()
            print("Addition of two numbers is ", add_result)
        case 3:
            sort_input = (
                input("Enter the array elements to sort with space in between\n").split(" "))
            sort_input = str([int(ele) for ele in sort_input])
            soc.send(("3"+sort_input).encode())
            sort_result = soc.recv(buffer_size).decode()
            print("Sorted numbers ", sort_result)
        case 4:
            matrix_input = []
            for i in range(0, 3):
                print("Enter the matrix elements", i+1)
                row1 = [int(ele) for ele in (input(
                    "Enter the elements of first row of matrix with space in between ").split(" "))]
                row2 = [int(ele) for ele in (input(
                    "Enter the elements of second row of matrix with space in between ").split(" "))]
                row3 = [int(ele) for ele in (input(
                    "Enter the elements of third row of matrix with space in between ").split(" "))]
                matrix_input.append((row1, row2, row3))

            soc.send(("4"+str(matrix_input)).encode())
            mul_result = soc.recv(buffer_size).decode()
            print("Resulted matrix after multiplication is ", mul_result)
        case 5:
            soc.send("5".encode())
            print("Connection closed")
            soc.close()
            break
