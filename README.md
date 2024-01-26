# ISPTool_Cross_Platform
ISPTool_Cross_Platform is a C++ project with sample codes base on different languages, which provide Nuvoton ISP function for Windows/Linux/MacOS platform.
## How to Use
1. Build the ISP_Lib code into a shared library base on the platform (.dll for Windows and .so for Linux/MacOS)
2. Choose one of the Sample Code or modify it to use.
3. Configure target chip to boot from LDROM with LDROM ISP code.
4. Connect with target board base on the supported interface.
5. Run the code.
## Sample Code Introduce
### ISPTool_SampleCode_C99
> ISPTool_SampleCode_C99 is a simple C code that use Nu-Link2-Pro as the device and support UART interface.  
> In order to use this sample, program the file into Nu-Link2-Pro's data flash and check the data flash base address.  
> Modify function DO_ISP to decide the program data place and length.  
> Connect Nu-Link2-Pro UART2 to target's ISP UART port and press the button on Nu-Link2-Pro (PC.7) to start.  
### ISP_Command_Line_Tool_SampleCode
> ISP_Command_Line_Tool_SampleCode is a command line tool base on Python3.  
> It support USB/ UART/ I2C/ SPI/ CAN/ RS485 interfaces in Windows/ Linux/ MacOS interface.  
> Nu-Link2-Pro is needed in I2C/ SPI/ CAN/ RS485 interfaces.  
> Make sure that shared library ISPLib.dll/ ISPLib.so has been placed in the same folder of the script isp_command_line.py.  
> Since the information of NuVoice chip is store in the library GetChipInformation.dll, it only supported in Windows platform.  
> Install the following Python modules to use this sample: pyserial, hidapi.  
### ISP_Tool_SampleCode
> ISP_Tool_SampleCode is a Python3 tool with GUI made by PyQt5.  
> It support USB/ UART/ I2C/ SPI/ CAN/ RS485 interfaces in Windows/ Linux/ MacOS interface.  
> Nu-Link2-Pro is needed in I2C/ SPI/ CAN/ RS485 interfaces.  
> Make sure that shared library ISPLib.dll/ ISPLib.so has been placed in the same folder of the script ISP_Sample.py  
> Since the information of NuVoice chip is store in the library GetChipInformation.dll, it only supported in Windows platform.  
> Install the following Python modules to use this sample: pyserial, hidapi, PtQt5.    
