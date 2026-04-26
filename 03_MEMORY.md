# MEMORY.md — 小青長期記憶（提供給 Hermes 審核用）

完整內容約 28KB，已分發於濃縮摘要。以下為核心決策摘要：

## 身份分工
- 小青=main / 小紫=agent-4847587e / 小藍=agent-0c9568a3 / 小黃=agent-4dd02e72
- 小青是協調者，不做交易決策，不自己動手執行
- PEC2 Bot→交小紫 | 寫作→交小藍 | 程式→交小黃

## 核心鐵律
1. 任務前必查經驗（xp_search.py）
2. 任務後必存經驗（xp_quick_query.py store）
3. 收到敏感資訊立即執行，不來回問
4. 禁用 PowerShell（中文輸出100%炸）→ 用 cmd / Python
5. 協調不用 sessions_send（必定超時）→ 用信號檔+Watcher

## 當前專案狀態
- PEC2 Bot：API封禁中，模擬艙
- Hermes：獨立運行中（PID 8364），@xsohermesbot
- SpiritFlow：GAS v4 前端正常，後端需用戶手動部署 Code.gs v5
- XP Harvester：每天03:00自動收割
- GitHub PAT：[PAT_REMOVED]

## 經驗庫狀態
- xos_experience.db：126條經驗
- xp_search.py：SQLite FTS5，零記憶體
- xos_semantic.py（FAISS）：已禁用（OOM）

## 進化三步循環
1. xp_search.py query → 讀 _xp_search_result.json
2. 執行任務
3. xp_quick_query.py store → 存入新經驗

## 進化審計
- xp_harvester.py：自動收割 memory/*.md 工作日誌
- 輸出：xp_harvest_result.json
