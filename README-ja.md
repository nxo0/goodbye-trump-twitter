# goodbye-trump-twitter

([English]() / 日本語)

"goodbye-trump-twitter" は、タイムラインやフォロワーからドナルド・トランプ氏のアイコンのユーザーを発見し, ブロックするTwitterBOTです。



## 要件

MacOSもしくはLinux.(Windowsも頑張れば動くかもしれません。)

### WindowsUserの方.......(under verification)

WSLで動かすほうが手っ取り早いかもしれません。 [this](Install_wsl.md) 


## 使い方

``bash
$ gbtrump run
```

実験で一度だけ実行したい場合:

```bash
$ gbtrump once
```

詳細はhelpを参照してください。

```bash
$ gbtrump --help
```



## インストール

```bash
$ pip3 install git+https://github.com/RiniaOkyama/goodbye-trump-twitter

$ gbtrump reset
```

必要な情報（TwitterAPIで使用するキーなど）を入力してください。
```bash
$ vi ~/.gbtt.conf
```

### dlib errorがでますか？

手動で入れる必要があるみたいです。

要件:
- Python3がインストールされていること。MacOSではhomebrewからインストールするか公式サイトからインストールしてください。Linuxでは、パッケージマネージャーを使用してインストールしてください。
  
- macOS:
  - Xcodeをインストールしてください（またはXcodeCommandLineToolsをインストールしてください。)
- Linux:
  - $ sudo apt install $(cat ./linux_dlib_require.txt) を実行して必要なパッケージをインストールしてください。

これらの手順は、nVidia GPUを持っておらず、CudaとcuDNNがインストールされておらず、GPUアクセラレーションを必要としないことを前提としています（現在のMacモデルはどれもこれをサポートしていないため）


```bash
git clone https://github.com/davisking/dlib.git
```

Build the main dlib library (optional if you just want to use Python):

```bash
cd dlib
mkdir build; cd build; cmake ..; cmake --build .
```

```bash
cd ..
python3 setup.py install
```

もう一度 goodbye-trump-twitterをインストールしてみる。

```bash
$ pip3 install git+https://github.com/RiniaOkyama/goodbye-trump-twitter
```

エラーが出ますか？その場合はご連絡ください。


# LICENSE

'goodbye-trump-twitter' は MIT License です。

