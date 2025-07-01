# Docker 容器日志监控工具

这是一个简单的基于 Web 的工具，用于监控主机上运行的 Docker 容器的日志。

## 功能

- 列出所有 Docker 容器（包括运行中和已停止的）。
- 查看任何选定容器的日志。
- 自动刷新容器列表。

## 如何运行

1.  **克隆仓库：**

    ```bash
    git clone <repository-url>
    cd docker-log-monitor
    ```

2.  **使用 Docker Compose 构建并运行应用：**

    ```bash
    docker compose up --build
    ```

3.  **打开你的网页浏览器并访问：**

    [http://localhost:5000](http://localhost:5000)

## 项目结构

```
.
├── app
│   ├── static
│   ├── templates
│   │   └── index.html
│   └── main.py
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```