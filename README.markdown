# Cyberdudebivash-mon-util

Welcome to **Cyberdudebivash-mon-util**, an open-source monitoring tool designed to provide real-time system performance tracking and anomaly detection. Inspired by top monitoring solutions like Datadog, Dynatrace, New Relic, Prometheus, Zabbix, and Grafana, this tool is built with Python and offers a lightweight yet powerful way to monitor CPU, memory, and disk usage.

## Features

- **Real-Time Metrics**: Monitor CPU, memory, and disk usage with live updates.
- **AI-Powered Anomaly Detection**: Utilize a simple neural network (Dynatrace-style) and Zabbix-style statistical methods to identify anomalies.
- **Custom Dashboards**: Generate visual representations of metrics saved as PNG files using Matplotlib.
- **Log Monitoring**: Track system logs for additional context (configurable via a log file path).
- **Cross-Platform**: Works on Linux, macOS, and Windows with OS-specific log support.
- **Extensible**: Open-source design allows for customization and enhancement.

## Installation

### Prerequisites
- Python 3.6 or higher
- Required Python libraries: `psutil`, `pandas`, `matplotlib`, `numpy`, `scipy`, `torch`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/14mb1v45h/Cyberdudebivash-mon-util.git
   cd Cyberdudebivash-mon-util
   ```
2. Install dependencies:
   ```bash
   pip install psutil pandas matplotlib numpy scipy torch
   ```
3. Run the script:
   ```bash
   python cyberdudebivash_mon_util.py
   ```

## Usage

### Running the Tool
- Execute the script to start monitoring:
  ```bash
  python cyberdudebivash_mon_util.py
  ```
- The tool runs for 5 minutes by default (adjustable via `monitor_duration` in the code) and generates a `dashboard.png` file.
- Press `Ctrl+C` to stop monitoring early.

### Configuration
- Edit the `main()` function in the script to customize:
  - `monitor_duration`: Duration in seconds (default: 300).
  - `interval`: Sampling interval in seconds (default: 5).
  - `log_file`: Path to a log file (e.g., `r'C:\test.log'` on Windows).
  - `thresholds`: Alert thresholds for CPU, memory, and disk (default: 80%, 80%, 90%).

### Example Output
- Console displays real-time metrics, alerts, logs, and anomaly detection results.
- A `dashboard.png` file is created with graphs for CPU, memory, and disk usage.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests. For major changes, open an issue first to discuss.

1. Fork the repo.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature-name"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- **Author**: 14mb1v45h
- **GitHub**: [https://github.com/14mb1v45h](https://github.com/14mb1v45h)
- **LinkedIn**: https://linkedin.com/in/bivash-nayak/

## Acknowledgments
- Inspired by monitoring giants: Datadog, Dynatrace, New Relic, Prometheus, Zabbix, and Grafana.
- Built with love using Python and open-source libraries.

## Copyright
  COPYRIGHT@CYBERDUDEBIVASH SEPTEMBER 2025