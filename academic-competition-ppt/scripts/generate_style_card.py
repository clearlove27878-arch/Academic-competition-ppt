#!/usr/bin/env python3
"""Generate a draft PPT style card from extracted PPTX style signals."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TEMPLATE = """# {style_id}: {name}

## 1. 风格名称

{name}。标签：{tags}。

## 2. 适用场景

{scenarios}

## 3. 不适用场景

不适合牺牲公式、表格、实证证据可读性的场景；不适合与用户明确指定风格冲突的任务。

## 4. 色彩系统

- 主背景色：根据模板提取，常见颜色包括 {colors}。
- 主强调色：从主色中选择 1-2 个高识别度颜色。
- 辅助色：浅灰、白色或模板中的低饱和辅助色。
- 正文字色：优先黑色/深灰，深色背景时使用白色/浅灰。
- 图表建议配色：使用主强调色 + 辅助灰，控制在 3-5 色。
- 禁用色彩：与模板主色冲突、降低证据可读性的高饱和颜色。

## 5. 字体与文字层级

- 封面标题：参考模板标题字体；不可用时使用思源宋体/SimSun/SimHei/微软雅黑替代。
- 一级标题：粗体，保持与模板主色一致。
- 二级标题：略小于一级标题，使用主色或深灰。
- 正文：微软雅黑/黑体，保证 14 pt 以上。
- 注释：灰色小字，保持可读。
- 页码/导航：沿用模板导航强弱，但不得抢正文标题。

## 6. 版式结构

- 封面：参考模板封面色彩、标题位置和背景语言。
- 目录页：保留学术研究链条或章节导航。
- 章节页：提取模板章节节奏，但保持内容逻辑。
- 内容页：用模板卡片、线条、标题层级承载论文内容。
- 图表页：证据图表优先，模板仅负责框架。
- 机制分析页：使用可编辑形状和连接线。
- 实证结果页：回归表/图表保持最大可读性。
- 政策建议页：稳健建议，避免口号化。
- 结论页：参考模板收束页。

## 7. 装饰元素

常见形状：{geometries}。装饰应作为视觉框架，不替代研究证据。

## 8. 信息密度

默认保持长页数论文汇报密度。若模板空间不足，应拆页而不是缩小文字；短摘要/路演版只在用户明确要求时使用。

## 9. 导航栏规则

保留模板导航位置和当前章节高亮方式；若模板没有导航，则使用默认学术竞赛导航。导航不能使用过强装饰压缩正文。

## 10. 图表风格

表格、图表、机制图应优先清晰；颜色与模板主色协调。原始论文图表不得拉伸或重绘成未经说明的装饰图。

## 11. 禁忌

不得机械复制模板页面内容；不得把模板设为默认风格；不得因为模板视觉强烈而降低学术表达完整度。

## 12. 调用提示词

- "使用 {name} 风格"
- "参考刚导入的 {name} 模板"
- "从模板库选择 {style_id}"
"""


def load_summary(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a draft style card from extract_ppt_style.py JSON.")
    parser.add_argument("--input", "-i", required=True, type=Path, help="JSON produced by extract_ppt_style.py.")
    parser.add_argument("--output", "-o", required=True, type=Path, help="Markdown draft path.")
    parser.add_argument("--style-id", required=True, help="Style id, e.g. style_08_custom.")
    parser.add_argument("--name", required=True, help="Human style name.")
    parser.add_argument("--tags", default="自定义模板, 可选风格, 学术竞赛")
    parser.add_argument("--scenarios", default="适合用户明确指定该模板或需要相近视觉语言的学术竞赛、课程汇报、论文展示。")
    parser.add_argument("--overwrite", action="store_true", help="Allow overwriting an existing output file.")
    args = parser.parse_args()

    if args.output.exists() and not args.overwrite:
        raise SystemExit(f"Refusing to overwrite existing file: {args.output}. Use --overwrite to replace it.")

    data = load_summary(args.input)
    colors = ", ".join(item["hex"] for item in data.get("top_colors", [])[:8]) or "未提取到明确主题色"
    geometries = ", ".join(item["geometry"] for item in data.get("shape_geometries", [])[:8]) or "未提取到常见形状"
    content = TEMPLATE.format(
        style_id=args.style_id,
        name=args.name,
        tags=args.tags,
        scenarios=args.scenarios,
        colors=colors,
        geometries=geometries,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(content, encoding="utf-8")
    print(str(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
