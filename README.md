## python-atcoder

* VSCode の Remote - DevContaienr 拡張機能を使って環境を整える
* Task
  * acc new
    * コンテストのデータをダウンロード
  * test && submit
    * テストが成功したら提出する
* Debug
  * 「sampleを指定してデバッグ」
    * サンプルデータを指定してデバッグを実施


### 初期設定

* ログイン
  * $ acc login
  * $ oj login https://atcoder.jp/
* テンプレートのコピー
  ```
  chmod +x __template/copy-script.sh
  ./__template/copy-script.sh
  ```