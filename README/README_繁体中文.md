- [简体中文](/README.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# 項目簡介 📚

歡迎來到 **Habitica 隊伍自動化管理項目**！🎉 這個項目致力於透過自動化工具和腳本來優化團隊成員管理，從而提升您在 Habitica 平台上的體驗。無論您是遊戲的一部分，還是僅僅想要輕鬆管理您的團隊，我們的工具都能助您一臂之力！

## 項目結構 📂

下面是項目的結構，確保您能輕鬆找到所需的文件：

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
│   └── README_繁體中文.md
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

## 文件簡介 🔍

### 自動化隊伍管理 (`.github/workflows/automated_party_management.yml`)
這個文件定義了一個名為 “隊伍自動化管理” 的 GitHub Actions 工作流。它會每 10 分鐘自動運行，或可手動觸發，實現以下功能：
- 檢出代碼倉庫
- 設置 Python 3.8 環境
- 安裝所需的依賴庫（如 `requests`）
- 執行管理腳本（`manage_members.py` 和 `update_description.py`），與 Habitica API 進行交互
- 在腳本執行之間設置延遲，防止超過 API 速率限制
- 提交並推送日誌更改，以記錄管理腳本的更新

### 许可证 (`LICENSE`)
本項目遵循 Apache 许可证 2.0，旨在促進開源合作，並保護創作者和用戶的權利。許可證詳細說明了使用、複製和分發軟體及其他作品的條款和條件。

### 依賴文件 (`requirements.txt`)
該文件列出了項目所需的外部庫和依賴項，這裡只包含 “requests” 庫，提供了一種簡便的方式來發送 HTTP 請求和處理響應。

### 成員管理腳本 (`scripts/manage_members.py`)
此腳本用於管理 Habitica 平台上的成員，自動化以下任務：
- 移除不活躍成員並向其發送通知
- 邀請尋求加入團隊的新用戶

### 描述更新腳本 (`scripts/update_description.py`)
該腳本負責更新 Habitica 隊伍的描述，動態獲取內容並進行更新。它的關鍵功能包括：
- 每日從外部 API 獲取的靈感語句
- 自動更新隊伍描述，確保信息新鮮感十足！

## 日誌文件 📜
所有執行操作的日誌都會記錄在 `logs` 文件夾中，方便您查看執行歷史和排查潛在問題。

## 開始使用 🚀

1. 克隆項目倉庫
2. 安裝依賴：`pip install -r requirements.txt`
3. 使用 GitHub Actions 自動化工作流，享受無縫的成員管理體驗！

## 參與貢獻 💡
如您希望為這個項目做出貢獻，歡迎提交 PR 或提出問題！讓我們一起讓 Habitica 更精彩！⭐️

感謝您閱讀本項目的 README 文件！期待您的加入與支持，快來 ⭐️ 這個項目吧！