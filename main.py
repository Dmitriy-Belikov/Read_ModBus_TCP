import time
import numpy as np
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp
import struct

server_host = '127.0.0.1'
server_port = 502

client = modbus_tcp.TcpMaster(host=server_host, port=server_port)
#client.connect()

start_address = 0
items = 6
while True:
    value = client.execute(1, cst.READ_HOLDING_REGISTERS, start_address, items*2)
    d16 = np.array(value).astype(dtype=np.int16)
    f32 = d16.view(dtype=np.float32)
    print(f32)
    time.sleep(1)

client.close()