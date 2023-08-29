import csv
import speedtest
import datetime
import time


def test_wifi_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = round(st.download() / 1_000_000, 1)  # Convert to Mbps and round to 1 decimal point
    upload_speed = round(st.upload() / 1_000_000, 1)  # Convert to Mbps and round to 1 decimal point
    ping = round(st.results.ping, 1)  # Round ping to 1 decimal point

    return download_speed, upload_speed, ping


def save_to_csv(filename, data):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def main():
    csv_filename = 'wifi_speed_test_results.csv'
    try:
        with open(csv_filename, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Download Speed (Mbps)', 'Upload Speed (Mbps)', 'Ping (ms)'])

    except FileExistsError:
        pass

    while True:
        timestamp = datetime.datetime.now()
        download_speed, upload_speed, ping = test_wifi_speed()
        data = [timestamp, download_speed, upload_speed, ping]

        save_to_csv(csv_filename, data)
        print("Speed test results saved to", csv_filename)

        # Wait for 15 minutes (900 seconds) before the next speed test
        time.sleep(900)


if __name__ == "__main__":
    main()
