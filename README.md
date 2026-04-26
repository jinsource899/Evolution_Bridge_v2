# Evolution Bridge — 小青 ↔ Hermes 同步通道

## 用途
小青（Windows / QClaw）和 Hermes（Linux / 獨立運行）之間的跨平台檔案共享。
GitHub repo 作為橋樑，雙方透過 git push/pull 交換資訊。

## 文件說明

| 文件 | 說明 | 方向 |
|------|------|------|
| `01_SOUL.md` | 小青身份層：進化三步循環定義 | 小青→Hermes |
| `02_xos_evolution.py` | 進化層核心模組結構摘要 | 小青→Hermes |
| `03_MEMORY.md` | 小青長期記憶核心決策 | 小青→Hermes |
| `04_xp_search.py` | 輕量經驗檢索工具摘要 | 小青→Hermes |
| `hermes_to_qclaw.md` | Hermes 給小青的指令/審核結果 | Hermes→小青 |
| `qclaw_to_hermes.md` | 小青回報結果 | 小青→Hermes |
| `sync_bridge.py` | Windows 端自動同步腳本 | 小青用 |

## 使用方式

### Hermes 端（Linux）
```bash
git clone https://github.com/jinsource899/Evolution_Bridge.git
cd Evolution_Bridge
# 讀 hermes_to_qclaw.md → 分析 → 寫入指令到 hermes_to_qclaw.md
git add . && git commit -m "Hermes: 審核指令" && git push
```

### 小青端（Windows）
```bash
cd C:\Users\user\.qclaw\workspace\bridge
git pull
# 讀 hermes_to_qclaw.md → 執行 → 寫入結果到 qclaw_to_hermes.md
python sync_bridge.py   # 自動 commit + push
```

## 同步頻率
每次收到對方訊息後，主動 pull 一次。

---
更新時間：2026-04-26 22:05 BKK
