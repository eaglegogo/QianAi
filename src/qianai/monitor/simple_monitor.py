import psutil
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def get_system_metrics():
    """采集主机CPU、内存、磁盘等基础指标"""
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'mem_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent
    }

def send_alert(subject, content, to_addr):
    """发送告警邮件（需配置实际邮箱）"""
    from_addr = 'your_alert_email@example.com'
    password = 'your_email_password'
    smtp_server = 'smtp.example.com'
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = Header('QianAi监控', 'utf-8')
    msg['To'] = Header('管理员', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    try:
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print('告警邮件已发送')
    except Exception as e:
        print('发送邮件失败:', e)

def format_percent(val):
    return f"{val:.1f}%"

def monitor_and_alert(thresholds, to_addr):
    """监控并触发告警"""
    metrics = get_system_metrics()
    alerts = []
    if metrics['cpu_percent'] > thresholds['cpu']:
        alerts.append(f"CPU使用率过高: {format_percent(metrics['cpu_percent'])}")
    if metrics['mem_percent'] > thresholds['mem']:
        alerts.append(f"内存使用率过高: {format_percent(metrics['mem_percent'])}")
    if metrics['disk_percent'] > thresholds['disk']:
        alerts.append(f"磁盘使用率过高: {format_percent(metrics['disk_percent'])}")
    if alerts:
        send_alert('QianAi监控告警', '\n'.join(alerts), to_addr)
    return metrics, alerts

if __name__ == '__main__':
    # 测试：CPU>50%、内存>80%、磁盘>90%时告警
    thresholds = {'cpu': 50, 'mem': 80, 'disk': 90}
    to_addr = 'admin@example.com'
    metrics, alerts = monitor_and_alert(thresholds, to_addr)
    print('当前指标:', {k: format_percent(v) for k, v in metrics.items()})
    if alerts:
        print('触发告警:', alerts)
    else:
        print('一切正常')
