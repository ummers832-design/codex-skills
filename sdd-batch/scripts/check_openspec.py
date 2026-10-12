#!/usr/bin/env python3
"""
check_openspec.py — OpenSpec 单批规格的结构校验器

按 references/openspec-template.md 的 9 节骨架，检查一份 OpenSpec Markdown
是否覆盖所有必需小节。

用法：
    python3 scripts/check_openspec.py <path-to-openspec.md>
    python3 scripts/check_openspec.py --root <directory>      # 递归扫描

退出码：
    0  — 全部节存在
    1  — 缺节
    2  — 文件不存在 / 用法错
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


# 模板里 9 个一级 / 二级节标题。匹配宽松（前后空格、冒号差异忽略）。
REQUIRED_SECTIONS: list[str] = [
    "元信息",
    "范围与非目标",
    "业务规则",
    "数据模型",
    "接口",
    "权限与数据归属",
    "验收条件",
    "风险与回滚",
    "OpenSpec 任务清单",
]


def normalize(text: str) -> str:
    """去掉空白、标点，便于宽松匹配。"""
    return "".join(ch for ch in text.lower() if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")


def find_missing(text: str) -> list[str]:
    norm = normalize(text)
    missing: list[str] = []
    for section in REQUIRED_SECTIONS:
        if normalize(section) not in norm:
            missing.append(section)
    return missing


def check_file(path: Path) -> bool:
    if not path.is_file():
        print(f"[SKIP] {path}  (not a file)")
        return True
    text = path.read_text(encoding="utf-8")
    missing = find_missing(text)
    if missing:
        print(f"[FAIL] {path}")
        for m in missing:
            print(f"        - missing: {m}")
        return False
    print(f"[ OK ] {path}")
    return True


def walk_root(root: Path) -> bool:
    md_files = sorted(root.rglob("*.md"))
    if not md_files:
        print(f"[WARN] no .md files under {root}")
        return True
    all_ok = True
    for f in md_files:
        if not check_file(f):
            all_ok = False
    return all_ok


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("file", nargs="?", help="单个 OpenSpec 文件路径")
    p.add_argument("--root", help="目录路径，递归扫描所有 .md")
    args = p.parse_args()

    if not args.file and not args.root:
        p.print_help()
        return 2

    if args.root:
        ok = walk_root(Path(args.root))
    else:
        ok = check_file(Path(args.file))

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
