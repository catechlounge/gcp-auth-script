## coming_readerのGCP認証
(参考)GoogleCloudサービス間認証
[https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token](https://cloud.google.com/run/docs/authenticating/service-to-service?hl=ja#run-service-to-service-example-python)

### 1. 環境変数を設定
/go または /python ディレクトリで作成してください
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

pythonの場合はrequirements.txtを作成してください
requirements.txt
```txt
python-dotenv
google-auth
requests
```

### 2. 実行
goの場合
```bash
go mod tidy
```

```bash
go run main.go
```

pythonの場合
1. 仮想環境を作成
```bash
python3 -m venv venv
```

2. 仮想環境をアクティベート
```bash
source venv/bin/activate
```

3. 依存関係をインストール
```bash
pip3 install -r requirements.txt
```

4. 実行
```bash
python3 main.py
```

5.仮想環境を終了
```bash
deactivate
```





