[Back to main language README](README.md)

# 🥳 自動化團隊管理工具 README

歡迎使用我們的自動化團隊管理工具！這個專案旨在通過與 Habitica API 的整合，提升團隊管理的效率與參與感。💼✨

## 📁 檔案概述

### 1. GitHub Actions 工作流程
- **路徑**: `.github/workflows/automated_party_management.yml`
- **功能**: 該工作流程每 10 分鐘觸發一次（也可以手動運行），包含以下關鍵步驟：
  - 檢出程式碼
  - 設置 Python 環境
  - 安裝依賴
  - 執行管理腳本以處理 Habitica 平台的團隊成員
  - 運行更新腳本記錄變更
- **特點**: 包含暫停功能以管理請求速率，最後將任何日誌變更提交並推送到代碼庫。🔄

### 2. 授權協議
- **檔名**: `LICENSE`
- **內容**: 內容為 Apache 授權，版本 2.0，概述了軟件及相關作品的使用、複製和散佈的條款與條件，包括定義、用戶權限、再散佈要求及免責聲明。📜

### 3. 成員管理腳本
- **檔名**: `manage_members.py`
- **功能**: 此 Python 腳本旨在管理 Habitica 平台中的團隊成員，主要功能包括：
  - **日誌設置**: 初始化日誌以跟蹤腳本操作，包括錯誤和一般信息。
  - **速率限制**: 實施機制以遵循 API 請求限制，透過控制請求時間進行管理。
  - **成員管理**:
    - 確定並檢索基於最後登錄時間的非活躍團隊成員。
    - 在移除成員前發送私信通知。
    - 向團隊聊天發送成員移除的通知。
  - **邀請功能**: 尋找正在尋找團隊的用戶，並向他們發送邀請，包括格式化的消息列表出被邀請的成員。
  - **實用工具**: 包含處理 API 響應、發送消息及根據用戶活動計算時間的輔助函數。

總之，此腳本通過自動化非活躍用戶的移除和新用戶的邀請，提升了 Habitica 的團隊管理，促進了更好的用戶參與。🎉

### 4. 描述更新腳本
- **檔名**: `update_description.py`
- **功能**: 此 Python 腳本旨在更新 Habitica 團隊的描述，功能包括：
  - 日常獲取一句話和團隊成員的最後登錄詳情。
  - 日誌記錄、執行 API 請求的速率限制。
  - 根據檢索的數據動態更新團隊描述。
  - 從模板檔案讀取描述格式，編譯成員信息，並向 Habitica API 發送更新請求。
  - 記錄操作過程中的成功與錯誤。

## 🛠️ 安裝與使用

1. 克隆本倉庫：
   ```bash
   git clone https://github.com/yourusername/repository.git
   cd repository
   ```

2. 設置 Python 環境：
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. 安裝依賴：
   ```bash
   pip install -r requirements.txt
   ```

4. 配置 GitHub Actions 工作流程（若需要），並在 Habitica API 中生成一個有效的密鑰。

5. 運行腳本：
   ```bash
   python manage_members.py
   python update_description.py
   ```

## 💡 貢獻

歡迎任何形式的貢獻！如有建議或問題，請提交 issue 或發起 pull request。😊

## 📞 聯繫

如果您有任何問題或反饋，請通過以下方式聯繫我：
- 郵箱: your_email@example.com
- GitHub: [你的GitHub用戶名](https://github.com/yourusername)

感謝您使用我們的工具，祝您在 Habitica 中的團隊管理更加順利！🎊