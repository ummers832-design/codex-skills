# assets/

用于在生成 OpenSpec / 报告 / 文档时**直接引用的静态资源**。

## 当前内容

（暂无 — 在你需要一个稳定复用的"模板图""速查表""示例 ER""示例状态机图"等二进制或可引用资源时再放进来。）

## 何时新增资源

- 你发现自己画了 3 次同样的 ER 图骨架 → 提 assets/
- 团队需要"字段类型速查表""状态机符号表" → 提 assets/
- 跨多个 OpenSpec 引用的同一份 schema / 字典 / 样例数据 → 提 assets/

## 写法约定

- 文件名用 kebab-case：`er-diagram-base.png` `enum-state-machine.md`
- Markdown 资源保持小、聚焦；不复制粘贴整本规范
- 二进制资源（图片、PDF、压缩包）保持 ≤ 5 MB；超大文件用 LFS 或外链
- 引用时用相对路径 `assets/xxx` 让 skill 整体可移植
