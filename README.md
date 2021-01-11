# goodbye-trump-twitter

"goodbye-trump-twitter" is a TwitterBOT that immediately blocks any user who has a Donald Trump icon on their timeline or among their followers.



## Requirements

macOS or Linux (Windows not officially supported, but might work)

### WindowsUsers.......(under verification)

Install WSL while reading [this](Install_wsl.md) section, and then run the installation on WSL.



## Usage

```bash
$ gbtrump run
```


## Install

```bash
$ pip3 install git+https://github.com/RiniaOkyama/goodbye-trump-twitter

$ gbtrump reset

$ vi ~/.gbtt.conf
```

### dlib error?

Pre-reqs:
- Have Python 3 installed. On macOS, this could be installed from homebrew or even via standard 
  Python 3.6 downloaded installer from https://www.python.org/download. On Linux, just use your
  package manager.
- On macOS:
  - Install XCode from the Mac App Store (or install the XCode command line utils).
  - Have [homebrew](https://brew.sh/) installed
- On Linux:
  - For a full list of apt packages required, check out the [example Dockerfile](https://github.com/ageitgey/face_recognition/blob/master/Dockerfile#L6-L34) and copy what's installed there.
  - These instructions assume you are using Ubuntu 16.04 or newer. If you are using 14.04, you can try [these installation instructions instead](https://github.com/ageitgey/face_recognition/issues/120) to work around the old CMake version.
- These instructions assume you don't have an nVidia GPU and don't have Cuda and cuDNN installed and don't want
  GPU acceleration (since none of the current Mac models support this).

Clone the code from github:

```bash
git clone https://github.com/davisking/dlib.git
```

Build the main dlib library (optional if you just want to use Python):

```bash
cd dlib
mkdir build; cd build; cmake ..; cmake --build .
```

Build and install the Python extensions:

```bash
cd ..
python3 setup.py install
```

Install goodbye-trump-twitter again, and if there is no error, you are done.

```bash
$ pip3 install git+https://github.com/RiniaOkyama/goodbye-trump-twitter
```


# LICENSE

'goodbye-trump-twitter' is under the MIT license.

