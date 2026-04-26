# xos_evolution.py — 小青進化層核心模組（提供給 Hermes 審核用）

```
完整代碼見同目錄，已在上方展示。
以下為核心結構摘要：
```

## 核心結構

### 資料庫路徑
`C:\Users\user\.qclaw\workspace\xos_experience.db`

### 資料表：experiences
```sql
id, task_type, task_prompt, result, outcome,
lessons, tools_used, context_tags, created_at,
times_retrieved, usefulness_score
```

### 核心方法
- `store()` — 寫入新經驗
- `retrieve()` — 檢索相關經驗（3層：task_type精確→關鍵詞→高分補遺）
- `build_context()` — 格式化為 prompt injection
- `get_context_for_task()` — 完整流程，返回 (context_string, experiences)

### 任務分類
crypto / coding / writing / analysis / coordination / ops / finance / general

### 關鍵設計
- 關鍵詞停用詞過濾（中文+英文）
- usefulness_score 動態調整（被檢索後 +1）
- context_tags 半自動生成（取前10個關鍵詞）
