---
title: Imaginary Landscapes
id: 1408255772646386308
author: Kirby Urner
published: 2010-09-07T15:12:00.000-07:00
updated: 2010-09-07T16:14:19.551-07:00
blog: bizmo_diaries
tags: 
---

Malcolm Tredinnick is a master of GeoDjango, which talks the language of maps.  He demonstrated an imaginary landscape he'd devised.  The PNG provides texture, but the underlying TIFF, some 19 MB of data, provides the real details.OpenLayers serves as a clearinghouse, knows where to go for what data to populate the different layers.  Show all restaurants of a given type in a given zip code area.  PostGIS supports data selection based on bounding boxes, so when you zoom in or pan, it sends back the right objects.  You'll want to cache tiles, especially the background ones that don't change.  Several open source projects do this, and support Python bindings.Mapnik is another piece of the puzzle, a strong source of Earthling data.Malcolm emphasized the importance of using a whole planet, even if your region is but a small island.  The geometry engines all assume a latitude-longitude context.Given my Geometry + Geography paradigm, I'm of course interested to what extent internal anatomy might be considered a GIS problem.  Bodies are not planets, but they are geospatial.What file formats accommodate both planets and livers?  When one zooms in, on a city street, it's worthwhile to show infrastructure, such as under-street pipes, optical fibers.  One zooms in on a body the same way, showing what's inside.  Indeed bodies walk on sidewalks.  Geography is all inclusive of special case "scenes" whereas geometry is generic (about shape in general -- what we call "pre-frequency" in Synergetics).  [Does x3D (VRML) support GIS](http://www.cadmaps.com/gisblog/?p=53)?