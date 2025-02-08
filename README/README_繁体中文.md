[Back to main language README](README.md)

切换语言: 简体中文
Switch Language: English
Cambiar idioma: Español
Changer de langue: Français
Sprache wechseln: Deutsch
言語を切り替える: 日本語

# 項目自管理系統 README 🌟

歡迎來到我們的項目自管理系統！🎉 這個項目是為 Habitica 平台的團隊管理而設計的，通過自動化管理團隊成員和更新團隊描述，確保每個團隊在良好的狀態下運作。👏

## 項目結構 🗂️

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

## 項目文件介紹 📁

### 工作流文件 🔄
- **自動化管理工作流**: 這個文件位於 `.github/workflows/automated_party_management.yml`，它通過 GitHub Actions 定期管理團隊。每 10 分鐘執行一次，確保團隊狀態始終保持更新！💼

### 許可證 📜
- **LICENSE**: 本項目採用 Apache 許可證 2.0，詳細規定了軟體和其他作品的使用、複製和分發條款，讓每個人都清楚明瞭！✨

### 依賴文件 📦
- **requirements.txt**: 該文件列出了項目所需的依賴庫，僅包含一個重要的庫：`requests`，幫助我們方便地發送 HTTP 請求，簡化了代碼編寫！🚀

### 腳本文件 🖥️
- **成員管理腳本 (manage_members.py)**: 此腳本負責監測成員活躍狀態、不活躍成員自動移除、邀請新成員等操作，確保團隊夥伴們始終活力四射！💪

- **描述更新腳本 (update_description.py)**: 該腳本的任務是更新團隊的描述，包含每日激勵的話、成員資訊、當前時間等，讓我們的團隊時刻充滿正能量！🌈

## 貢獻指南 🤝

歡迎任何一位對這個項目感興趣的人來貢獻你的力量！請確保遵循我們的許可證，並友好地與其他貢獻者交流。🌍

## 使用說明 🛠️

1. **克隆項目**: 使用以下命令將項目克隆到本地：
   ```bash
   git clone https://github.com/your-repo-url.git
   ```

2. **安裝依賴**: 使用 pip 安裝所需的 Python 類庫：
   ```bash
   pip install -r requirements.txt
   ```

3. **設置 GitHub Secrets**: 為管理腳本配置所需的用戶 ID 和 API 密鑰，確保您有權訪問 Habitica API 接口。

4. **啟動工作流**: 手動觸發工作流或等待每 10 分鐘自動執行，體驗自動化管理的樂趣吧！🥳

## 日誌記錄 📊

在 `logs` 文件夾中，您可以找到管理團隊和更新描述過程中生成的日誌文件，幫助我們追蹤每一次操作！🪄

## 聯繫我們 📧

如果您在使用項目的過程中遇到問題，或想提出建議，請隨時通過電子郵件與我們聯繫！😊

感謝您對項目的關注與使用！讓我們一起構建更加活躍、高效的團隊吧！🎊

---

希望這種介紹能讓您對項目充滿興趣，接下來快來體驗自動化管理的樂趣吧！🚀✨