# sfcct-tracker

Snowflake の [Credit Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf) PDF の変更を GitHub Actions で日次監視するリポジトリ。

PDF と変換済み Markdown をリポジトリに保存することで、変更履歴を GitHub 上で管理できる。

---

## ファイル構成

```
sfcct-tracker/
├── .github/
│   └── workflows/
│       └── check.yml                   # 日次スケジュール実行ワークフロー
├── scripts/
│   └── fetch_and_convert.py            # PDF取得 + Markdown変換スクリプト
├── data/
│   ├── CreditConsumptionTable.pdf      # 取得したPDF（Git管理）
│   └── CreditConsumptionTable.md       # 変換済みMarkdown（Git管理）
├── pyproject.toml                      # uv プロジェクト設定
├── uv.lock
├── CLAUDE.md                           # このファイル
└── .gitignore
```

---

## ローカル実行方法

```bash
# 依存パッケージのインストール
uv sync

# スクリプト実行（data/ に PDF と Markdown が生成される）
uv run scripts/fetch_and_convert.py
```

---

## GitHub Actions の動作

- **スケジュール**: 毎日 UTC 0:00（JST 9:00）に自動実行
- **手動実行**: Actions タブから `workflow_dispatch` で手動トリガー可能
- **処理フロー**:
  1. `uv run scripts/fetch_and_convert.py` を実行
  2. `git diff --quiet data/` で変更を確認
  3. 変更なし → 終了（コミットなし）
  4. 変更あり → `git commit & git push`

---

## 依存ライブラリの追加方法

```bash
uv add <package>
```
