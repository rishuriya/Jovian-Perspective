
# 🚀 Jovian Perspective 

Our project aims to develop an easy-to-use desktop application which can process the planetary images as per the user's requirements. It can perform various operations on the image such as auto-enhancement, sharpening, edge detection, increasing brightness, color variation, denoising and gamma correction. As per the challenge, the application can process the JunoCam raw images in different ways to be used by scientists for research purposes or by artists for creative use. 
Processing the images in different aspects is important as it can provide better details for studying the state of the planets and can also provide a better visualization.
## 👩‍💻 Technology Stack
- Python
- PyQt
- opencv
- pillow
## 🛠 Installation instructions 

Write the following code to clone the repository
```bash
git clone https://github.com/rishuriya/nasa-spaceapp
```

To install all the required packages type the following code
```bash
pip install -r requirements.txt
```

To Start the application, type
```bash
python start.py
```
## 📚 User Instructions 

- ### Sharpness

    This particular feature allows the user to sharpen the input image using a slider.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458062-a8f9295e-ba90-4ce2-9c61-ead0904b8d9e.png)

- ### Auto Enhance
    We have provided two types of enhancement: 
    
    1) The first one enhances the image based on the mean and variance of the colors, and brightness of each pixel.
    
        ![image](https://user-images.githubusercontent.com/91690484/193459988-6ac51381-6fd3-40af-90cd-a9036f415ce8.png)

    2) The second one equalizes the image by improving the contrast of the colors to make it more accurate. It makes the features more visible.
    
        ![image](https://user-images.githubusercontent.com/91690484/193460676-abbb6d19-a3b1-4725-bf97-ad4703e752eb.png)

- ### Edge Detection
    
    This feature detects the edges in the image according to the kernel size which can be controlled by the slider. Our application uses SobelY to detect the edges.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458715-9a26ae6d-6d8a-4d84-bfb2-b88e6735e9ba.png)

- ### Brightness Correction
    
    This allows the user to change the brightness of the image by using the given slider.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458763-3e48b8e7-bd48-419f-b686-e5325f0c6593.png)

- ### Color Variation

    User can change the intensity of each color; Red, Blue and Green seperately; using respective sliders.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458825-52fca65f-592a-469d-92f2-edb299ad5271.png)

- ### Denoising

    This feature reduces the noise in those images which contain noise **else it might just make the image a bit foggy.**
    
    ![image](https://user-images.githubusercontent.com/91690484/193458873-48437c8d-2f41-4681-bb4e-76c8d8513398.png)

- ### Gamma Correction

    This allows the user to change the gamma values till *100* using a given slider.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458962-31031598-333f-46b3-827b-030434555320.png)

## Team Members
<table>
    <tr>
    <td align="center"><a href="https://github.com/rishuriya"><img src="https://avatars.githubusercontent.com/u/85174423?v=4" width="100px;" alt=""/><br /><sub><b>Rishav Kumar</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Harikrishna-AL"><img src="https://avatars.githubusercontent.com/u/91690484?v=4" width="100px;" alt=""/><br /><sub><b>Harikrishna Pillai</b></sub></a><br /></td>

    <td align="center"><a href="https://github.com/Pakhi07"><img src="https://avatars.githubusercontent.com/u/92666755?v=4" width="100px;" alt=""/><br /><sub><b>Pakhi Banchalia</b></sub></a><br /></td>

    <td align="center"><a href="https://github.com/yasharora102"><img src="https://avatars.githubusercontent.com/u/29159814?v=4" width="100px;" alt=""/><br /><sub><b>Yash Arora</b></sub></a><br /></td>
    </tr>
</table>


