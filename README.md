# goodbye-trump-twitter

(English / [日本語](README-ja.md))

"goodbye-trump-twitter" is a TwitterBOT that immediately blocks any user who has a Donald Trump icon on their timeline or among their followers.



## Requirements

macOS or Linux (Windows not officially supported, but might work)

### WindowsUsers.......(under verification)

Install WSL while reading [this](Install_wsl.md) section, and then run the installation on WSL.



## Usage

```bash
$ gbtrump run
```

If you only want to check the operation

```bash
$ gbtrump once
```

See help for a detailed explanation.

```bash
$ gbtrump --help
```



## Install

```bash
$ pip3 install git+https://github.com/RiniaOkyama/goodbye-trump-twitter

$ gbtrump reset
```

Enter the necessary information (e.g., the key used by the Twitter API).     

```bash
$ vi ~/.gbtt.conf
```

### Do you get a dlib error?

<!--
Pre-reqs:
- Python 3 must be installed; on MacOS, install from homebrew or from the official website; on Linux, install using a package manager.
  
- macOS:
  - Install Xcode (or install XcodeCommandLineTools, if you have it).
- Linux:
  - $ sudo apt install $(cat . /linux_dlib_require.txt) to install the necessary packages.

- These instructions assume you don't have an nVidia GPU and don't have Cuda and cuDNN installed and don't want
  GPU acceleration (since none of the current Mac models support this).

-->

Clone the code from github:

```bash
git clone https://github.com/davisking/dlib.git
```

```bash
cd dlib
python3 setup.py install
```

Install goodbye-trump-twitter again, and if there is no error, you are done.

```bash
$ pip3 install git+https://github.com/RiniaOkyama/goodbye-trump-twitter
```


# LICENSE

'goodbye-trump-twitter' is under the MIT license.

