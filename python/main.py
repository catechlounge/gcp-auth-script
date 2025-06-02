import os
import sys
import urllib.request
from dotenv import load_dotenv

import google.auth.transport.requests
import google.oauth2.id_token

def make_authorized_get_request(endpoint: str, audience: str) -> bytes:
    req = urllib.request.Request(endpoint)

    auth_req = google.auth.transport.requests.Request()
    id_token_fetched = google.oauth2.id_token.fetch_id_token(auth_req, audience)

    req.add_header("Authorization", f"Bearer {id_token_fetched}")

    try:
        response = urllib.request.urlopen(req)
        return response.read()
    except urllib.error.HTTPError as e:
        error_body = ""
        try:
            error_body = e.read().decode('utf-8', errors='replace')
        except Exception:
            pass
        raise Exception(f"HTTPError: {e.code} {e.reason}. Body: {error_body}") from e
    except Exception as e:
        raise Exception(f"Request failed: {e}") from e

if __name__ == "__main__":
    if not load_dotenv():
        print("注意: .env ファイルの読み込みに失敗しました。外部で設定された環境変数に依存します。")

    google_app_creds = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    target_url = os.getenv("TARGET_URL")
    audience = os.getenv("AUDIENCE")

    if not google_app_creds:
        print("警告: GOOGLE_APPLICATION_CREDENTIALS が .env または環境変数に設定されていません。")
    else:
        print(f"使用する GOOGLE_APPLICATION_CREDENTIALS (from .env or env): {google_app_creds}")

    if not target_url:
        print("エラー: TARGET_URL が .env または環境変数に設定されていません。")
        sys.exit(1)

    if not audience:
        audience = target_url
        print("警告: AUDIENCE が設定されていなかったため、TARGET_URL と同じ値を使用します。")

    print(f"ターゲットURL: {target_url}")
    print(f"オーディエンス: {audience}")

    try:
        response_body_bytes = make_authorized_get_request(target_url, audience)
        print(response_body_bytes.decode('utf-8'))
        print("\nリクエストは正常に完了しました。")
    except Exception as e:
        print(f"リクエストの送信に失敗しました: {e}")
        sys.exit(1)
