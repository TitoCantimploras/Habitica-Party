[Back to main language README](README.md)

# 🎉 聚會管理工具

## 🚀 專案介紹

歡迎來到聚會管理工具的專案！本專案旨在提供一個高效的解決方案，幫助用戶管理聚會活動。通過使用 GitHub Actions，我們可以定期自動執行兩個 Python 腳本，從而簡化聚會組織過程中的管理任務。無論是朋友聚會、團隊活動還是其他社交場合，這個工具都能幫助你輕鬆安排。

## 📦 安裝步驟

在開始使用聚會管理工具之前，請確保你的開發環境中已安裝 [Python](https://www.python.org/downloads/) 和 [Git](https://git-scm.com/downloads)。

1. **克隆倉庫**

   ```bash
   git clone https://github.com/你的用戶名/聚會管理工具.git
   cd 聚會管理工具
   ```

2. **安裝依賴**

   請確保在你的虛擬環境中安裝所需的依賴項：

   ```bash
   pip install -r requirements.txt
   ```

## 📄 使用說明

1. **配置腳本**

   在使用之前，請根據你的需求配置 `script1.py` 和 `script2.py` 文件，確保它們具備正確的參數和設置。

2. **手動執行**

   你可以手動執行腳本來測試功能：

   ```bash
   python script1.py
   python script2.py
   ```

3. **自動化執行**

   通過 GitHub Actions，腳本將根據預設的時間表自動執行。你可以在 `.github/workflows` 目錄中查看和調整工作流。

## 🤝 貢獻指南

我們歡迎任何形式的貢獻！如果你想為聚會管理工具貢獻代碼，請遵循以下步驟：

1. **Fork 此倉庫**
2. **創建一個新的分支**

   ```bash
   git checkout -b feature/你的特性
   ```

3. **提交更改**

   ```bash
   git commit -m "添加了一項新特性"
   ```

4. **推送到分支**

   ```bash
   git push origin feature/你的特性
   ```

5. **提交 pull request**

請描述清楚你的更改和功能。感謝你的貢獻！💪

## 📜 授權

本專案遵循 [Apache License, Version 2.0](LICENSE)。請確保遵循授權條款，以便合法使用、複製和發佈本軟件。

---

感謝閱讀本 README 文件，祝你使用愉快！如果你有任何問題或建議，請隨時與我們聯繫！😊