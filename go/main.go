package main

import (
	"context"
	"fmt"
	"io"
	"log"
	"os"

	"github.com/joho/godotenv"
	"google.golang.org/api/idtoken"
)

func makeGetRequest(w io.Writer, targetURL string, audience string) error {
	ctx := context.Background()
	client, err := idtoken.NewClient(ctx, audience)
	if err != nil {
		return fmt.Errorf("idtoken.NewClient: %w", err)
	}
	resp, err := client.Get(targetURL)
	if err != nil {
		return fmt.Errorf("client.Get: %w", err)
	}
	defer resp.Body.Close()
	if _, err := io.Copy(w, resp.Body); err != nil {
		return fmt.Errorf("io.Copy: %w", err)
	}
	return nil
}

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Println("注意: .env ファイルの読み込みに失敗しました。外部で設定された環境変数に依存します:", err)
	}
	googleAppCreds := os.Getenv("GOOGLE_APPLICATION_CREDENTIALS")
	targetURL := os.Getenv("TARGET_URL")
	audience := os.Getenv("AUDIENCE")

	if googleAppCreds == "" {
		log.Println("警告: GOOGLE_APPLICATION_CREDENTIALS が .env または環境変数に設定されていません。")
	} else {
		fmt.Printf("使用する GOOGLE_APPLICATION_CREDENTIALS (from .env or env): %s\n", googleAppCreds)
	}

	if targetURL == "" {
		log.Fatal("エラー: TARGET_URL が .env または環境変数に設定されていません。")
	}
	if audience == "" {
		audience = targetURL
		log.Println("警告: AUDIENCE が設定されていなかったため、TARGET_URL と同じ値を使用します。")
	}

	fmt.Printf("ターゲットURL: %s\n", targetURL)
	fmt.Printf("オーディエンス: %s\n", audience)

	err = makeGetRequest(os.Stdout, targetURL, audience)
	if err != nil {
		log.Fatalf("リクエストの送信に失敗しました: %v", err)
	}

	fmt.Println("\nリクエストは正常に完了しました。")
}
