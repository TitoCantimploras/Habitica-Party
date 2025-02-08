- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)

# プロジェクト紹介 📚

ようこそ、**Habitica チーム自動化管理プロジェクト**へ！🎉 このプロジェクトは、自動化ツールとスクリプトを通じてチームメンバーの管理を最適化し、Habiticaプラットフォームでの体験を向上させることを目的としています。ゲームの一部として参加している方も、単にチームを管理したい方も、私たちのツールがあなたの助けになります！

## プロジェクト構造 📂

以下はプロジェクトの構造です。必要なファイルを簡単に見つけることができます：

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml
├── LICENSE
├── README.md
├── README
│   ├── README_Deutsch.md
│   ├── README_English.md
│   ├── README_Español.md
│   ├── README_Français.md
│   ├── README_日本語.md
│   └── README_繁体中文.md
├── documents
│   ├── brief_description.md
│   ├── new_members.md
│   ├── party_description.md
│   ├── remove_PM.md
│   └── remove_members.md
├── logs
│   ├── manage_members.log
│   └── update_description.log
├── requirements.txt
└── scripts
    ├── manage_members.py
    └── update_description.py
```

## ファイル紹介 🔍

### チーム自動管理 (`.github/workflows/automated_party_management.yml`)
このファイルは、「チーム自動化管理」という名前のGitHub Actionsワークフローを定義しています。10分ごとに自動で実行されるか、手動でトリガー可能です。以下の機能を実現します：
- コードリポジトリのチェックアウト
- Python 3.8環境の設定
- 必要な依存ライブラリ（例：`requests`）のインストール
- 管理スクリプト（`manage_members.py` と `update_description.py`）を実行し、Habitica APIと対話
- スクリプト実行間に遅延を設定し、APIのレート制限を超えないようにする
- 管理スクリプトの更新を記録するために、ログの変更をコミットしてプッシュ

### ライセンス (`LICENSE`)
本プロジェクトはApacheライセンス2.0に従っており、オープンソースの協力を促進し、クリエイターとユーザーの権利を保護することを目指しています。ライセンスには、ソフトウェアやその他の作品の使用、コピー、配布に関する条件が詳細に記載されています。

### 依存ファイル (`requirements.txt`)
このファイルには、プロジェクトで必要な外部ライブラリと依存関係がリストされています。ここでは「requests」ライブラリのみが含まれており、HTTPリクエストの送信とレスポンスの処理を簡単に行う方法を提供します。

### メンバー管理スクリプト (`scripts/manage_members.py`)
このスクリプトはHabiticaプラットフォーム上のメンバーを管理するために使用され、以下のタスクを自動化します：
- 非アクティブなメンバーを削除し、通知を送信
- チームに参加希望の新しいユーザーを招待

### 説明更新スクリプト (`scripts/update_description.py`)
このスクリプトはHabiticaチームの説明を更新し、コンテンツを動的に取得して更新します。主な機能は以下の通りです：
- 外部APIからのインスピレーションの文を毎日取得
- チームの説明を自動的に更新し、情報の新鮮さを保つ！

## ログファイル 📜
すべての実行操作のログが`logs`フォルダーに記録され、実行履歴を確認したり潜在的な問題を調査したりするのに便利です。

## 使用開始 🚀

1. プロジェクトリポジトリをクローンします
2. 依存関係をインストールします：`pip install -r requirements.txt`
3. GitHub Actions 自動化ワークフローを使用して、シームレスなメンバー管理体験を楽しんでください！

## 貢献について 💡
このプロジェクトに貢献したい場合は、PRを提出するか、質問を尋ねてください！一緒にHabiticaをより素晴らしいものにしましょう！⭐️

このプロジェクトのREADMEファイルをお読みいただきありがとうございます！あなたの参加とサポートを期待しています。ぜひ ⭐️ このプロジェクトをお願いします！