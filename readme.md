# D2ApiSamples
- EN: This is begginer's tutorial for [Destiny2](https://www.bungie.net/7/en/Destiny) guardians who want to try python coding with [Bungie API](https://bungie-net.github.io/multi/index.html).
- JP: [Bungie API](https://bungie-net.github.io/multi/index.html)を使ってPythonプログラミングをしてみたい[Destiny2](https://www.bungie.net/7/ja/Destiny)ガーディアン向けのチュートリアルです。
- Japanese follows English / 日本語説明は後半へ

# What does this code do?


`d2api_hello.py` will do:
- Read your Bungie API keys.
- Connect to bungie server with OAuth2
    - Save access token to your local storage so that you won't need to copy&paste(step4) every run.
- Retrive your bungie user profile and show in json style.

# Environment
- Python 3.11.4
    - requests-oauthlib: Run `pip install requests requests-oauthlib` to install.
- Windows10 64bit
- Bugie API key
    - You need to register a new application at https://www.bungie.net/en/Application to get an API key and client IDs.
    - In my test environment I set "Confidential" for OAuth Client Type.
    - Redirect URL must match in python code(`REDIRECT_URL`) and registration page.

# How to run
1. Clone the repository to your python directory.
2. Open `d2api_hello.py` and replace following variables with your own Keys/IDs defined in https://www.bungie.net/en/Application.
    - `API_KEY`       -> API Key
    - `CLIENT_ID`     -> OAuth client_id
    - `CLIENT_SECRET` -> OAuth client_secret
    - `REDIRECT_URL`  -> Redirect URL
3. `d2api_hello.py`を実行
4. Access to the Authorization link(shown in terminal) with your browser and log in to bungie.net.
    ```
    Authorization link: https://www.bungie.net/en/OAuth/Authorize?******************************************
    Paste url link here:
    ```
    - Then you will be redirected to `REDIRECT_URL`.
        - In this sample I set my github page, but you can replace it with any link.
    - Copy the URL from your browser's address bar and paste to your terminal.
5. If everything was ok, your bungie account profiles will be retrieved from the server and shown in your terminal as json style.
6. Your Authorization token will be saved as `token_file` in the same directory once you granted connection to bungie server with this code.
    - Next time you won't need do step4 unless you delete token_file.

# Next Step
- Read [Bungie API references](https://bungie-net.github.io/multi/index.html) and build your own application!

# 環境
- Python 3.11.4
    - requests-oauthlib: `pip install requests requests-oauthlib` でインストール
- Windows10 64bit
- Bungie APIキー
    - https://www.bungie.net/ja/Application へアクセスしてアプリケーション登録を行い、APIキーとクライアントIDを取得しておいてください。
    - テスト環境では"OAuthクライアントタイプ"は"機密"に設定しています。
    - "リダイレクトURLへリンク"はコード内の`REDIRECT_URL`と一致している必要があります。

# これは何をするプログラム？
`d2api_hello.py` の機能：
- Bungie APIキーの読み込む。
- OAuth2を使いBungieサーバーに接続する。
    - アクセストークンをローカルに保存し、実行の度に手順4のコピペ作業が発生しないようにしている。
- Bungieユーザデータを取得し、JSON形式で表示する。

# 使い方
1. リポジトリをクローン
2. `d2api_hello.py` を開き、下記の変数を自分のAPIキー等に置き換え。
    - `API_KEY`       -> APIキー
    - `CLIENT_ID`     -> OAuth client_id
    - `CLIENT_SECRET` -> OAuth client_secret
    - `REDIRECT_URL`  -> リダイレクトURLへリンク
3. `d2api_hello.py`を実行
4. 下記のようにAuthorization linkがターミナルに表示されるのでブラウザでアクセスする。Bungie.netログインが必要。
    ```
    Authorization link: https://www.bungie.net/en/OAuth/Authorize?******************************************
    Paste url link here:
    ```
    - ログイン後、`REDIRECT_URL`へ飛ばされる。
        - このサンプルではCryMateのgithubページにしているが好きなページに変更可能。
    - リダイレクトされたページのリンクをブラウザアドレスバーからコピーし、ターミナルの `Paste url link here`に貼り付け。
5. ここまでうまくいっていれば、自分のBungieアカウント情報がjson形式でターミナルに表示される。
6. 一度このコードでBungieサーバとの認証に成功すると、認証トークンが同フォルダに`token_file`として保存される。
    - `token_file`を削除しない限り、次にこのコードを実行した時は手順4は要求されない。

# 次のステップ
- [Bungie APIリファレンス](https://bungie-net.github.io/multi/index.html)を読んで、好きなアプリケーションを開発しましょう!

# Author
- CryMate
    - [Github:CryMate](https://github.com/CryMate)
    - [Twitter:@cry_mate](https://twitter.com/cry_mate)