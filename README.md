# Cayenne PCF8574 Plugin
A plugin allowing the [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent) to to read data from and write data to a PCF8574 device and display it in the [Cayenne Dashboard](https://cayenne.mydevices.com).

## Requirements
### Hardware
* [Rasberry Pi](https://www.raspberrypi.org).
* [PCF8574](http://www.ti.com/product/PCF8574).

### Software
* [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent). This can be installed from the [Cayenne Dashboard](https://cayenne.mydevices.com).
* [Git](https://git-scm.com/).

## Getting Started
### 1. Installation

   From the command line run the following commands to install this plugin.
   ```
   cd /etc/myDevices/plugins
   sudo git clone https://github.com/myDevicesIoT/cayenne-plugin-pcf8574.git
   ```

### 2. Modifying the plugin

   Specify the device you are using by setting the `class` value under the `PCF8574` section in the `cayenne-mcp23xxx.plugin` file.
   By default this is set to `PCF8574` but it can also be set `PCF8574A`.

   By default the plugin alternates between input and output channels. To specify different functions for specific channels you
   can modify the `class` for that section to specify `DigitalInput` or `DigitalOutput`.

### 3. Restarting the agent

   Restart the agent so it can load the plugin.
   ```
   sudo service myDevices restart
   ```
   Temporary widgets for the plugin should now show up in the [Cayenne Dashboard](https://cayenne.mydevices.com). You can make them permanent by clicking the plus sign.

   NOTE: If the temporary widgets do not show up try refreshing the [Cayenne Dashboard](https://cayenne.mydevices.com) or restarting the agent again using `sudo service myDevices restart`.