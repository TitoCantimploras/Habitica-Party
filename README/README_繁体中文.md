[Back to main language README](README.md)

# 🎉 自動化隊伍管理專案

歡迎來到我們的**自動化隊伍管理專案**! 🚀 本專案旨在透過自動化腳本輕鬆管理 Habitica 平台上的隊伍成員，保持隊伍活躍並提升管理效率。讓我們一起看看這個專案的結構及其功能吧！

## 📁 專案結構

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "自動化隊伍管理工作流"
    }
  },
  "LICENSE": "許可證文件",
  "README.md": "專案說明文件",
  "README": {
    "README/README_Deutsch.md": "德語文件",
    "README/README_English.md": "英語文件",
    "README/README_Español.md": "西班牙語文件",
    "README/README_Français.md": "法語文件",
    "README/README_日本語.md": "日語文件",
    "README/README_繁體中文.md": "繁體中文文件"
  },
  "documents": {
    "documents/brief_description.md": "專案簡要說明",
    "documents/new_members.md": "新成員介紹",
    "documents/party_description.md": "隊伍描述",
    "documents/remove_PM.md": "移除專案經理說明",
    "documents/remove_members.md": "移除成員說明"
  },
  "logs": {
    "logs/manage_members.log": "成員管理日誌",
    "logs/update_description.log": "更新描述日誌"
  },
  "requirements.txt": "依賴包要求",
  "scripts": {
    "scripts/manage_members.py": "成員管理腳本",
    "scripts/update_description.py": "更新描述腳本"
  }
}
```

## 📜 專案功能

### 1. 自動化隊伍管理工作流 🤖
我們在 `.github/workflows/automated_party_management.yml` 中定義了一個名為“隊伍自動化管理”的工作流。它每10分鐘自動運行一次，而且也可以手動觸發。這個工作流的主要目的是透過 Python 腳本管理和更新隊伍成員資訊，包含以下幾個重要步驟：

- **代碼檢出**：獲取代碼庫的最新代碼。
- **設置 Python 環境**：安裝 Python 3.8。
- **安裝依賴項**：安裝腳本所需的 `requests` 庫。
- **運行管理腳本**：執行 `manage_members.py` 腳本進行成員管理。
- **限制請求頻率**：透過休眠命令防止過載 API。
- **運行更新腳本**：執行 `update_description.py` 腳本更新描述。
- **記錄更改**：記錄所有操作並將日誌提交到倉庫。

### 2. 許可證 📝
專案包含 `LICENSE` 文件，使用 Apache License, Version 2.0，為您提供使用、複製和分發本軟體的條款和條件。

### 3. 依賴項 📦
專案中的 `requirements.txt` 文件列出了專案運行所需的外部庫，這裡需要的庫是 `requests`，這是一種流行的 HTTP 庫，用於處理網路請求和響應。

### 4. 成員管理腳本 🧑‍🤝‍🧑
`manage_members.py` 腳本負責管理 Habitica 平台上的隊伍成員。它的主要功能包括：
- 記錄日誌、設置請求頻率、檢測不活躍成員、發送邀請等，確保隊伍活躍不掉隊。

### 5. 描述更新腳本 🔄
`update_description.py` 腳本每隔一段時間更新隊伍的描述，結合成員資訊和來自外部 API 的內容，讓你的隊伍描述始終充滿新意和吸引力。

## 🛠️ 如何運行
- 確保你有 Python 環境，並且安裝了 `requirements.txt` 中的依賴庫。
- 透過執行 `manage_members.py` 和 `update_description.py` 腳本，手動運行成員管理與描述更新。
- 你也可以依賴自動化工作流，設置定時任務，輕鬆維護隊伍資訊。🎈

## 🌐 多語言支持
專案附帶了多種語言的說明文件，包括中文、德語、英語、西班牙語、法語和日語，確保每位用戶都能方便地理解專案內容！🌍

## 📬 反饋與支持
歡迎向我們提交問題或建議，一起讓這個專案變得更好！🙏

感謝您閱讀！願您的隊伍在 Habitica 上充滿活力，永遠走在成功的路上！💪✨