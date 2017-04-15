# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SuddenRasterTools
                                 A QGIS plugin
 This is a tool collection for raster processing
                             -------------------
        begin                : 2017-04-15
        copyright            : (C) 2017 by none
        email                : none
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SuddenRasterTools class from file SuddenRasterTools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .suddenrastertools import SuddenRasterTools
    return SuddenRasterTools(iface)
