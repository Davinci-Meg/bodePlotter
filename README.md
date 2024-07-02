# Bode Plotter
(日本語版は[こちら](README-jp.md))

<img src="https://camo.qiitausercontent.com/eb8e0216005c7badaaa4bf7eb2be4d177990d747/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507974686f6e2d4632433633432e7376673f6c6f676f3d707974686f6e267374796c653d666f722d7468652d6261646765">

This repository contains code for generating an open-loop 2nd order Bode plot using Python and the control library.

## Installation

To use this code, follow these steps:

1. Clone the repository to your local machine.
   ```
   git clone https://github.com/Davinci-Meg/bodePlotter.git
   cd bodePlotter
   ```
3. Install the required dependencies by running the following command:
    ```
    pip install control matplotlib numpy
    ```
4. Run the code using a Python interpreter.

## Usage

To generate the Bode plot, simply run the `src/openloop-2ndOrder_bodePlot.py` script. The resulting plot will be saved as `img/openloop-2ndOrder_bodePlot.png`.
If yor want to know the data of which is genarated, simply run the `src/openloop-2ndOrder_bodePlot_savedata.py` script. The resulting plot will be saved as `src/ax1_data.csv` and `src/ax2_data.csv`.

## Example

Show the example of generated image.

![OpenGlass](img/Open-loop-bodePlot-example.png)

## Note

I do not take any responsibility for image generation. Please proceed at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
