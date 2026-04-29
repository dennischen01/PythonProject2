# LLMOps

基于 Flask + LangChain 构建的 LLM 应用运维平台。

## 项目架构

采用 7 层架构设计，各层职责清晰、解耦合理。

| 层级 | 模块 |
|------|------|
| **表示层** | PC 网站 / 开放 API / APP |
| **接入层** | Nginx / 负载均衡 |
| **控制层** | AI 应用模块 / 用户模块 / 授权模块 / 插件模块 |
| **服务层** | LLM 应用服务 / 上传服务 / 授权服务 / 文本嵌入服务 |
| **核心层** | 多 LLM 集成 / Agent 集成 / LangChain 封装 |
| **存储层** | PostgreSQL / Redis / 向量数据库 / 对象存储 |
| **资源层** | Linux 服务器 / Docker 虚拟机 / K8s |

**表示层**：面向终端用户的交互入口，支持 PC 网站、开放 API 及移动端 APP 三种访问方式。

**接入层**：通过 Nginx 统一接收外部流量，结合负载均衡策略将请求分发至后端服务。

**控制层**：承载核心业务逻辑，包括 AI 应用管理、用户体系、权限授权及插件扩展能力。

**服务层**：提供具体的功能服务，涵盖 LLM 调用、文件上传、授权校验与文本向量化。

**核心层**：封装底层 AI 能力，集成多种 LLM 提供商、Agent 编排框架及 LangChain 工具链。

**存储层**：负责数据持久化，PostgreSQL 存储结构化数据，Redis 负责缓存，向量数据库支撑语义检索，对象存储管理文件资源。

**资源层**：基础设施底座，基于 Linux 服务器运行，通过 Docker 容器化部署，K8s 负责集群编排与弹性扩缩容。

## 目录结构

```
.
├── app.py                          # 应用启动入口
├── requirements.txt                # 第三方依赖
├── .env                            # 环境变量配置
├── .gitignore
│
├── app/                            # 应用入口集合
│   ├── __init__.py
│   └── http/                       # HTTP 入口
│
├── config/                         # 应用配置
│   ├── __init__.py
│   ├── config.py                   # 多环境配置（Dev / Prod / Test）
│   └── default_config.py           # 默认配置基类
│
├── internal/                       # 应用内部模块
│   ├── core/                       # LLM 核心层：LangChain、Embedding 等非业务逻辑
│   │   ├── agent/                  # Agent 编排
│   │   ├── chain/                  # LangChain 链路封装
│   │   ├── prompt/                 # Prompt 模板管理
│   │   ├── model_runtime/          # 模型运行时适配
│   │   ├── moderation/             # 内容审核
│   │   ├── tool/                   # 工具集成
│   │   └── vector_store/           # 向量存储适配
│   │
│   ├── exception/                  # 通用公共异常
│   │   ├── __init__.py
│   │   └── exception.py            # AppException 及子类定义
│   │
│   ├── extension/                  # Flask 扩展初始化
│   │   ├── __init__.py
│   │   └── database_extension.py   # SQLAlchemy + Flask-Migrate
│   │
│   ├── handler/                    # 路由处理器（控制器层）
│   │   ├── __init__.py
│   │   └── account_handler.py      # 账户注册 / 登录接口
│   │
│   ├── middleware/                 # 应用中间件
│   │   ├── __init__.py
│   │   └── middleware.py           # login_required 等校验装饰器
│   │
│   ├── migration/                  # 数据库迁移文件（Flask-Migrate 自动生成）
│   │   └── versions/
│   │
│   ├── model/                      # 数据库模型
│   │   ├── __init__.py
│   │   └── account.py              # Account 模型
│   │
│   ├── router/                     # 路由注册
│   │   ├── __init__.py
│   │   └── router.py               # 统一注册所有 Blueprint 路由
│   │
│   ├── schedule/                   # 定时任务 / 调度任务
│   │   └── __init__.py
│   │
│   ├── schema/                     # 请求 / 响应结构体（dataclass / Pydantic）
│   │   ├── __init__.py
│   │   └── account_schema.py
│   │
│   ├── server/                     # Flask 应用工厂（与 app/ 对应）
│   │   ├── __init__.py
│   │   └── app.py                  # create_app()
│   │
│   ├── service/                    # 业务服务层
│   │   ├── __init__.py
│   │   ├── account_service.py      # 账户注册 / 登录业务
│   │   └── oauth_service.py        # OAuth 授权业务
│   │
│   └── task/                       # 任务队列（即时任务 + 延迟任务）
│       └── __init__.py
│
├── pkg/                            # 可复用扩展包
│   ├── __init__.py
│   └── oauth/
│       ├── __init__.py
│       └── github_oauth.py         # GitHub OAuth 授权流程
│
├── storage/                        # 本地文件存储
└── test/                           # 测试目录
```

## 快速开始

### 环境要求

- Python 3.11+
- PostgreSQL 15+
- Redis 7+

### 安装依赖

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 配置环境变量

复制 `.env` 并填写实际配置：

```bash
cp .env .env.local
```

```dotenv
FLASK_ENV=development
DATABASE_URL=postgresql://user:password@localhost:5432/llmops
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
```

### 初始化数据库

```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```

### 启动服务

```bash
flask run
# 或
python app.py
```

服务默认运行在 `http://localhost:5000`。

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/account/register` | 账户注册 |
| POST | `/api/account/login` | 账户登录 |

## 技术栈

| 类别 | 技术 |
|------|------|
| Web 框架 | Flask 3.x |
| ORM | SQLAlchemy 2.x + Flask-Migrate |
| 数据库 | PostgreSQL |
| 缓存 | Redis |
| AI 框架 | LangChain 0.2.x |
| 任务队列 | Celery |
| 认证 | JWT (PyJWT) |
