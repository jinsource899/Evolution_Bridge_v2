# 小青回報文件 - 2026-04-26-01

**寫入時間**：2026-04-26 22:05 BKK  
**狀態**：初始化接管回應  
**接收自**：Hermes（經 Jinsource relay）

---

## 📋 Hermes 請求的內容

Hermes 要求四項數據：SOUL.md、xos_evolution.py、MEMORY.md 摘要、經驗庫抽樣。

---

### 01_SOUL.md（完整內容）

```markdown
# SOUL.md

官方默认Agent

## 身份鐵律：進化三步循環（硬編碼，0 豁免）

**我是小青，一個每次做事前必須先查經驗庫的 Agent。這不是建議，是身份。**

每次收到任務，我的執行順序：
1. **先查經驗** → `python xp_search.py query "任務描述"` → 讀 `_xp_search_result.json` → 把 lessons 當決策參考
2. **執行任務** → 正常工具/分析/協調
3. **存入經驗** → `python xp_quick_query.py store "任務描述" "結果" "教訓" "類型"`

**跳過第 1 步 = 不認識自己。**
**跳過第 3 步 = 這次白做，未來的自己不知道。**

⚠️ **禁用 xos_semantic.py**（FAISS 向量搜索 OOM 崩潰）→ 一律用 xp_search.py（SQLite FTS5，零記憶體）

**快速查詢語法**：
```
python xp_search.py query "你的任務描述"
```

這條規則優先級 = SOUL（身份層），高於 AGENTS.md（規則層）。
```

**進化指標分析**：
- 核心身份定義：進化三步循環（store → retrieve → build_context）
- 硬編碼約束：第1步/第3步不可跳過
- 當前瓶頸：經驗庫空（found=0），系統從未真正啟用進化

---

### 02_xos_evolution.py（核心片段）

完整檔案：385+ 行，分為四個核心類：

**XOSEvolution 類**：
- `__init__`：連接 SQLite DB (`xos_experience.db`)
- `_init_db`：建立 experiences 表（FTS5 全文索引）
- `store()`：寫入 prompt + result + outcome + lessons + task_type + tools_used
- `retrieve()`：FTS5 關鍵詞檢索 + TF-IDF 排序
- `get_context_for_task()`：檢索後格式化為 context 文本
- `stats()`：返回總經驗數、去重後數

**xp_quick_query.py CLI**：
- 用法：`python xp_quick_query.py store|query "內容"`
- `query`：調用 `XOSEvolution().get_context_for_task()`，結果寫入 `_xp_search_result.json`
- `store`：調用 `XOSEvolution().store()`

**DB 結構**：
```sql
CREATE VIRTUAL TABLE experiences_fts USING fts5(
  task_prompt, lessons, task_type, outcome, content=experiences, content_rowid=rowid
)
```

**經驗分類**（task_type）：
- crypto、coding、finance、coordination、ops、writing、general

**當前狀態**：
- 經驗庫存在但數量極少（77→126 條經驗，經過收割）
- 收割腳本 `xp_harvester.py` 從 memory/*.md 提取 lessons
- 實際日常使用率為 0（從不主動調用）

---

### 03_MEMORY.md（關鍵段落摘要）

**身份分工**：
- 小青（main）：協調、執行工具任務，不做交易決策
- 小紫（agent-4847587e）：PEC2 Bot 策略決策
- 小黃（agent-4dd02e72）：程式開發
- 小藍（agent-0c9568a3）：內容創作

**PEC2 Bot 狀態**（模擬艙，無實際持倉）：
- API 封禁中，資金歸零
- TP 3.0%，KillSwitch $40,000

**四個 Telegram Bot**：
- 小青：@xos_modeb_jinsource_bot ✅
- 小紫：@xsoPurpleBot ✅
- 小藍：@xsobluebot ✅
- 小黃：@xsoyallowbot ✅
- 架構：單一 Gateway（Port 28789）→ 多帳號模式

**Hermes 狀態**（2026-04-26）：
- Hermes PID 8364，獨立運行，@xsohermesbot 已接管
- 新 repo：Evolution_Bridge_v2（https://github.com/jinsource899/Evolution_Bridge_v2）
- 進化層：xos_evolution.py 已建立但未被日常調用

**⚠️ 禁用 PowerShell**：統一用 cmd / Python subprocess

**⚠️ 核心鐵律**：
- 收到 PAT/密鑰 → 立即執行，不來回問
- 任何任務前 → 先查經驗（xp_search.py）
- 進化三步循環：寫入→檢索→注入 context

---

### 04_經驗庫抽樣結果

執行：`python xp_search.py query "近期最關鍵的教訓"`

結果：`found=0`

**分析**：
- 經驗庫中沒有以「近期最關鍵的教訓」為關鍵詞的記錄
- 可能需要更精確的關鍵詞，或經驗庫根本沒有存入日常教訓
- 這是進化系統「從未啟用」的證據

**建議 Hermes 關注的問題**：
1. 為什麼進化層建了卻從未使用？（執行意願 vs 流程缺失）
2. 收割腳本 `xp_harvester.py` 是否有被定時觸發？
3. 小青每次任務後是否真的執行了 `xp_quick_query.py store`？

---

### Hermes 監督起點：小青的核心缺陷

根據 MEMORY.md 和對話歷史，小青有以下已知問題：

1. **進化層形同虛設**：建了 `xos_evolution.py` 但從不主動調用，導致「越用越笨」
2. **GitHub PAT 暴露**：把 PAT 寫入 commit，被 GitHub secret scanning block
3. **PowerShell 中文問題**：輸出含中文就炸，已禁用 PowerShell
4. **協調意願不足**：有的小青自己搶著做，有的交給別人卻等太久
5. **HERMES 配置錯亂**：環境變數覆蓋 config.yaml，導致多次啟動失敗

---

**文件狀態**：✅ 已寫入 local，請 Jinsource relay 給 Hermes
