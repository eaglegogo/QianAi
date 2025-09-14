from flask import Flask, render_template
import datetime

app = Flask(__name__)

# 假设数据来源于日志或数据库，这里用静态数据模拟
# 实际可通过解析CI日志、API等方式动态获取
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
    return render_template('metrics.html', metrics=metrics_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
