## Melisandre

Melisandre is a futuristic UI for the lovely virtual assistant [Melissa](https://github.com/Melissa-AI/Melissa-Core/). Melisandre uses Google Chrome's speech-to-text engine (works only with Chrome). This project is currently under development and has Melissa as a dependancy.

Check out our [wiki](https://github.com/Melissa-AI/Melissa-Core/wiki), where we have installation and configuration instructions for Melissa, usage guide as well as relevant documentation. Credits to [Nakul Saxena](http://nakulsaxena.in) for designing and developing this awesome interface.

### Installation of Melisandre

After installing Melissa-Core, issue the following commands on your terminal:

```
git clone https://github.com/Melissa-AI/Melisandre.git
cd Melisandre
pip install -r requirements.txt
FLASK_APP=main.py flask run
```

Open `http://127.0.0.1:5000` on Chrome and click on the lock icon in the center of the UI. This will open up the Melisandre console for Melissa. Click on the big panel on the right side of the interface to start the speech recognition.

### Discussion and Support

If you face an issue or require support, please take a look through the GitHub Issues, as you may find some useful advice there. If you are still facing issues, feel free to create a post at our [Google Group Forum](https://groups.google.com/forum/#!forum/melissa-support--discussion-forum/) describing the issue and the steps you have taken to debug it.

### Licence

[The MIT License (MIT)](https://github.com/Melissa-AI/Melisandre/blob/master/LICENSE.md)
