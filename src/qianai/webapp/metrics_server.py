import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from flask import Flask, render_template
from src.qianai.webapp.ai_log_analyzer import analyze_log
from src.qianai.monitor.simple_monitor import get_system_metrics, monitor_and_alert

app = Flask(__name__, static_folder='static')

# 静态模拟数据，实际可对接数据库或CI/CD接口
metrics_data = {
    'build_time': '2025-09-15 10:12:30',
    'build_duration': '1m 45s',
    'deploy_time': '2025-09-15 10:15:00',
    'deploy_duration': '2m 10s',
    'deploy_success_rate': '99.2%',
    'test_time': '2025-09-15 10:17:30',
    'test_duration': '1m 20s',
    'test_case_pass_rate': '97.5%'
}

@app.route('/')
def index():
    thresholds = {'cpu': 50, 'mem': 80, 'disk': 90}
    to_addr = 'admin@example.com'
    monitor_metrics, _ = monitor_and_alert(thresholds, to_addr)
    monitor_metrics_fmt = {k: f"{v:.1f}%" for k, v in monitor_metrics.items()}
    ai_log_result = analyze_log()
    return render_template('dashboard.html', metrics=metrics_data, monitor=monitor_metrics_fmt, ai_log=ai_log_result)

@app.route('/build')
def build():
    return render_template('build.html', metrics=metrics_data)

@app.route('/deploy')
def deploy():
    return render_template('deploy.html', metrics=metrics_data)

@app.route('/test')
def test():
    return render_template('test.html', metrics=metrics_data)

@app.route('/ai-log')
def ai_log():
    result = analyze_log()
    return render_template('ai_log.html', summary=result['summary'], errors=result['errors'])

@app.route('/monitor')
def monitor():
    thresholds = {'cpu': 50, 'mem': 80, 'disk': 90}
    to_addr = 'admin@example.com'
    monitor_metrics, alerts = monitor_and_alert(thresholds, to_addr)
    # 格式化百分比
    monitor_metrics_fmt = {k: f"{v:.1f}%" for k, v in monitor_metrics.items()}
    return render_template('monitor.html', monitor=monitor_metrics_fmt, alerts=alerts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
