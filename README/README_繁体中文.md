- [{main_language}](README.md)- [Switch Language: English](README/README_English.md)
- [Cambiar idioma: Español](README/README_Español.md)
- [Changer de langue: Français](README/README_Français.md)
- [Sprache wechseln: Deutsch](README/README_Deutsch.md)
- [言語を切り替える: 日本語](README_日本語.md)

# 📚 專案簡介 README

歡迎來到我們的專案！🎉 在這裡，我們致力於透過自動化工具來管理 Habitica 社區的團隊成員，讓團隊管理更加高效和輕鬆。接下來，讓我們了解一下這個專案的結構和功能吧！✨

## 📁 專案結構

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

## 📝 文件簡介

### GitHub Actions 自動化工作流

在 `.github/workflows/automated_party_management.yml` 檔案中，定義了一個 GitHub Actions 工作流，用於自動管理團隊成員。它每 10 分鐘觸發一次，或可手動調用，運行在 Ubuntu 環境中，包含多個關鍵步驟：

1. **檢出代碼**：獲取專案代碼。
2. **搭建 Python 環境**：配置 Python 3.8。
3. **安裝依賴**：安裝需要的 `requests` 庫。
4. **執行管理腳本**：運行管理成員的 Python 腳本（`manage_members.py`），使用環境變數管理用戶憑證。
5. **速率限制**：引入暫停以管理請求速率。
6. **執行更新腳本**：運行更新說明的腳本（`update_description.py`），同樣使用環境變數。
7. **記錄更改**：將腳本生成的日誌更新提交到代碼庫。
8. **推送更改**：將更新的日誌推送回遠程代碼庫。

這個工作流旨在高效自動化團隊成員的管理和日誌的更新工作，真是個聰明的助手！🤖

### 授權文件

`LICENSE` 檔案是 Apache 授權 2.0，作為一種寬鬆的開源軟體授權，它為軟體及其他作品的使用、複製和分發奠定了條款和條件。它賦予用戶改革、修改和分發作品的權利，並確保對原作者的適當致謝。同時，檔案中還包含商標使用、保證免責的條款及責任限制。這份文件旨在促進開發者間的合作與用戶的使用，維護軟體自由，同時保護原作者的權利。

### 依賴文件

`requirements.txt` 檔案列出了專案運行所需的外部程式包和庫。在本專案中，它僅列出了 `requests` 庫，這是一個廣受歡迎的 Python 模組，它使得開發者能夠輕鬆發送 HTTP 請求，與網頁服務和 API 進行互動。使用簡潔的命令 `pip install -r requirements.txt`，你就可以輕鬆安裝這些依賴，立刻開始你的魔法之旅！✨

### 腳本文件

- **成員管理腳本 `manage_members.py`**

  這個腳本用於管理 Habitica 團隊中的成員，執行以下主要功能：

  1. **日誌記錄**：使用日誌模組記錄操作和錯誤，存儲在旋轉日誌檔案中，並在控制台輸出重要信息。
  2. **速率限制的 API 請求**：定義一個輔助函數以確保請求遵循規定的間隔。
  3. **用戶管理**：獲取團隊成員列表，檢查不活躍成員並將其移除。
  4. **消息發送**：可向用戶發送私信，並在團隊聊天中發布成員邀請和移除消息。
  5. **邀請新用戶**：對尋找團隊的新用戶發送邀請，並在聊天中通知團隊。

  透過這些功能，這個腳本極大地簡化了 Habitica 團隊成員的管理，讓社區管理變得更加輕鬆愉快！🎈

- **更新描述腳本 `update_description.py`**

  此腳本透過整合每日句子和成員活動信息，自動更新 Habitica 團隊描述。其主要功能包括：

  1. **速率限制的 API 請求**：管理請求的間隔，防止過載 Habitica API。
  2. **每日句子獲取**：從外部 API 獲取每日句子，獲取其英文內容和翻譯。
  3. **成員數據收集**：收集團隊成員的信息，包括最後登錄時間和上次活躍時長。
  4. **描述格式化**：讀取 Markdown 模板並格式化為當前內容、成員信息和時間戳。
  5. **更新闡釋**：將更新的描述發送回 Habitica API。

  透過這樣的自動化手段，該腳本不斷提升團隊描述的吸引力和成員互動，簡直是個文藝範兒的朋友！🎨

---

感謝您查看我們的專案！希望我們提供的工具能為您的 Habitica 社區管理帶來便利與樂趣。如有任何問題，請隨時聯繫！🎈👋