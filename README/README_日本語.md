[Back to main language README](README.md)

切换语言: 简体中文
切換語言: 繁體中文
Switch Language: English
Cambiar idioma: Español
Changer de langue: Français
Sprache wechseln: Deutsch

# プロジェクト自管理システム README 🌟

私たちのプロジェクト自管理システムへようこそ！🎉 このプロジェクトは Habitica プラットフォームのチーム管理のために設計されており、チームメンバーの自動管理とチーム説明の更新を通じて、すべてのチームが良好な状態で運営されることを保証します。👏

## プロジェクト構造 🗂️

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

## プロジェクトファイルの紹介 📁

### ワークフローファイル 🔄
- **自動管理ワークフロー**: このファイルは `.github/workflows/automated_party_management.yml` に位置し、GitHub Actions を通じて定期的にチームを管理します。10 分ごとに実行し、チームの状態が常に更新されるようにします！💼

### ライセンス 📜
- **LICENSE**: 本プロジェクトは Apache ライセンス 2.0 に基づいており、ソフトウェアおよびその他の作品の使用、複製、配布の条項を明確に規定しています！✨

### 依存ファイル 📦
- **requirements.txt**: このファイルにはプロジェクトに必要な依存ライブラリがリストされており、重要なライブラリとして `requests` のみが含まれています。HTTP リクエストを簡単に送信でき、コードの記述が簡素化されます！🚀

### スクリプトファイル 🖥️
- **メンバー管理スクリプト (manage_members.py)**: このスクリプトはメンバーの活発状態を監視し、不活発なメンバーを自動で削除し、新しいメンバーを招待するなどの操作を担当しています。チームの仲間たちが常に活力にあふれるようにします！💪

- **説明更新スクリプト (update_description.py)**: このスクリプトの役割は、チームの説明を更新することです。毎日のモチベーションの言葉、メンバー情報、現在の時間などを含み、私たちのチームが常にポジティブなエネルギーに満ちているようにします！🌈

## 貢献ガイドライン 🤝

このプロジェクトに興味がある誰でも、ぜひあなたの力をお貸しください！私たちのライセンスに従い、他の貢献者と友好的に交流してください。🌍

## 使用方法 🛠️

1. **プロジェクトをクローン**: 以下のコマンドを使用してプロジェクトをローカルにクローンします：
   ```bash
   git clone https://github.com/your-repo-url.git
   ```

2. **依存ライブラリをインストール**: pip を使用して必要な Python ライブラリをインストールします：
   ```bash
   pip install -r requirements.txt
   ```

3. **GitHub Secretsを設定**: 管理スクリプトに必要なユーザー ID と API キーを設定し、Habitica API インターフェースにアクセスできる権限を持っていることを確認します。

4. **ワークフローを起動**: 手動でワークフローをトリガーするか、10 分ごとの自動実行を待ち、自動管理の楽しさを体験してください！🥳

## ロギング 📊

`logs` フォルダー内には、チーム管理および説明更新プロセスで生成されたログファイルがあり、すべての操作を追跡するのに役立ちます！🪄

## お問い合わせ 📧

プロジェクトの使用中に問題が発生したり、提案がある場合は、遠慮なく電子メールでお問い合わせください！😊

プロジェクトへの関心とご利用に感謝します！さあ、一緒により活発で効率的なチームを作りましょう！🎊

---

この紹介がプロジェクトへの関心を高めてくれることを願っています。さあ、自動管理の楽しさを体験しましょう！🚀✨