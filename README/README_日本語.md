[Back to main language README](README.md)

# 🎉 自動化チーム管理プロジェクト

ようこそ！私たちの**自動化チーム管理プロジェクト**へ！🚀 このプロジェクトは、Habiticaプラットフォーム上でチームメンバーを簡単に管理し、チームの活性を保ち、管理の効率を向上させることを目指しています。それでは、このプロジェクトの構造と機能を見てみましょう！

## 📁 プロジェクト構造

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "自動化チーム管理ワークフロー"
    }
  },
  "LICENSE": "ライセンスファイル",
  "README.md": "プロジェクト説明文書",
  "README": {
    "README/README_Deutsch.md": "ドイツ語文書",
    "README/README_English.md": "英語文書",
    "README/README_Español.md": "スペイン語文書",
    "README/README_Français.md": "フランス語文書",
    "README/README_日本語.md": "日本語文書",
    "README/README_繁体中文.md": "繁体字中国語文書"
  },
  "documents": {
    "documents/brief_description.md": "プロジェクトの簡易説明",
    "documents/new_members.md": "新メンバー紹介",
    "documents/party_description.md": "チームの説明",
    "documents/remove_PM.md": "プロジェクトマネージャー削除の説明",
    "documents/remove_members.md": "メンバー削除の説明"
  },
  "logs": {
    "logs/manage_members.log": "メンバー管理ログ",
    "logs/update_description.log": "説明更新ログ"
  },
  "requirements.txt": "依存パッケージの要件",
  "scripts": {
    "scripts/manage_members.py": "メンバー管理スクリプト",
    "scripts/update_description.py": "説明更新スクリプト"
  }
}
```

## 📜 プロジェクト機能

### 1. 自動化チーム管理ワークフロー 🤖
私たちは `.github/workflows/automated_party_management.yml` に「チーム自動化管理」という名前のワークフローを定義しました。これにより、10分ごとに自動的に実行され、手動トリガーも可能です。このワークフローの主な目的は、Pythonスクリプトを使用してチームメンバー情報を管理・更新することです。以下の重要なステップが含まれています：

- **コードの取得**：リポジトリの最新コードを取得します。
- **Python環境の設定**：Python 3.8をインストールします。
- **依存項目のインストール**：スクリプトに必要な `requests` ライブラリをインストールします。
- **管理スクリプトの実行**：`manage_members.py` スクリプトを実行してメンバー管理を行います。
- **リクエスト頻度の制限**：スリープコマンドでAPIを過負荷にしないようにします。
- **更新スクリプトの実行**：`update_description.py` スクリプトを実行して説明を更新します。
- **変更履歴の記録**：すべての操作を記録し、ログをリポジトリにコミットします。

### 2. ライセンス 📝
プロジェクトには `LICENSE` ファイルが含まれており、Apache License, Version 2.0 を使用しています。これは、ソフトウェアの使用、複製、配布の条件を提供します。

### 3. 依存項目 📦
プロジェクトの `requirements.txt` ファイルには、このプロジェクトを実行するために必要な外部ライブラリが列挙されています。ここで必要なライブラリは `requests` で、これはネットワークリクエストやレスポンスを処理するための人気のHTTPライブラリです。

### 4. メンバー管理スクリプト 🧑‍🤝‍🧑
`manage_members.py` スクリプトは、Habiticaプラットフォーム上のチームメンバーを管理する役割を担っています。主な機能には以下が含まれます：
- ログの記録、リクエスト頻度の設定、非アクティブメンバーの検出、招待の送付など、チームの活性を維持するための機能です。

### 5. 説明更新スクリプト 🔄
`update_description.py` スクリプトは、一定の間隔でチームの説明を更新します。メンバー情報と外部APIからの内容を組み合わせて、あなたのチームの説明を常に新鮮で魅力的に保ちます。

## 🛠️ 実行方法
- Python環境が整っていることを確認し、`requirements.txt` に記載された依存ライブラリをインストールしてください。
- `manage_members.py` と `update_description.py` スクリプトを実行することで、メンバー管理と説明更新を手動で行えます。
- 自動化ワークフローに依存し、定期ジョブを設定して、チーム情報の管理を楽にしましょう。🎈

## 🌐 多言語サポート
このプロジェクトには、日本語を含む多言語の説明文書が付属しており、すべてのユーザーがプロジェクト内容を簡単に理解できるようになっています！🌍

## 📬 フィードバックとサポート
是非、質問や提案をお寄せください。一緒にこのプロジェクトをより良いものにしましょう！🙏

ご覧いただきありがとうございます！あなたのチームがHabiticaで活気あふれ、成功の道を常に歩み続けることを願っています！💪✨