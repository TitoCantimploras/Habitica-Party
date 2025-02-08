- [{main_language}](README.md)- [切換語言: 繁體中文](README/README_繁体中文.md)
- [Switch Language: English](README/README_English.md)
- [Cambiar idioma: Español](README/README_Español.md)
- [Changer de langue: Français](README/README_Français.md)
- [Sprache wechseln: Deutsch](README/README_Deutsch.md)

# 📚 プロジェクト概要 README

私たちのプロジェクトへようこそ！🎉 ここでは、自動化ツールを通じて Habitica コミュニティのチームメンバーを管理し、チーム管理をより効率的で楽にすることに取り組んでいます。それでは、このプロジェクトの構造と機能について見ていきましょう！✨

## 📁 プロジェクト構造

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "automated_party_management.yml"
    }
  },
  "LICENSE": "LICENSE",
  "README.md": "README.md",
  "README": {
    "README/README_Deutsch.md": "README_Deutsch.md",
    "README/README_English.md": "README_English.md",
    "README/README_Español.md": "README_Español.md",
    "README/README_Français.md": "README_Français.md",
    "README/README_日本語.md": "README_日本語.md",
    "README/README_繁体中文.md": "README_繁体中文.md"
  },
  "documents": {
    "documents/brief_description.md": "brief_description.md",
    "documents/new_members.md": "new_members.md",
    "documents/party_description.md": "party_description.md",
    "documents/remove_PM.md": "remove_PM.md",
    "documents/remove_members.md": "remove_members.md"
  },
  "logs": {
    "logs/manage_members.log": "manage_members.log",
    "logs/update_description.log": "update_description.log"
  },
  "requirements.txt": "requirements.txt",
  "scripts": {
    "scripts/manage_members.py": "manage_members.py",
    "scripts/update_description.py": "update_description.py"
  }
}
```

## 📝 ファイルの概要

### GitHub Actions 自動化ワークフロー

`.github/workflows/automated_party_management.yml` ファイルでは、チームメンバーの自動管理用の GitHub Actions ワークフローが定義されています。10 分ごとにトリガーされるか、手動で呼び出すことができ、Ubuntu 環境で実行され、以下の主要なステップが含まれています：

1. **コードのチェックアウト**：プロジェクトコードを取得します。
2. **Python 環境の構築**：Python 3.8 を設定します。
3. **依存関係のインストール**：必要な `requests` ライブラリをインストールします。
4. **管理スクリプトの実行**：メンバー管理の Python スクリプト（`manage_members.py`）を実行し、環境変数でユーザー資格情報を管理します。
5. **レート制限**：リクエストのペースを管理するために一時停止を導入します。
6. **更新スクリプトの実行**：更新の説明用のスクリプト（`update_description.py`）を同様に実行します。
7. **変更の記録**：スクリプトにより生成されたログをコードリポジトリに更新します。
8. **変更のプッシュ**：更新されたログをリモートコードリポジトリにプッシュします。

このワークフローは、チームメンバーの管理とログの更新作業を効率的に自動化することを目的としており、本当に賢い助手です！🤖

### 免許ファイル

`LICENSE` ファイルは Apache ライセンス 2.0 であり、これは緩やかなオープンソースソフトウェアライセンスとして、ソフトウェア及びその他の作品の使用、コピー及び配布の条件を定めています。ユーザーに作品を改築、変更及び配布する権利を与え、原作者への適切な謝辞を保証します。また、商標の使用、責任の免除条項なども含まれています。この文書は開発者間の協力とユーザーの使用を促進し、ソフトウェアの自由を維持しつつ原作者の権利を保護することを目指しています。

### 依存関係ファイル

`requirements.txt` ファイルは、プロジェクトの実行に必要な外部パッケージとライブラリを示しています。このプロジェクトでは、人気のある Python モジュールである `requests` ライブラリのみが記載されています。これを使えば、開発者は簡単に HTTP リクエストを送信し、ウェブサービスや API と対話できます。シンプルなコマンド `pip install -r requirements.txt` を使用することで、これらの依存関係を簡単にインストールし、あなたの魔法の旅をすぐに始めることができます！✨

### スクリプトファイル

- **メンバー管理スクリプト `manage_members.py`**

  このスクリプトは、Habitica チームのメンバーを管理するために使用され、以下の主要機能を実行します：

  1. **ログ記録**：ログモジュールを使用して操作とエラーを記録し、回転ログファイルに保存し、コンソールに重要情報を出力します。
  2. **レート制限の API リクエスト**：リクエストが規定された間隔に従うことを確保するための補助関数を定義します。
  3. **ユーザー管理**：チームメンバーのリストを取得し、非アクティブメンバーをチェックして削除します。
  4. **メッセージ送信**：ユーザーにプライベートメッセージを送信し、チームチャットにメンバーの招待や削除メッセージを投稿します。
  5. **新しいユーザーへの招待**：チームを探している新しいユーザーに招待を送信し、チャットでチームに通知します。

  これらの機能を通じて、このスクリプトは Habitica チームメンバーの管理を大幅に簡素化し、コミュニティ管理をより楽しいものにします！🎈

- **更新説明スクリプト `update_description.py`**

  このスクリプトは、毎日の文とメンバー活動情報を統合して Habitica チームの説明を自動更新します。主な機能は以下の通りです：

  1. **レート制限の API リクエスト**：リクエストの間隔を管理し、Habitica API の過負荷を防ぎます。
  2. **毎日の文の取得**：外部 API から毎日の文を取得し、その英語の内容と翻訳を入手します。
  3. **メンバーデータの収集**：チームメンバーの情報を収集し、最終ログイン時間や最後の活動時間を確認します。
  4. **説明のフォーマット化**：Markdown テンプレートを読み込み、現在の内容、メンバー情報、タイムスタンプとしてフォーマットします。
  5. **更新の送信**：更新された説明を Habitica API に送信します。

  このような自動化手段を通じて、チームの説明の魅力とメンバー間のインタラクションを向上させ、まるで文芸風の友人のようです！🎨

---

私たちのプロジェクトを見ていただき、ありがとうございます！提供するツールがあなたの Habitica コミュニティ管理に便利さと楽しさをもたらすことを願っています。ご質問があれば、いつでもお気軽にお問い合わせください！🎈👋