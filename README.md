## python-atcoder

* VSCode の Remote - DevContaienr 拡張機能を使って環境を整える
* Task
  * acc new
    * コンテストのデータをダウンロード
  * test && submit
    * テストが成功したら提出する


### 初期設定

* ログイン
  * $ acc login
  * $ oj login https://atcoder.jp/
* 問題をインストールするときに全問インストールするように変更
  * $ acc config default-task-choice all
* テンプレートファイルの修正
  * 移動
    * $ cd `acc config-dir`
  * Python ディレクトリを作成して、main.py と template.json の作成をする
    ```sh
    mkdir `acc config-dir`/python
    touch `acc config-dir`/python/template.json `acc config-dir`/python/main.py
    code `acc config-dir`/python/template.json
    ```

    * template.json の編集
      ```json
      {
          "task": {
              "program": [
                  "main.py"
              ],
              "submit": "main.py"
          }
      }
      ```
* デフォルトのテンプレートを Python に変更
  * $ acc config default-template python