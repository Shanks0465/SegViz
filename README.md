
![facebook_cover_photo_2](https://user-images.githubusercontent.com/48712410/95494985-651f8c00-09bc-11eb-8d6d-e1b169271be6.png)
<br />
<p align="center">

  <h3 align="center">SegViz -  A Simple Segmentation Tool</h3>

  <p align="center">
    An Image Segmentation Tool made using OpenCV and Tkinter
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [License](#license)
* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project



### Built With
This application was built using the following Libraries.
* [OpenCV](https://opencv.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Pillow](https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html)



<!-- GETTING STARTED -->
## Getting Started

To start segmenting your images or build upon this code base, get a local copy up and running follow these simple steps.

### Prerequisites

Setup a suitable Python Environment or [PyCharm Environment](https://www.jetbrains.com/pycharm/)

### Installation

1. Clone the repo
```sh
git clone https://github.com/Shanks0465/SegViz.git
```
2. Install the required libraries
```sh
cd SegViz && pip install -r requirements.txt
```
3. Download ActiveTcl for Tkinter [ActiveTCL](https://www.activestate.com/products/tcl/downloads/)

4. Run the Application
```sh
python ImSegApp.py
```



<!-- USAGE EXAMPLES -->
## Usage

* Run the App, You'll be presented with mini application view. Click on Select Folder and Choose the image folder.

![SegVizLanding](https://user-images.githubusercontent.com/48712410/95497131-7ae28080-09bf-11eb-8fd1-76150d44a85c.PNG)

* You'll be presented with a application view with a buffer SegViz Image and a List on the left. Click on an Image on the list.

![SegVizCanvas](https://user-images.githubusercontent.com/48712410/95497140-7ddd7100-09bf-11eb-97ea-ba776f5374b7.PNG)

* You can either click or use arrows to traverse the list.

![SegVizCanvasImage](https://user-images.githubusercontent.com/48712410/95497148-82a22500-09bf-11eb-9ecd-0436283fd5b9.PNG)

* Double Left Click on the Image Canvas to place points to mark the region.

![SegVizCanvasImagePoints](https://user-images.githubusercontent.com/48712410/95497157-8635ac00-09bf-11eb-80b7-e159f42fd0e8.PNG)

* Choose a color from the palette by selecting Select Color Button.

![SegVizCanvasImageColorChoose](https://user-images.githubusercontent.com/48712410/95497171-89309c80-09bf-11eb-8361-96d35f6afedf.PNG)

* After Choosing Right click to generate the segment region

![SegVizCanvasImageSeg](https://user-images.githubusercontent.com/48712410/95497181-8c2b8d00-09bf-11eb-89ac-954355a8cffd.PNG)

* After segmenting and annotating the image, Click on Save Segmentation to save it inside /Segmentation folder at your images root directory.



<!-- ROADMAP -->
## Roadmap

Future Features may include:
* MRCNN Auto Image Segmentation
* Pan and Zoom Features
* Auto Save and Formatting ( Pascal VOC, COCO )


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [Umashankar](https://www.linkedin.com/in/shankar-kumar-74a228146/) - umashanks99@gmail.com

Project Link: [SegViz](https://github.com/Shanks0465/SegViz)








