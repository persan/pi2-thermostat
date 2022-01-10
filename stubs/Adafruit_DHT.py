DHT11 = 1
data = [[20.0, 0.0],
        [20.0, 1.0],
        [20.0, 2.0],
        [20.0, 3.0],
        [20.0, 4.0],
        [20.0, 5.0],
        [20.0, 6.0],
        [20.0, 7.0],
        [20.0, 8.0],
        [20.0, 9.0],
        [20.0, 10.0]]
index = 0
def read_retry(a, b):
    global index
    index = (index + 1) % len(data)
    return data[index]

if __name__ == "__main__":
    for i in range(0,30):
        print (read_retry(10,1))
