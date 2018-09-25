[![OpenSource](https://img.shields.io/badge/Open-Source-orange.svg)](https://github.com/doyousketch2)  [![PythonVersions](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)  [![License](https://img.shields.io/badge/license-AGPL-lightgrey.svg)](https://www.gnu.org/licenses/agpl-3.0.en.html)  [![Git.io](https://img.shields.io/badge/Git.io-fANWr-233139.svg)](https://git.io/fANWr) 

**Noobtown**  --  Automate builds in Minetest  

Completed:  
- [x] Main Menu  
- [x] Calibration Screen  
- [x] locate Minetest window, and raise focus  
- [x] retrieve X, Y coordinates from screen  
- [x] generate all craft-grid coords, given upper-left and lower-right corners  
- [x] generate all inventory coords, given a1 and h8 corners  
- [x] Python global hotkey hook, so you can tap \` to return  
- [x] save data in Python's .pickle format  
- [x] screenshot function  
- [x] OCR the XYZ coords  
- [x] RGB PixelAt(x,y) color function  
- [x] .pitch CSM to report tilt of camera view  

To-do:  
- [ ] create a simple scripting language  
+ **N**orth,  **S**outh,  **E**ast,  **W**est  
+ **L**eft,  **R**ight,  **F**orward,  **B**ackward  
+ **C**hop,  **P**lace a block,  look **U**p,  look **D**own  
+ **1**-**8** will select that inventory slot  
+ **J**ump,  **H**old shift,  **R**elease shift  
+ # comments  
- [ ] add some kind of looping functionality  
+ letter followed by number will repeat that many times  
- [ ] OCR xyz >> movement >> OCR xyz >> compare routine  
- [ ] pixel RGB >> action >> pixel RGB >> compare if item's been placed / used  
- [ ] .pitch >> OCR >> .pitch >> compare camera view tilt  


`sudo pip3 install keyboard`  
(or)  
`sudo python3 -m pip install keyboard`  

ended up importing keyboard instead of keybinder  
better examples, can get it to run, but you have to use sudo...  

`sudo ./noobtown`  
(or)  
`sudo python3 -m noobtown`  
