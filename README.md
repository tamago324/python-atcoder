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
  * Python ディレクトリを作成して、main.py と template.json の作成をする
    ```sh
    mkdir -p `acc config-dir`/python
    cd __template
    cp template.json `acc config-dir`/python/template.json 
    cp main.py `acc config-dir`/python/main.py
    cp -f config.json `acc config-dir`/config.json
    ```