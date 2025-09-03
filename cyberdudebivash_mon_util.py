import time
import os
import sys
import platform
import psutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import torch
import torch.nn as nn
from datetime import datetime

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(1, 1)
    
    def forward(self, x):
        return self.fc(x)

def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    mem_percent = memory.percent
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    return {
        'timestamp': time.time(),
        'cpu_percent': cpu_percent,
        'mem_percent': mem_percent,
        'disk_percent': disk_percent
    }

def monitor_logs(log_file):
    if not log_file or not os.path.exists(log_file):
        return ["No valid log file specified or file not found. Skipping log monitoring."]
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            logs = f.readlines()[-10:]
        return logs
    except Exception as e:
        return [f"Error reading log file: {str(e)}"]

def check_alerts(metrics, thresholds):
    alerts = []
    if metrics['cpu_percent'] > thresholds['cpu']:
        alerts.append(f"High CPU usage: {metrics['cpu_percent']}%")
    if metrics['mem_percent'] > thresholds['mem']:
        alerts.append(f"High Memory usage: {metrics['mem_percent']}%")
    if metrics['disk_percent'] > thresholds['disk']:
        alerts.append(f"High Disk usage: {metrics['disk_percent']}%")
    return alerts

def simple_anomaly_detection(data_series):
    if len(data_series) < 2:
        return []
    z_scores = np.abs(stats.zscore(data_series))
    anomalies = np.where(z_scores > 2)[0]
    return anomalies

def ai_anomaly_detection(data_series):
    if len(data_series) < 2:
        return []
    model = SimpleNN()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    loss_fn = nn.MSELoss()
    
    x = torch.tensor(list(range(len(data_series))), dtype=torch.float32).unsqueeze(1)
    y = torch.tensor(data_series, dtype=torch.float32).unsqueeze(1)
    
    for _ in range(100):
        pred = model(x)
        loss = loss_fn(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    pred = model(x).detach().numpy()
    residuals = np.abs(y.numpy() - pred)
    anomalies = np.where(residuals > np.mean(residuals) * 1.2)[0]
    return anomalies

def generate_dashboard(df, output_file='dashboard.png'):
    plt.figure(figsize=(12, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(df['timestamp'], df['cpu_percent'], label='CPU %', color='#1E90FF')
    plt.title('CPU Usage')
    plt.legend()
    
    plt.subplot(3, 1, 2)
    plt.plot(df['timestamp'], df['mem_percent'], label='Memory %', color='#32CD32')
    plt.title('Memory Usage')
    plt.legend()
    
    plt.subplot(3, 1, 3)
    plt.plot(df['timestamp'], df['disk_percent'], label='Disk %', color='#FFA500')
    plt.title('Disk Usage')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    print(f"Dashboard saved to {output_file}")

def main(monitor_duration=300, interval=5, log_file=None, thresholds={'cpu': 80, 'mem': 80, 'disk': 90}):
    print("Starting Cyberdudebivash-mon-util monitoring...")
    print("This tool incorporates features from the top 5 monitoring tools of 2025:")
    print("- Datadog: Unified observability for metrics and logs with real-time alerts")
    print("- Dynatrace: AI-powered anomaly detection using neural networks")
    print("- New Relic: Full-stack metrics monitoring and anomaly alerts")
    print("- Prometheus: Time-series data collection and storage using Pandas")
    print("- Zabbix: Threshold-based alerting and open-source adaptability")
    print("- Inspired by Grafana: Dashboard visualizations using Matplotlib")
    print("\nMonitoring will run for the specified duration. Press Ctrl+C to stop early.\n")
    
    if log_file:
        print(f"Monitoring log file: {log_file}")
    else:
        print("No log file specified. Skipping log monitoring.")
    
    data = []
    start_time = time.time()
    try:
        while time.time() - start_time < monitor_duration:
            metrics = get_system_metrics()
            data.append(metrics)
            
            alerts = check_alerts(metrics, thresholds)
            if alerts:
                print("ALERTS:")
                for alert in alerts:
                    print(f"  {alert}")
            
            if log_file:
                logs = monitor_logs(log_file)
                print(f"\nRecent Logs (as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}):")
                for log in logs:
                    print(f"  {log.strip()}")
            
            print("-" * 50)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    
    if data:
        df = pd.DataFrame(data)
        
        cpu_anomalies = simple_anomaly_detection(df['cpu_percent'])
        print(f"\nSimple Anomalies in CPU (Zabbix-style): {cpu_anomalies}")
        
        ai_anomalies = ai_anomaly_detection(df['cpu_percent'].values)
        print(f"AI Anomalies in CPU (Dynatrace-style): {ai_anomalies}")
        
        generate_dashboard(df)
    else:
        print("No data collected.")

if __name__ == "__main__":
    try:
        import psutil
    except ImportError:
        print("Warning: psutil not installed. Install with 'pip install psutil' for real metrics.")
        print("Using simulated data for demonstration.")
        def get_system_metrics():
            return {
                'timestamp': time.time(),
                'cpu_percent': np.random.uniform(10, 90),
                'mem_percent': np.random.uniform(20, 80),
                'disk_percent': np.random.uniform(30, 70)
            }
    
    os_type = platform.system()
    default_log = None
    if os_type == 'Linux':
        default_log = '/var/log/syslog'
    elif os_type == 'Darwin':
        default_log = '/var/log/system.log'
    elif os_type == 'Windows':
        default_log = r'C:\Windows\Logs\CBS\CBS.log'
        print(f"Default log set to {default_log}. Ensure you have read permissions or specify another path.")
    
    main(monitor_duration=300, interval=5, log_file=default_log)