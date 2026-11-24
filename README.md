# aider-test

一个用于测试 [aider](https://aider.chat/) 的小型 Python 仓库。

## 目的

这个仓库只用来做实验，不是真实项目。里面故意放了一些方便测试编辑行为的小文件：

- 有明确边界的小函数，方便验证 `diff` / `whole` 编辑格式
- 有未使用的 import 和风格问题，方便触发 lint
- 有一个简单的 CLI 入口，方便做端到端改动测试

## 目录结构

```
aider-test/
├── main.py        # CLI 入口
├── calc.py        # 四则运算
├── utils.py       # 输入解析与格式化
└── README.md
```

## 运行

```bash
python3 main.py add 1 2
python3 main.py div 10 4
python3 main.py pow 2 10
```

## 已知问题

- `calc.py` 的 `div` 没有处理除零
- `utils.py` 的 `parse_number` 不支持负数
- `main.py` 缺少 `--help` 之外的参数校验

这些是留给 aider 改的。

## 注意

仓库内的 `.aider.conf.yml` 配置了 `lint-cmd`，在 aider 中每成功编辑一个 Python 文件就会执行一次。这是为了测试配置驱动的命令执行行为，**不是正常项目的配置方式**。
