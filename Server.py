import socket
import time
from pathlib import Path
import math
time.sleep(5)

# variable declaration
buffer_size = 4096


def calculate_pi():
    return math.pi


def add(i, j):
    return i + j


def convert_matrices(arr):
    arr = arr[1:-1].split(")")
    arr = arr[:-1]
    i = 0
    for _ in arr:
        if (arr[i])[0] == ',':
            arr[i] = (arr[i])[3:]
        else:
            arr[i] = (arr[i])[1:]
        i = i + 1

    i = 0
    for _ in arr:
        arr[i] = arr[i].split("]")
        j = 1
        matrix = arr[i]
        matrix = matrix[:-1]
        matrix[0] = matrix[0][1:]
        for _ in matrix:
            if j == 3:
                break
            matrix[j] = matrix[j][3:]
            j = j + 1
        arr[i] = matrix
        i = i + 1

    i = 0
    for _ in arr:
        j = 0
        for __ in _:
            print(i, j)
            arr[i][j] = str("[" + arr[i][j] + "]")
            arr[i][j] = convert_array(arr[i][j])
            j = j + 1
        arr[i] = tuple(arr[i])
        i = i + 1
    return arr


def convert_array(arr):
    arr = arr[1:-1].split(",")
    i = 0
    for _ in arr:
        arr[i] = int(arr[i].replace(" ", ""))
        i = i + 1
    return arr


def multiply_matrix(matrix):
    i = matrix[0]
    j = matrix[1]
    result = [[sum(a * b for a, b in zip(i_row, j_col)) for j_col in zip(*j)] for i_row in i]
    i = result
    j = matrix[2]
    result = [[sum(a * b for a, b in zip(i_row, j_col)) for j_col in zip(*j)] for i_row in i]
    return result


soc = socket.socket()
port = 9876
soc.bind(('', port))

print("Socket successfully connected to Client")
soc.listen(1)
conn, addr = soc.accept()
print(f"Connected by address {addr}",)

while True:
    input_data = conn.recv(buffer_size).decode()
    userChoice = input_data[0]
    result = ''
    input_data = input_data[1:]
    match userChoice:
        case "1":
            result = math.pi
        case "2":
            result = sum(convert_array(input_data))
        case "3":
            arr = convert_array(input_data)
            arr.sort()
            result = arr
        case "4":
            result = multiply_matrix(convert_matrices(input_data))
        case "5":
            print("Server socket connection closed successfully")
            soc.close()
            break

    conn.send(str(result).encode())
