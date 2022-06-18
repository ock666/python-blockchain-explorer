<div id="top"></div>

![Contributors][contributors-shield]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Python Blockchain</h3>

  <p align="center">
    A blockchain coded in python
    <br />
    <a href="https://github.com/ock666/python-blockchain"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/ock666/python-blockchain/issues">Report Bug</a>
    ·
    <a href="https://github.com/ock666/python-blockchain/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#API">API</a></li>
    <li><a href="#features">Features</a></li> 
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


A blockchain explorer written in python which is meant to interface with my other project [Python Blockchain](https://www.github.com/ock666/python-blockchain)



Here's why:
* To provide a front-end to more easily view the chain data
* For fun and learning
* because I have no friends

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Flask](https://flask.palletsprojects.com/)
* [Requests](https://pypi.org/project/requests/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Be sure to read this readme in full before trying to get set up or submitting any issues to the repo.

### Prerequisites

Install the requirements with
* pip
  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ock666/python-blockchain-explorer.git
   ```
2. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Run explorer.py to start the webpage.
   ```sh
   python3 explorer.py
   ```


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

* Start the block explorer with:
```sh
python3 explorer.py
```
* Provide the address of a blockchain node to the explorer.py CLI

* Navigate to 127.0.0.1:5000 or $your_local_IP_address:5000 
* The web interface should load immediately, if not check the console window for any errors.
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- FEATURES -->

## Features

### Search
search the chain for block index, transaction hash, or public address to see details of the requested information.

### Block View 
View block data including transactions in blocks.

### Address View
View details pertaining to an address on the chain, including sent and received transactions, and balance.

### Transaction View
View transaction data.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Create templates for block, address, and transaction views.
- [x] Write functions to return chain data.
- [ ] Implement CSS styling.
- [ ] Come up with some more ideas for the roadmap.



See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [Oskar Petersen](https://www.linkedin.com/in/oskar-petersen-39a849185/) - oskargjerlevpetersen@gmail.com

Project Link: [https://github.com/ock666/python-blockchain-explorer](https://github.com/ock666/python-blockchain)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ock666/python-blockchain-explorer.svg?style=for-the-badge
[contributors-url]: https://github.com/ock666/python-blockchain-explorer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ock666/python-blockchain-explorer.svg?style=for-the-badge
[forks-url]: https://github.com/ock666/python-blockchain-explorer/network/members
[stars-shield]: https://img.shields.io/github/stars/ock666/python-blockchain-explorer.svg?style=for-the-badge
[stars-url]: https://github.com/ock666/python-blockchain-explorer/stargazers
[issues-shield]: https://img.shields.io/github/issues/ock666/python-blockchain-explorer.svg?style=for-the-badge
[issues-url]: https://github.com/ock666/python-blockchain-explorer/issues
[license-shield]: https://img.shields.io/github/license/ock666/python-blockchain-explorer?style=for-the-badge
[license-url]: https://github.com/ock666/python-blockchain-explorer/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/oskar-petersen-39a849185/
