## coming_readerのGCP認証

### 1. 環境変数を設定
```bash
touch .env
```
TARGET_URLとAUDIENCEはGCPのCloud RunのURLを設定してください。
パスの指定を間違えないようにしてください
```.env
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/gcp-credential.json"
TARGET_URL="GCP_CLOUD_RUN_URL"
AUDIENCE="GCP_CLOUD_RUN_URL"
```

### 2. 実行

```bash
go run main.go
```

