## セットアップ

* clone
  * $ gh repo clone tamago324/python-atcoder
* clone したディレクトリを VSCode で開く
  * 「開発コンテナで開きますか？」というダイアログが表示されるため、再度開くを選択して開発コンテナを起動する

### 初期設定

* ログイン
  * $ acc login
  * $ oj login https://atcoder.jp/

## python-atcoder

* VSCode の Remote - DevContaienr 拡張機能を使って環境を整える

* Task (`tasks.json`参照)
  * download
    * コンテストのデータをダウンロード
    * `contests` 配下にダウンロードされる
  * test && submit
    * サンプルでのテストと提出
      * テストが成功したら提出を実行する
  * sample
    * サンプルを使って実行する
* Debug (`launch.json`参照)
  * 「sampleを指定してデバッグ」
    * サンプルデータを指定してデバッグを実施

