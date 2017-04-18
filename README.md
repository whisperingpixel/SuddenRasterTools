# SuddenRasterTools

I have collected set of tools, which I use to make my life easier. With this plugin, I try to put all of them in a QGIS plugin and hope, it might be useful for other users as well.



# Installation

Copy the files into your plugin directory, e.g., in:

    ~/.qgis2/python/plugins


# Usage

Select a categorical raster file. The button "Pixel Class Statistics" calculates some pixel-statistics. The button "Object Class Statistics" calculates some object-statistics. Note that an object is generated with the "polygonize" function of QGIS, i.e., all pixels, which have the same cell values in a 4x4 neighbourhood will be connected.

# Development

This plugin is constantly under development. The first aim is to provide a working environment for the promises I made in "Usage".

