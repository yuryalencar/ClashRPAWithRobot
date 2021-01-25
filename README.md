<br />
<p align="center">
  <h3 align="center">RPA: An Sample Using Robot Framework.</h3>
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

This project aims provide a sample robot to get and generate an csv with members of the Clash Royale Based in start tag information.

## Starting

### Installation

For run this project is required: Robot Framework and Playwright. For install use below steps.

1. Install Python 3
```
https://www.python.org/downloads/
```

2. Install Robot Framework
```
pip3 install robotframework
```

3. Install Playwright to Robot Framework
```
pip3 install robotframework-browser
```

### Languages used

- [Robot Framework (Python Version)](https://robotframework.org/)
- [Playwright (Robot Version)](https://robotframework-browser.org/)

### How To Use

1. Copy your `config.example.robot` to `config.robot`.
```
cp config.example.robot config.robot
```
2. Configure your `config.robot` file setting your respective user.
```
OBS.: IN ${TAG_CLA_START} VARIABLE REPLACE '#' TO '%23'
```
3. Run your Robot
```
robot -d ./logs  --loglevel <INFO | DEBUG> robots
```

### Best Pratices

1. Run yours tests using `-d ./logs` for organize log files.

### Files by directories

Below is a list of the files by directory.

|               Directory | Files in folder                                                               |
| ----------------------: | ----------------------------------------------------------------------------- |
|                `config` | **config.robot** and **page_register.config.robot** for config and imports all robot pages.  |
|            `components` | **components.robot** all components of the system.                            |
|                `robots` | Contains all robots execution.   |
|                 `pages` | Contains all pages of the system (Page Object Pattern and Page Factory).|
|         `pages/commons` | **hooks.robot** for setup robot and robot teardown.             |

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
