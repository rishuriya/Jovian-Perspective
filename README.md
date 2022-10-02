
# Jovian Perespective

A Image processing software for process image of Jovian system. The Images was capture by the junocam of Nasa. This is the project for Nasa space app challenge.


## Deployment

To deploy this project, Make a empty directory name 'Temp', you have updated version of Python and pip, To download the required Package run

```bash
    pip install -r requirements.txt
```
To run the project, give command of

```bash
    python start.py
```

## User Instructions

- ### Sharpness

    This particular feature allows the user to sharp the input image using a slider.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458062-a8f9295e-ba90-4ce2-9c61-ead0904b8d9e.png)

- ### Auto Enhance
    There are two types of enhancment provided by us. 
    
    1) The first one just enhances based of the mean and variance of the colors and brightness of each pixels.
    
    ![image](https://user-images.githubusercontent.com/91690484/193459988-6ac51381-6fd3-40af-90cd-a9036f415ce8.png)

    2) The second one ehnances the image in a different way by changing colors to make it more accurate. It make the features more visible
    
    ![image](https://user-images.githubusercontent.com/91690484/193460676-abbb6d19-a3b1-4725-bf97-ad4703e752eb.png)

- ### Edge Dectection
    
    This feature detects the edges in an image acoording to it's kernel size which can be controlled by the slider. Our application uses SobelY to detect the edges.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458715-9a26ae6d-6d8a-4d84-bfb2-b88e6735e9ba.png)

- ### Brightness Coreection
    
    This allows the user to change the brightness in an image using the given slider.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458763-3e48b8e7-bd48-419f-b686-e5325f0c6593.png)

- ### Color Variation

    User can change the intensity of the each colors; Red, Blue and Green seperately using respective sliders.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458825-52fca65f-592a-469d-92f2-edb299ad5271.png)

- ### Denoising

    This feature reduces the noise in the images where noises can be found **else it might just make the image a bit foggy.**
    
    ![image](https://user-images.githubusercontent.com/91690484/193458873-48437c8d-2f41-4681-bb4e-76c8d8513398.png)

- ### Gamma Correction

    Allows the user to change the gamma values till *100* using a given slider.
    
    ![image](https://user-images.githubusercontent.com/91690484/193458962-31031598-333f-46b3-827b-030434555320.png)



## Screenshots
Screenshot of the Home Page of Software

![App Screenshot](https://github.com/rishuriya/nasa-spaceapp/blob/master/Resource/Screenshot%20from%202022-09-30%2019-32-49.png)

