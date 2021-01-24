<br />
<p align="center">
  <h3 align="center">TeasyStructure: Structure for Run tests generated in Teasy Language.</h3>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About Project](#about-project)
- [Starting](#starting)
  - [Installation](#installation)
  - [Languages Used](#languages-used)
  - [How to Use](#how-to-use)
  - [Best Pratices](#best-pratices)
  - [Files by directories](#files-by-directories)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About Project

This project aims provide a structure to run Teasy robot files generated.

## Starting

### Installation

This project not contains installation. **But** this project **require Robot Framework installed**. Install Robot using below steps.

1. Install Python 3
```
https://www.python.org/downloads/
```

2. Install Robot Framework
```
pip3 install robotframework
```

3. Install Selenium for Robot Framework
```
pip3 install --upgrade robotframework-seleniumlibrary
```

3. Install your browser driver (below chrome driver) and insert in system variable path
```
https://chromedriver.chromium.org/downloads
```

### Languages used

- [Robot Framework (Python Version)](https://robotframework.org/)
- [Teasy Language (Generate Robot Files)](https://github.com/yuryalencar/Teasy)
- [Teasy FSM Generator (Tests files)]()

### How To Use

1. Copy all files for yours [respective directory](#files-by-directories).
2. Run your tests
```
robot -d ./logs tests
```

### Best Pratices

1. Run yours tests using `-d ./logs` for organize log files.

### Files by directories

Below is a list of the files by directory.

|               Directory | Files in folder                                                               |
| ----------------------: | ----------------------------------------------------------------------------- |
|                `config` | **config.robot** and **page_register.config.robot** for config and imports all robot pages.  |
|            `components` | **components.robot** all components of the system.                            |
|                 `tests` | All files of **.tests.robot** extension, contains all execution test cases.   |
|                 `pages` | All files of **.pages.robot** extension, contains all pages of the system (Page Object Pattern).|
|         `pages/commons` | **hooks.pages.commons.robot** for setup tests and tests teardown.             |

## Contributing

Contributions are what make the open source community an incredible place to learn, inspire and create. Any contribution you make will be **much appreciated**.
1. Make a project Fork
2. Create a Branch for your feature (`git checkout -b feature/amazing-feature`)
3. Insert your changes (`git add .`)
4. Make a commit with your changes (`git commit -m 'feat(<teasy-filename>): Inserting a Amazing Feature !`)
5. Push the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

Distributed under the MIT license. See `LICENSE` for more information.

## Contact

Yury Alencar - [Github](https://github.com/yuryalencar) - **yuryalencar19@gmail.com**
