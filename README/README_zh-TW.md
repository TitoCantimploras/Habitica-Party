<div align="center">

[简体中文](/README.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 🎉 自動化Party管理系統 📈

歡迎加入 **自動化Party管理系統** 項目！我們的目標是為 Habitica 用戶提供高效、便捷的Party管理工具。無論您是熱愛管理的領袖，還是希望積極參與的成員，這裡都有您所需的工具和文檔！✨

## 🚀 項目結構

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml    # GitHub Actions 工作流程文件
├── LICENSE                                    # 項目許可證
├── documents                                  # 項目文檔資料夾
│   ├── brief_description.md                   # 簡要描述文檔 
│   ├── new_members.md                         # 新成員列表文檔 
│   ├── party_description.md                   # Party描述文檔 
│   ├── remove_PM.md                           # 成員移除通知模板 
│   └── remove_members.md                      # 移除成員記錄模板 
├── logs                                        # 日志文件夾
│   ├── manage_members.log                     # 成員管理日志
│   └── update_description.log                 # 描述更新日志
├── requirements.txt                           # 依賴文件 
└── scripts                                     # 腳本目錄
    ├── manage_members.py                      # 管理成員的腳本 
    └── update_description.py                  # 更新Party描述的腳本 
```

## 📄 文件簡介

| 文件名                                   | 描述                                                         |
|---------------------------------------|------------------------------------------------------------|
| **automated_party_management.yml**    | 每 10 分鐘自動運行的 GitHub Actions 工作流程文件，負責管理團隊任務。通過設置 Python 環境、安裝依賴，並執行成員管理和描述更新腳本，確保您的Party始終保持活躍！ 🎯 |
| **brief_description.md**              | 提供每日一句名言及其翻譯，促進語言學習和社區參與。該文檔還會自動更新最新成員信息，保障內容的新鮮。 🌱 |
| **new_members.md**                    | 記錄新成員的邀請，強調社區的積極參與。該文檔通過定時操作更新，確保您不會錯過任何新夥伴的加入！ 👥 |
| **party_description.md**              | 闡述Party的宗旨與規則，鼓勵成員分享個人體驗並積極參與任務。同時，內容中包含存在主義與虛無主義的討論，幫助您在生活中探索更深的意義。 📚 |
| **remove_PM.md**                      | 一份友好的通知模板，用於告知因活躍度不佳而被移除的成員，並提供重新加入的選項，提升溝通的友好度與效率。 🤝 |
| **remove_members.md**                 | 記錄成員被移除的原因和相關鏈接，確保管理過程透明，並定期更新以便審計與記錄。 🔍 |
| **requirements.txt**                  | 列出所需的 Python 依賴，確保您的環境設置一致，以便輕鬆安裝所需庫。 ⚙️ |
| **manage_members.py**                 | 管理Party成員的腳本，包括不活躍成員的刪除、邀請發送及日誌記錄等功能，簡化管理過程。 ⚡️ |
| **update_description.py**             | 自動更新Party描述的腳本，確保您每日都有更新的內容與成員分享，增強參與感。 🌟 |

## 如何使用

1. **Fork 本項目**: 點擊右上角的 "**Fork**" 按鈕。
2. **配置 API Token**: 在您的克隆項目中的 Actions secrets 中配置您的 Habitica API token 和 ID。
3. **自定義模板**: 根據需要修改 `documents` 文件夾中的模板，確保佔位符不被破壞。
4. **享受自動化管理**: 完成上述步驟後，您將能夠實現期望的自動化管理！ 🚀

## 🌟 如何貢獻

如果您覺得這個項目對您有所幫助，或者希望參與其中，歡迎為我們的項目加個 ⭐️！您的支持是我們最大的動力！期待您提供建議、報告問題或貢獻代碼，歡迎您的參與！💪

## 📧 聯繫我們

如您有任何問題或建議，請隨時通過 Issues 與我們聯繫，我們會儘快回覆您！😉

感謝您對自動化Party管理系統的關注，祝您使用愉快！🎉