def get_hostname():
    hostname = input("Enter hostname: ")
    return hostname


def get_ip():
    ip = input("Enter IP address: ")
    return ip


def get_metrics():
    metrics = []

    print("Enter system metrics (type 'done' to finish):")

    while True:
        metric = input("Metric: ")

        if metric.lower() == "done":
            break

        metrics.append(metric)

    return metrics


def display_info(hostname, ip, metrics):
    print("\n--- System Monitoring Configuration ---")
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip}")
    print("Metrics:")

    for metric in metrics:
        print(f" - {metric}")


def main():
    hostname = get_hostname()
    ip = get_ip()
    metrics = get_metrics()

    display_info(hostname, ip, metrics)


if __name__ == "__main__":
    main()