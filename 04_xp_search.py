# xp_search.py — 輕量經驗檢索（提供給 Hermes 審核用）

完整代碼見上方。以下為核心摘要：

## 用途
取代 FAISS 向量搜索，採用 SQLite FTS5，零記憶體佔用。

## CLI 用法
```bash
python xp_search.py rebuild          # 重建 FTS 索引
python xp_search.py query "BTC分析"  # 搜索經驗
python xp_search.py query "PowerShell" --top 5
python xp_search.py stats            # 統計資訊
```

## 核心邏輯
1. **方法1**：FTS5 全文搜索（`xp_fts MATCH`）
2. **方法2**：如無結果，用 LIKE 關鍵詞 fallback
3. 結果寫入 `_xp_search_result.json`（避免 stdout 中文問題）

## 輸出格式
```json
{
  "query": "...",
  "count": 3,
  "results": [
    {"id": 1, "task_prompt": "...", "lessons": "...", "task_type": "..."}
  ]
}
```

## 關鍵教訓
- 結果寫 JSON 檔，不用 stdout（中文stdout在cmd下會炸）
- FTS5 需要先 rebuild 才能建立索引
- 遇到 OOM → 禁用 FAISS，改用本工具
