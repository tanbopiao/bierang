"""别壤（BIERANG）· 实验隔离基线分支

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：实验隔离基线分支。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Bierang:
    """别壤（BIERANG）算子骨架 v0。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "BIERANG"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "bierang",
            "cn": "别壤",
            "code": self.CODE,
            "duty": "实验隔离基线分支",
            "mingwen": "同根异壤，界立不淆",
            "anchor": self.ANCHOR,
        }

    def branch(self, name):
        """同根异壤：开实验分支，返回壤号（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("BIERANG.branch 骨架桩，候进化轮补齐")

    def diff(self, ref):
        """壤分判读：实验壤与圭本真值分化（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("BIERANG.diff 骨架桩，候进化轮补齐")
