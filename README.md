# Real-Time-Log-Monitoring-Solution
Developed a real-time log monitoring system with a server-side component and web-based client for viewing updates in a continuously growing log file:

- **Server-side**: Designed and implemented a server that efficiently monitors an append-only log file and streams updates to multiple clients in real-time. Optimized the system to retrieve the last 10 lines from large log files (several GB in size) without retransmitting the entire file.
- **Client-side**: Built a web-based interface accessible at `http://localhost/log`, displaying the last 10 lines of the log file upon load. Implemented real-time updates without requiring page refresh, using persistent connections (e.g., WebSockets) to stream new log entries as they happen.
- **Challenges addressed**: Ensured low-latency streaming, supported concurrent clients, and minimized memory usage by only processing new log entries instead of reloading the entire file.

## How to Run
1. **Start WebSocket Server**:
   ```bash
   python server-side.py
   ```
2. **Serve Client HTML**:
   ```bash
   python server.py
   ```
3. **Access Client**: Open a browser and navigate to `http://localhost:8000/log.html`.
