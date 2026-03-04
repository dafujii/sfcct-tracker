# sfcct-tracker

Snowflake の [Credit Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf) PDF の変更を GitHub Actions で日次監視するリポジトリ。

PDF と変換済み Markdown をリポジトリに保存することで、変更履歴を GitHub 上で管理できる。

## 仕組み

毎日 UTC 0:00（JST 9:00）に GitHub Actions が起動し、PDF を取得・Markdown に変換する。前回から変更があった場合のみコミット・プッシュする。

```
GitHub Actions（毎日 UTC 0:00）
  ↓
PDF をダウンロード → data/CreditConsumptionTable.pdf
  ↓
Markdown に変換 → data/CreditConsumptionTable.md
  ↓
変更あり → git commit & push
変更なし → 終了
```

## ファイル構成

```
sfcct-tracker/
├── .github/workflows/check.yml        # 日次スケジュール実行ワークフロー
├── scripts/fetch_and_convert.py       # PDF取得 + Markdown変換スクリプト
├── data/
│   ├── CreditConsumptionTable.pdf     # 取得したPDF（Git管理）
│   └── CreditConsumptionTable.md      # 変換済みMarkdown（Git管理）
├── pyproject.toml                     # uv プロジェクト設定
└── uv.lock
```

## ローカル実行

```bash
uv sync
uv run scripts/fetch_and_convert.py
```

## 手動実行

GitHub の Actions タブから `Check CCT Update` ワークフローを選択し、**Run workflow** で手動実行できる。
