# scripts/

可执行脚本目录。**当有重复的转换 / 校验 / 批处理逻辑时**放进这里，不是占位。

## 当前内容

| 文件 | 用途 |
|---|---|
| `check_openspec.py` | 检查 OpenSpec Markdown 是否覆盖 9 节必备小节（按 [references/openspec-template.md](../references/openspec-template.md)） |

## 何时新增脚本

- 同一段检查 / 转换逻辑 ≥ 3 次出现在不同 OpenSpec 中 → 提脚本
- 校验、迁移、回滚演练里**确定性高、人工易错**的步骤 → 提脚本
- 仅一次性手动动作 → 不需要进 scripts/，留在 PR 描述里即可

## 写法约定

- 用 `python3` 兼容 Python 3.11+
- 入口接受文件路径或 `--root` 目录
- 退出码：0 成功 / 1 业务失败 / 2 用法错
- 跑通脚本后再合并；不通过 quick_validate 的脚本禁止合入
