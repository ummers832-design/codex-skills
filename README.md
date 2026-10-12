# codex-skills

个人维护的 [Codex](https://github.com/openai/codex) Skill 集合。每个 skill 一个子目录，
遵循 [Codex Skill 官方结构](https://github.com/openai/codex/tree/main/.codex/skills/.system/skill-creator)：

```
<codex-skills>/
├── .gitignore
├── README.md                        ← 本文件
└── <skill-name>/                    ← 每个 skill 一目录
    ├── SKILL.md                     ← 必选，YAML frontmatter + Markdown
    ├── agents/openai.yaml           ← 可选，UI 元数据
    ├── references/                  ← 可选，按需加载的文档
    ├── scripts/                     ← 可选，可执行脚本
    └── assets/                      ← 可选，静态资源
```

## 已收录 skill

| skill | 一句话 | 状态 |
|---|---|---|
| [sdd-batch](./sdd-batch) | 分批 SDD（Software Design Document）开发规范骨架：判断是否需要 SDD、按业务路径分批、编码前清单对照 | 已发布 |

## 安装到本机 `~/.codex/skills/`

```bash
# 整体 clone 后挑需要的
git clone git@github.com:ummers832-design/codex-skills.git ~/codex-skills-src
ln -sfn ~/codex-skills-src/sdd-batch ~/.codex/skills/sdd-batch
```

> 用 symlink 而不是拷贝：以后仓库里改了 `sdd-batch/` 直接生效，不用重新链接。

## 新增一个 skill

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/init_skill.py <new-skill> \
  --path "$(pwd)" \
  --resources scripts,references,assets
```

然后在 `<new-skill>/SKILL.md` 里写 frontmatter（name + description）+ Markdown 正文，
跑 `python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py <new-skill>` 自检。

## 验证 skill 完整性

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-name>
```

## 许可

MIT — 自由使用、修改、再分发。
