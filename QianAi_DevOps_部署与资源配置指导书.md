# QianAi DevOps 工程资源配置与部署说明指导书

---

## 一、功能概述

本工程集成：
- 代码自动构建与打包
- 自动化部署与回滚
- 自动化测试与用例统计
- Docker 镜像构建与部署
- Web 可视化指标展示
- 基于 transformers 大模型的日志智能分析
- 修改文档的注释
---

## 二、推荐硬件资源配置

### 1. 基础环境（适合中小团队/测试）
- CPU：4核及以上
- 内存：16GB 及以上
- 硬盘：100GB SSD
- 操作系统：Ubuntu 20.04+/CentOS 7+/Windows Server 2019+
- 网络：千兆网卡

### 2. 生产/大团队（高并发/大日志量）
- CPU：8核及以上
- 内存：32GB 及以上
- 硬盘：500GB SSD+
- GPU（可选）：NVIDIA 8GB 显存及以上（如需高效大模型推理）

---

## 三、软件与依赖环境

- Python 3.8 及以上
- pip 20+，建议用 venv/conda 虚拟环境
- requirements.txt 依赖：flask、transformers、torch、pytest 等
- Docker CE 20+，Docker Compose（如需多服务编排）
- GitLab Runner（如用 GitLab CI）
- SSH 免密登录（自动部署/回滚）
- 日志目录（如 logs/devops.log），Web 服务需有读权限

---

## 四、部署与配置流程

1. 克隆代码仓库，进入工程目录
2. 配置 Python 虚拟环境，安装 requirements.txt
3. 安装并配置 Docker、GitLab Runner
4. 配置 SSH 免密，确保 CI/CD 能远程操作目标服务器
5. 配置 .gitlab-ci.yml，填写实际服务器地址、路径、镜像仓库等变量
6. 启动 Web 服务（`python src/qianai/webapp/metrics_server.py`），访问 http://localhost:5000
7. 日志分析功能需准备 logs/devops.log，或对接实际 CI/CD 日志产出

---

## 五、资源与性能建议

- 日志分析和大模型推理建议单独部署，避免影响主业务服务
- 并发高时，建议将 Web 服务、CI/CD、日志分析分布式部署
- 定期清理无用镜像、历史日志，释放磁盘空间
- 监控系统资源，及时扩容

---

## 六、安全与合规

- 生产环境建议开启 HTTPS，限制管理端口访问
- 定期备份代码、数据库、日志
- 配置操作审计与告警，防止异常操作

---

## 七、常见问题与优化建议

- 大模型首次加载慢，可提前预热或用轻量模型
- 资源不足时，优先扩容内存和磁盘
- 日志量大时，建议分片存储并定期归档

---

如需更详细的分布式部署、云平台适配、性能调优等方案，请根据实际业务场景补充说明。
