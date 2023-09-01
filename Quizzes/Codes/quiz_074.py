from math import ceil


def build_data_pkg(mac_rx: str, ip_rx: str, mac_sx: str, ip_sx: str, data: str):
    ip_mac = f"{mac_rx}|{ip_rx}|{mac_sx}|{ip_sx}|"
    output = []
    length = ceil(len(data) / 4)
    for i in range(length):
        load = data[:4]
        if len(load) < 4:
            load = data
        data = data[4:]
        output.append(f"{ip_mac}{i}|{load}")

    return output


data_package = build_data_pkg("8C:31:03:4F:CE:DB", "192.168.0.1", "7A:7A:A7:C2:44:FB", "192.168.0.2", "Hello world")
print(data_package)
