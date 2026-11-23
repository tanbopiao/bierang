"""别壤（BIERANG）· 实验隔离基线分支

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：实验隔离基线分支。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Bierang:
    """别壤（BIERANG）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "BIERANG"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.branches = {}
        self._seq = 0

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
        """同根异壤：开实验分支，返回壤号。"""
        self._seq += 1
        soil_id = "BR-%04d" % self._seq
        self.branches[soil_id] = {"soil_id": soil_id, "name": name, "base": "gui", "changes": []}
        self.events.append({"event": "branch", "soil_id": soil_id, "name": name})
        return soil_id

    def diff(self, ref):
        """壤分判读：实验壤与圭本真值分化。"""
        if ref not in self.branches:
            raise KeyError("无此壤号： %s" % ref)
        branch = self.branches[ref]
        return {
            "soil_id": ref,
            "base": branch["base"],
            "diverged": bool(branch["changes"]),
            "changes": list(branch["changes"]),
        }
