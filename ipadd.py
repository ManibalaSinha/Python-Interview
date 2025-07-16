from collections import defaultdict

def find_top_ip(log_lines):
   ip_count = defaultdict(int)
   for line in log_lines:
      ip= line.split()[0]
      ip_count[ip] += 1
      max_ip = max(ip_count, key=ip_count.get)
   return max_ip, ip_count[max_ip]
logs=[
   
    "192.168.1.10 - - [10/Jul/2025:13:55:36] \"GET /index.html HTTP/1.1\" 200",
    "10.0.0.2 - - [10/Jul/2025:13:55:37] \"POST /login HTTP/1.1\" 302",
    "192.168.1.10 - - [10/Jul/2025:13:55:38] \"GET /dashboard HTTP/1.1\" 200",
    "192.168.1.10 - - [10/Jul/2025:13:55:40] \"GET /contact HTTP/1.1\" 200"

]
ip,count = find_top_ip(logs)
print(f"The IP with Most Hits is: {ip} ({count} times)")